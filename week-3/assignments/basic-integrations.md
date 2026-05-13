# Dialogflow CX Integrations – Practical Assignments

These assignments guide associates through real-world Dialogflow CX integrations:

1. Cloud Run Webhook (Python)
2. Dialogflow Messenger + Cloud Storage Deployment
3. Conversational Phone Gateway + Logging + UI Customization

---

# Assignment 1: Cloud Run Webhook (Python)

## Objective
Build a simple Dialogflow CX webhook using Python on Cloud Run.

## Requirements
- Google Cloud Project
- Cloud Run enabled
- Dialogflow CX agent

---

## Step 1: Create a new Webhook with the inline editor on Cloud Run

Follow the prompts for creating a simple webhook using python

## Step 2: Webhook Code (main.py)

Below is a sample. Feel free to modify it to your agent's design

```python
import functions_framework
from flask import jsonify

@functions_framework.http
def webhook(request):
    req = request.get_json(silent=True)

    tag = req.get("fulfillmentInfo", {}).get("tag", "")
    params = req.get("sessionInfo", {}).get("parameters", {})

    if tag == "math_add":
        a = float(params.get("a", 0))
        b = float(params.get("b", 0))
        response_text = f"The sum is {a + b}"

    elif tag == "welcome":
        name = params.get("name", "there")
        response_text = f"Hello {name}, welcome to Dialogflow CX!"

    else:
        response_text = "Webhook received but no matching tag found."

    return jsonify({
        "fulfillment_response": {
            "messages": [
                {"text": {"text": [response_text]}}
            ]
        }
    })
```

---

## Step 3: requirements.txt

```
flask==3.*
functions-framework==3.*
```

---

## Step 4: Connect to Dialogflow CX
- Go to Webhooks section
- Add Cloud Run URL
- Create routes using tags:
  - math_add
  - welcome
    - These are both samples, modify the code above and use different tags if you want

---

# Assignment 2: Dialogflow Messenger + Cloud Storage

## Objective
Deploy a chatbot embedded in a hosted “About Me” page.

---

## Step 1: About Me Webpage

Use the About me page you created and deployed in a previous assignment as the base for your agent's deployment

---

## Step 2: Enable Messenger
- Dialogflow CX → Integrations → Enable Messenger
- Copy Code and add to your HTML file

---

## Step 3: Deploy to Cloud Storage
- Create bucket
- Upload index.html
- Make public and accessible as a website (follow previous instructions if needed)

---

## Step 4: Access Site

```
https://storage.googleapis.com/YOUR_BUCKET_NAME/index.html
```

---

# Assignment 3: Conversational Phone Gateway

## Objective
Deploy a voice agent using Dialogflow CX Phone Gateway.

---

## Step 1: Enable Phone Gateway
- Dialogflow CX → Integrations → Phone Gateway
- Enable and assign number

---

## Step 2: Build Voice Flow
- Welcome intent
- Help intent
- Basic fallback handling

---

## Step 3: Customize UI
- Change theme colors
- Enable call transcript
- Enable visual companion UI

---

## Step 4: Enable Logging
- Cloud Logging in settings → Logs Explorer

## Step 5: Test Call
- Verify flow works
- Check logs
- Confirm no dropped sessions

---
