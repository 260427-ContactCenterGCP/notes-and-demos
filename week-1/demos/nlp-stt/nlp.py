# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

def analyze_text(text):
    document = language_v1.Document(
        content=text,
        type_=language_v1.Document.Type.PLAIN_TEXT,
    )

    # Sentiment Analysis
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    # Entity Detection
    entities = client.analyze_entities(
        request={"document": document}
    ).entities

    print("\n==============================")
    print(f"Text: {text}")
    print("------------------------------")
    print(f"Sentiment Score: {sentiment.score}")
    print(f"Magnitude: {sentiment.magnitude}")

    print("\nEntities:")
    for entity in entities:
        print(f" - {entity.name} ({language_v1.Entity.Type(entity.type_).name})")

# 🔹 TEST WITH 3 SAMPLES
analyze_text("I absolutely love this phone but the battery is terrible.")
analyze_text("This laptop is fast and lightweight, but the screen is disappointing.")
analyze_text("Global markets rally after central bank announces rate cuts.")