from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

text = "Once upon a time, in a dark forest, a mysterious shadow appeared."

synthesis_input = texttospeech.SynthesisInput(text=text)

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

with open("plain_output.wav", "wb") as out:
    out.write(response.audio_content)

print("Plain TTS audio generated.")