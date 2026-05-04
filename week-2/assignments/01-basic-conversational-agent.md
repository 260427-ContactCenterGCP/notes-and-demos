# Neon Arcade Chatbot Assignment

## Overview

You are building a conversational assistant for a retro arcade called **Neon Arcade**. The assistant helps users purchase game passes, check available games, and learn about pricing and rewards.

This assignment is designed to help you practice:

* Intent-based routing
* Entity extraction and normalization
* Form-based data collection
* Conditional conversation logic
* Multi-turn conversational design

---

## Bot Concept

**Neon Arcade Assistant**

Users interact with the bot to:

* Buy arcade game passes
* Ask about available games
* View pricing information

The bot should feel fun, energetic, and slightly playful while still behaving like a structured transactional assistant.

---

## Required Flows

You must implement the following flows:

### 1. Default Flow (Routing Only)

This flow should:

* Identify user intent
* Route users to the correct specialized flow

Supported intents:

* Buy Game Pass
* Check Games / Availability
* Pricing Inquiry
* Fallback handling

---

### 2. Game Pass Purchase Flow (MAIN FLOW)

This is the primary structured flow and must include a form.

#### Form Requirements

Collect the following parameters:

**Required fields:**

* player_name
* pass_type
* duration
* start_date
* favorite_genre

---

#### Personalization Logic (Conditional Routing)

Add at least one conditional response based on `favorite_genre`:

Examples:

* Fighting games → mention tournaments or arcade fighters
* Racing games → mention racing games
* Retro games → mention classic arcade machines
* Rhythm games → mention music-based cabinets

---

### 3. Information Flow (Can be within default flow)

This flow handles general questions.

Supported topics:

* Available games
* Pricing information

Responses can be static or lightly dynamic, but should not require forms.

---

## Required Intents

You must define at least the following intents:

### Buy Game Pass Intent

Triggers the Game Pass Purchase Flow.

Example phrases:

* I want a game pass
* Buy a day pass
* I want to play at the arcade
* Get me access to Neon Arcade

---

### Check Games Intent

Handles game availability questions.

Example phrases:

* What games do you have?
* Is Street Fighter available?
* What can I play there?

---

### Pricing Intent

Handles pricing questions.

Example phrases:

* How much is a pass?
* What does it cost?
* Pricing info

---

## Required Entities

### pass_type (Custom Entity)

Values:

* day pass
* weekend pass
* unlimited pass

Synonyms:

* full access → unlimited pass
* daily pass → day pass
* weekend → weekend pass

---

### duration (Custom Entity)

Values:

* 1 hour
* 3 hours
* all day
* weekend

---

### favorite_genre (Custom Entity)

Values:

* fighting
* racing
* retro
* rhythm
* shooter

Synonyms:

* fighting games → fighting
* racing games → racing
* old games → retro

---

### System Entities

Use built-in system entities where applicable:

* Date (start_date)
* Any free text fallback if needed

---


## Submit a screenshot of your completed Dialogflow CX flow showing:

* Default routing flow
* Game Pass Purchase Flow with form

We will review and walk through each implementation together in the next session.

---

## Bonus (Optional)

* A “Start Over” handling route
* A playful confirmation message at the end of booking
* Additional genre-based responses

