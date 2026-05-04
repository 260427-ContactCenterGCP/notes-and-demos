# AI-Powered Contact Center MVP 

## Project Overview

The AI-Powered Contact Center project focuses on designing, building, and demonstrating a cloud-native customer support solution using Google Cloud Platform (GCP) and Google Customer Engagement Suite (CES).

The goal is to deliver a functional **Minimum Viable Product (MVP)** that demonstrates:

- Intelligent customer support through **chat and voice**
- A structured **Dialogflow CX** virtual agent with multiple business flows
- Use of **Generative AI Playbooks** for dynamic support
- At least one **custom third-party integration**
- **Voice telephony support** through an external provider
- **Human escalation** supported by **Agent Assist**
- Testable, demonstrable, and enterprise-style architecture

Requirements are subject to change at Trainer's discretion depending on time and capacity restraints

---

# MVP Goal

Build and demonstrate an AI-powered support center for a fictional business that supports:

1. **Customer self-service via chat**
2. **Customer self-service via voice**
3. **Generative AI support for open-ended requests**
4. **Escalation to human support**
5. **Agent Assist recommendations during live handoff**
6. **Basic analytics and testing coverage**

The final product should feel like a small but realistic enterprise contact center experience.

---

# Recommended Business Scenarios (Choose One)

Teams may choose any support domain, but should keep scope tight.

Recommended scenarios:

- **E-Commerce Support**
  - Order status
  - Returns/refunds
  - Product inventory lookup
  - Escalation to support agent

- **Healthcare Clinic Support**
  - Appointment scheduling
  - Insurance FAQ
  - Prescription refill routing
  - Escalation to staff

- **Banking / Financial Services**
  - Account FAQs
  - Card issue reporting
  - Branch / hours lookup
  - Escalation to live support

- **Telecom / ISP Support**
  - Service outage checks
  - Billing support
  - Plan changes
  - Escalation to agent

- **Travel / Hospitality**
  - Reservation lookup
  - Booking changes
  - Refunds/cancellation policy
  - Escalation to support

---

# MVP Scope (Required Features)

## 1. Conversational Agent (Dialogflow CX)

Build a **Dialogflow CX virtual agent** that supports both structured and natural conversation.

### Minimum Requirements

- At least **3 core customer support flows**
- At least **1 reusable shared flow**
- At least **2 entities**
- At least **5 intents**
- At least **1 form-driven flow**
- At least **1 webhook / integration route**
- Clear fallback and recovery handling
- Session parameter usage
- Conditional routing

### Recommended Flows

#### Core Flows (Choose 3+)
- Order / account lookup
- Returns / refunds
- Product / inventory lookup
- Appointment / reservation management
- Billing support
- Technical issue troubleshooting

#### Shared Flow
- Authentication / identity verification
- Human escalation
- Business hours / contact info
- FAQ / policy flow

### Expectations

The bot should feel like a real support assistant, not just a FAQ tree.

It must demonstrate:

- Guided support flows
- Branching logic
- Parameter capture
- Clarification handling
- Recovery from invalid input
- Realistic conversation design

---

## 2. Generative AI (Playbooks)

The MVP must include **Generative AI features** using **Playbooks**.

### Minimum Requirements

Use Playbooks for at least **one open-ended support experience** where deterministic flow logic is too rigid.

Examples:

- Product recommendation assistant
- Policy Q&A
- Troubleshooting assistant
- “Explain my issue” freeform intake
- Natural language FAQ summarization

### Expectations

Playbooks should demonstrate:

- Prompt grounding
- Safe tool usage
- Context-aware responses
- Controlled generative behavior
- Proper handoff back into deterministic flow when needed

---

## 3. Third-Party Integration (Custom Integration)

The MVP must include at least **one custom integration** with an external system.

This should simulate a realistic business dependency.

### Minimum Requirements

Build one integration that the bot calls during a support flow.

### Example Integrations

- CRM customer lookup
- Order management API
- Product inventory service
- Appointment system
- Ticket / case creation
- Loyalty / membership lookup

### Implementation Options

- Dialogflow CX webhook
- Cloud Run service
- Simple REST API
- Mock service with static JSON
- Firebase / Firestore-backed service

### Expectations

Integration should demonstrate:

- Request/response flow
- Parameter passing
- Real business data usage
- Error handling
- Returned data displayed in conversation

---

## 4. Voice / Telephony Integration

The MVP must support **voice interaction**, not just chat.

### Minimum Requirements

Integrate the agent with at least one external telephony path for a live voice demo.

### Expectations

Teams must demonstrate:

- Inbound voice interaction
- Speech-to-Text working
- Text-to-Speech responses
- Voice-specific prompt tuning
- At least one voice test case

---

## 5. Human Escalation + Agent Assist

The MVP must include **human handoff** and **Agent Assist**.

### Minimum Requirements

At least one flow must escalate from bot to human.

Example:
- Refund dispute
- Escalated complaint
- Complex billing issue
- Failed authentication
- Customer frustration detected

### Agent Assist Must Demonstrate

At minimum, show one of:

- Suggested knowledge articles
- Suggested responses
- Real-time agent guidance
- Context surfaced from conversation

### Expectations

This should demonstrate:

- Bot-to-human transfer logic
- Context carryover
- Agent support augmentation
- Hybrid automation model

---

## 6. Testing & Validation

Teams must produce test coverage and validation artifacts.

### Minimum Requirements

- Intent test cases
- Flow routing tests
- Happy path tests
- Failure path tests
- Integration validation
- Voice test scenario
- Escalation test scenario

### Expected Deliverables

- Test case matrix
- Example transcripts
- Failure scenario coverage
- Known limitations list

---

## 7. Analytics / Insights (Lightweight)

Full analytics depth is not required for MVP, but teams should demonstrate awareness of operational insights.

### Minimum Requirements

Demonstrate one of:

- Basic conversation review
- Intent match review
- Escalation tracking
- Conversation quality observations
- Conversational Insights overview 

---

# Final Demo Expectations

Teams should demonstrate:

1. Customer interacts via chat
2. Bot handles structured support flow
3. Bot calls external integration
4. Bot uses generative AI for open-ended help
5. Customer calls via voice
6. Voice interaction succeeds
7. Complex issue escalates to human
8. Agent Assist supports live agent
9. Team reviews test evidence and architecture

This should feel like a realistic enterprise customer support experience.

---

# Success Criteria

A successful MVP demonstrates:

- Strong conversational design
- Real business workflow support
- Effective use of deterministic + generative AI
- Working external integration
- Voice capability
- Human escalation
- Agent Assist usage
- Testing discipline
- Clear enterprise architecture thinking

---