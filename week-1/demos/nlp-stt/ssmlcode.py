from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

ssml_text = """
<speak>
  <p>
    <s>Once upon a time...</s>
    <break time="1s"/>
    <s>in a <emphasis level="strong">dark forest</emphasis>,</s>
    <break time="500ms"/>
    <s>a <prosody rate="slow" pitch="-2st">mysterious shadow</prosody> appeared.</s>
  </p>
</speak>
"""

synthesis_input = texttospeech.SynthesisInput(ssml=ssml_text)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

with open("ssml_output.wav", "wb") as out:
    out.write(response.audio_content)

print("SSML TTS audio generated.")