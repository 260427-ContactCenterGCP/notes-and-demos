
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
import os

# YOUR PROJECT ID
PROJECT_ID = "project-012adcd5-76a1-4b22-b06"

# YOUR LOCATION
LOCATION = "us-east1"

# Create client
client = SpeechClient(
    client_options={"api_endpoint": f"{LOCATION}-speech.googleapis.com"}
)

def transcribe_audio(filename):
    # Get absolute path (fixes relative path issues)
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "resources", filename)

    print("\n==============================")
    print(f"Processing file: {file_path}")
    print("------------------------------")

    # Read audio file
    with open(file_path, "rb") as f:
        audio_content = f.read()

    # Configure request
    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=["en-US"],
        model="short",
    )

    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{PROJECT_ID}/locations/{LOCATION}/recognizers/_",
        config=config,
        content=audio_content,
    )

    # Call API
    response = client.recognize(request=request)

    # Print results
    if not response.results:
        print("No transcription results.")
        return

    for result in response.results:
        alt = result.alternatives[0]
        print(f"Transcript: {alt.transcript}")
        print(f"Confidence: {alt.confidence}")


# 🔹 TEST FILES

# Clean audio 
transcribe_audio("Sandshrew.wav")