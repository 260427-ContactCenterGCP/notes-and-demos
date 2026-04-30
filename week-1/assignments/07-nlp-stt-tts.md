# Google Cloud AI API Lab Bundle

## Overview
This assignment bundle is designed to give you hands-on experience with three core Google Cloud AI APIs:

1. Natural Language Processing (NLP)
2. Speech-to-Text (STT)
3. Text-to-Speech (TTS)

You have been provided starter code in the course repository (read through the code and interpret to the best of your ability). Your job is to clone the notes-and-demos repo, configure your environment, run the provided examples, and complete the tasks below.

---

# Prerequisites

Before beginning:

- Clone the provided repository
- Ensure you have:
  - Google Cloud SDK (`gcloud`) installed
  - Authentication configured
  - Required Python libraries installed (google-cloud-language and google-cloud-speech)
- Confirm the following APIs are enabled in your GCP project:
  - Cloud Natural Language API
  - Cloud Speech-to-Text API
  - Cloud Text-to-Speech API

---

# Assignment 1: Natural Language API Exploration

## Objective
Use the Google Cloud Natural Language API to analyze text and observe how GCP extracts meaning from language.

## Task
Run the provided NLP example and test it with **3 different text samples** of your choosing.

You may use:
- a tweet
- a product review
- a news headline
- a paragraph from a blog
- a short conversation snippet

## For each text sample
Run the NLP script and capture output for:

- Sentiment analysis
- Entity detection

## Deliverable
- 3 text samples tested
- API output (copy/paste or screenshots)

## Goal
Understand how GCP interprets written language and where NLP performs well or poorly.

---

# Assignment 2: Speech-to-Text API Exploration

## Objective
Use Google Cloud Speech-to-Text to transcribe spoken audio and evaluate transcription quality.

## Task
Run the provided Speech-to-Text example using **2 audio samples**.

### Audio Requirements
1. Clean audio sample
   - Clear voice
   - Minimal background noise
   - 10–30 seconds

2. Difficult audio sample
   - Background noise, music, overlapping speech, accent, or poor mic quality
   - 10–30 seconds

You may record your own audio or use public/royalty-free clips.

## For each audio sample
Capture:

- Transcript
- Confidence score (if available)

## Deliverable
- Audio files
- Transcripts
- Confidence scores

## Goal
Understand how audio quality impacts speech recognition.

---

# Assignment 3: Text-to-Speech API Exploration (Plain Text + SSML)

## Objective
Use Google Cloud Text-to-Speech to generate speech and compare plain text vs SSML-enhanced speech.

## Task
Generate **two versions** of the same short text:

1. Plain text TTS
2. SSML-enhanced TTS

Choose:
- a short fairy tale excerpt OR
- a short tweet / dramatic / humorous text

Keep it short (15–30 seconds spoken).

---

## Part A: Plain Text Version
Use default TTS example (no SSML).

---

## Part B: SSML Dramatic Version
Rewrite the same text using SSML.

Must include at least **3 SSML features**, such as:

- `<break>`
- `<emphasis>`
- `<prosody>`
- `<say-as>`
- `<p>`
- `<s>`

Goal: make it dramatic, theatrical, funny, or suspenseful.

---

## Deliverable
- Original text
- Plain text version
- SSML version
- Both audio files
- Be prepared to play both versions in class.

---

# Bonus (Optional)

Try additional experiments:
- Sarcasm in NLP
- Overlapping speech in STT
- Extreme SSML dramatization in TTS

Include observations if attempted.

---