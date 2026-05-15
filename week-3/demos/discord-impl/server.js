/**
 * TODO(developer):
 * Add your service key to the current folder.
 * Uncomment and fill in these variables.
 */
const projectId = 'YOUR-PROJECT-ID';
const locationId = 'us-central1';
const agentId = 'YOUR-AGENT-ID';
const languageCode = 'en';

const discordToken = process.env.DISCORD_TOKEN;

const express = require("express");
const server = express();

const { Client, GatewayIntentBits, Partials } = require('discord.js');

const bot = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.DirectMessages,
    GatewayIntentBits.MessageContent
  ],
  partials: [Partials.Channel, Partials.Message]
});

bot.login(discordToken)
  .catch(err => console.error("Discord login failed:", err));

bot.on('clientReady', () => {
  console.log(`Logged in as ${bot.user.tag}!`);
});

const structProtoToJson =
  require('../../botlib/proto_to_json.js').structProtoToJson;

const { SessionsClient } = require('@google-cloud/dialogflow-cx');

const client = new SessionsClient({
  apiEndpoint: locationId + '-dialogflow.googleapis.com'
});

function splitMessage(text, maxLength = 1900) {
  const chunks = [];

  while (text.length > maxLength) {
    let splitIndex = text.lastIndexOf('\n', maxLength);

    if (splitIndex === -1) {
      splitIndex = maxLength;
    }

    chunks.push(text.slice(0, splitIndex));
    text = text.slice(splitIndex).trim();
  }

  if (text.length > 0) {
    chunks.push(text);
  }

  return chunks;
}

function discordToDetectIntent(discordRequest, sessionPath) {
  return {
    session: sessionPath,
    queryInput: {
      text: {
        text: discordRequest.content,
      },
      languageCode,
    },
  };
}

async function detectIntentResponse(discordRequest) {
  try {
    const tenMinuteWindow = Math.floor(Date.now() / (1000 * 60 * 10));

    const sessionId = `${discordRequest.author.id}-${tenMinuteWindow}`;

    const sessionPath = client.projectLocationAgentSessionPath(
      projectId,
      locationId,
      agentId,
      sessionId
    );

    const request = discordToDetectIntent(discordRequest, sessionPath);

    const [response] = await client.detectIntent(request);

    return response;

  } catch (err) {
    console.error("detectIntent FAILED:", err);
    throw err;
  }
}

async function convertToDiscordMessage(responses) {
  let replies = [];

  for (let response of responses.queryResult.responseMessages) {
    let reply;

    switch (true) {
      case response.hasOwnProperty('text'):
        reply = response.text.text.join();
        break;

      case response.hasOwnProperty('payload'):
        reply = await structProtoToJson(response.payload);
        break;
    }

    if (reply) replies.push(reply);
  }

  return replies;
}

bot.on('messageCreate', async message => {
  if (message.author.id === bot.user.id || message.author.bot) return;

  let isReplyToBot = false;

  if (message.reference?.messageId) {
    try {
      const refMsg = await message.channel.messages.fetch(message.reference.messageId);
      isReplyToBot = refMsg.author.id === bot.user.id;
    } catch (err) {
      console.error("Reply fetch failed:", err);
    }
  }

  const shouldRespond =
    message.mentions.users.has(bot.user.id) ||
    message.channel.isDMBased() ||
    isReplyToBot;

  if (!shouldRespond) return;

  try {
    await message.channel.sendTyping();

    const responses = await detectIntentResponse(message);
    const replies = await convertToDiscordMessage(responses);

    for (const req of replies) {
      const chunks = splitMessage(req);

      for (const chunk of chunks) {
        await message.channel.send(chunk);
      }
    }

  } catch (err) {
    console.error("Handler error:", err);
  }
});

const PORT = process.env.PORT || 8080;

server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

module.exports = {
  discordToDetectIntent,
  convertToDiscordMessage
};