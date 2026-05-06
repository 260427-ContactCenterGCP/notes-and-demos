# Joke Assistant with Dynamic Types (API + Generative Playbook)

## Objective
Build a conversational agent that retrieves jokes from a public API using a **Generative Playbook**.

This assignment introduces:
- API integration
- Dynamic data retrieval
- Multi-step tool usage (IMPORTANT)
- Response formatting

---

## Scenario: Smart Joke Assistant

Your agent will:
1. Discover available joke types dynamically
2. Retrieve jokes based on user preference
3. Format responses in a clean, friendly way

---

## Required Documentation

Official Joke API:
https://github.com/15Dkatz/official_joke_api/tree/master

OpenAPI Specification Guide:
https://swagger.io/docs/specification/v3_0/basic-structure/

---

## Key Concept (IMPORTANT)

You are NOT hardcoding joke types.

Instead:

1. Call `/types` → get available types
2. Use one of those types
3. Call `/jokes/{type}/random`

---

## API Overview

Base URL:
https://official-joke-api.appspot.com

---

### Endpoint 1: Get Joke Types
GET /types

Response example:
["general", "programming", "knock-knock"]

---

### Endpoint 2: Get Joke by Type
GET /jokes/{type}/random

Example:
/jokes/programming/random

Response:
[
  {
    "type": "programming",
    "setup": "Why do programmers hate nature?",
    "punchline": "Too many bugs."
  }
]

---

## Step-by-Step Instructions

### 1. Create OpenAPI Spec
Define:
- /types (GET)
- /jokes/{type}/random (GET)

---

### 2. Create Generative Playbook

Name:
Joke_Assistant_Playbook

---

### 3. Playbook Behavior

Step 1 — Detect user intent
Step 2 — Call /types
Step 3 — Select type (user-provided or random)
Step 4 — Call /jokes/{type}/random

---

### 4. Response Formatting

Joke Type: [type]

Setup:
[setup]

Punchline:
[punchline]

---

### 5. Fallback Behavior

"I couldn’t fetch a joke right now, but I promise I’m funnier than this error."

---

## Example Inputs

- Tell me a joke
- Give me a programming joke
- Knock knock
- I’m bored
- Say something funny

---

## Test Questions

1. Tell me a joke  
2. Give me a programming joke  
3. What types of jokes are available?  
4. Give me a knock-knock joke  
5. Tell me a random joke  
6. Give me a joke I haven’t heard before  

---

## Evaluation Criteria

- Correct multi-step API usage
- Dynamic type handling
- Clean response formatting
- Proper fallback handling
