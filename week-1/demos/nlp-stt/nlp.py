# Imports the Google Cloud client library.
from google.cloud import language_v1
from pyasn1_modules.rfc7633 import Features

# Instantiates a client.
client = language_v1.LanguageServiceClient()

# CHANGE ME
text = "Hello, world!"

document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text.
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

# Add in details for checking the entities, classification, and moderation results

print(f"Text: {text}")
print(f"Sentiment: {sentiment.score}, Magnitude: {sentiment.magnitude}")