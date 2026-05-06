# GCP Conversational Agents- Playbooks

## What are Playbooks?

**Playbooks** represent the modern, generative evolution of Dialogflow CX. While traditional Dialogflow CX uses **Flows** and **Pages** to build a deterministic state machine, Playbooks use Large Language Models (LLMs) to orchestrate conversations using natural language instructions.

Playbooks are the core engine of a **Generative Agent**. Instead of mapping out every possible intent and transition, you provide the agent with a goal, a set of instructions, and examples of how to behave. The LLM then determines the best path to fulfill the user's request in real-time.

---

# Generative vs. Deterministic Agents

In the modern Conversational Agents ecosystem, you often use a hybrid approach combining both models.

| Feature | Deterministic (Flows) | Generative (Playbooks) |
| :--- | :--- | :--- |
| **Logic Construction** | Visual state machine (Nodes/Edges) | Natural language (Instructions) |
| **User Input** | Must match predefined **Intents** | Interpreted by LLM (Generative) |
| **Conversation Path** | Rigid and predefined | Dynamic and non-linear |
| **Maintenance** | High (Visual graphs get complex) | Medium (Focus on prompt engineering) |
| **Best For** | Transactions, strict compliance, payments | Reasoning, FAQs, troubleshooting, complex data collection |

[Reference: Generative vs. Deterministic](https://docs.cloud.google.com/dialogflow/cx/docs/generative-deterministic)

---

# Core Building Blocks of a Playbook

## 1. The Goal
The **Goal** is a high-level summary of what the playbook is designed to achieve. It acts as the "North Star" for the LLM during the session.

- **Purpose:** Sets the mission and scope for the agent.
- **Example:** "Help the user troubleshoot their home internet connection, verify their account status, and schedule a technician if a remote fix is not possible."

[Reference: Playbook Goal](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/goal)

---

## 2. Instructions
**Instructions** are the "code" of the playbook, written in natural language. They guide the agent through the steps it must take to achieve the goal.

### Characteristics of Effective Instructions
- **Imperative:** Use command-style language (e.g., "Ask for," "Verify," "Do not").
- **Structured:** Use numbered or bulleted lists for clear sequences.
- **Conditional:** Use "If/Then" logic to handle different scenarios.

### Example Instruction Set
1. Greet the user and ask for their name and account number.
2. Use the `AccountVerify` tool to check if the account exists.
3. If the account is invalid, inform the user and ask them to re-enter the details.
4. If the account is valid, ask the user to describe the issue.
5. If the issue is related to "Speed," use the `CheckSignal` tool.

[Reference: Playbook Instructions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/instruction)

---

## 3. Parameters
**Parameters** are the variables that store state and information during the conversation. Unlike traditional CX where you must manually map entities to parameters, Playbook LLMs perform **Automatic Parameter Extraction**.

### Types of Parameters
- **Input Parameters:** Data passed from a parent playbook or flow (e.g., `user_id`).
- **Output Parameters:** Data collected during the playbook to be passed back (e.g., `troubleshooting_result`).

### Parameter Extraction Example
If an instruction says "Collect the user's shipping address," and the user says "I live at 123 Maple St, Seattle," the LLM automatically maps that string to the `address` parameter.

[Reference: Playbook Parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter)

---

## 4. Examples (Few-Shot Prompting)
**Examples** are the most powerful way to ground the agent. They are sample transcripts of "Golden Conversations" that show the LLM exactly how to handle specific inputs and when to use tools.

- **User Utterance:** The predicted user input.
- **Agent Action:** The tool the agent should call.
- **Agent Response:** How the agent should reply to the user.

[Reference: Playbook Example](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example)

---

# Advanced Logic: Conditionals and Code Blocks

## Conditional Actions
Conditionals allow for complex branching logic based on the current state of parameters or tool outputs.

- **Syntax Example:**
  - "If the `customer_type` is 'Premium', offer a direct transfer to a human specialist."
  - "Else, continue with the automated troubleshooting steps."

[Reference: Conditional Actions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions)

---

## Code Blocks
Code blocks use a YAML-like syntax within the instructions to perform programmatic tasks, such as calling tools with specific arguments.

### Code Block Example
```yaml
- tool_call: check_flight_status
  arguments:
    flight_number: ${parameter.flight_id}
- condition: ${check_flight_status.is_delayed == true}
  instruction: "Inform the user about the delay and offer to rebook."
```

[Reference: Code Blocks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block)

---

# Integration: Tools and Data Stores

## Tools
**Tools** are the "hands" of the agent. They allow the playbook to interact with the external world.

1. **OpenAPI Tools:** Connect to standard REST APIs (e.g., getting weather, checking order status).
2. **Client-Side Functions:** Trigger code execution in your own application frontend or backend.
3. **Flow/Playbook Tools:** Transfer the conversation to another specialized playbook or a legacy deterministic flow.

[Reference: Playbook Tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool)

---

## Data Stores (RAG)
**Data Stores** enable Retrieval-Augmented Generation (RAG). By connecting a playbook to a data store containing PDFs, websites, or BigQuery data, the agent can answer questions by searching those documents rather than hallucinating answers.

- **Use Case:** Upload a company's HR policy PDF. The agent can then accurately answer "How many vacation days do I get?" by citing the specific page in the document.

[Reference: Data Stores](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store)

---

# Best Practices for Playbook Design

1. **Modularity:** Build small, focused playbooks for specific tasks (e.g., `Refund_Playbook`) instead of one giant agent.
2. **Grounding:** Always use Data Stores for factual information.
3. **Explicit Constraints:** Tell the agent what **not** to do (e.g., "Do not provide financial advice").
4. **Iterative Testing:** Use the **Reasoning** tab in the Dialogflow CX simulator to see *why* the LLM made a specific decision.
5. **Diverse Examples:** Provide examples for happy paths, errors, and user interruptions.

[Reference: Best Practices](https://docs.cloud.google.com/dialogflow/cx/docs/concept/best-practices)

---

# Simple Mental Model

Think of a **Playbook** as a new employee:
- **The Goal** is their job description.
- **The Instructions** are the training manual they read.
- **The Parameters** are their notepad for taking down details.
- **The Tools** are the software systems they log into to get work done.
- **The Examples** are "shadowing" sessions where they watch an expert handle a call.
- **The Data Store** is the internal Wiki they look at when they don't know an answer.

---

# Summary of Build Workflow
1. **Define the Goal:** What is the agent's purpose?
2. **Write Instructions:** How should the agent achieve that goal?
3. **Configure Tools:** What external systems are needed?
4. **Add Examples:** How should the conversation look?
5. **Test in Simulator:** Review the "Reasoning" to fine-tune the instructions.

[Reference: Quickstart - Build an Agent Playbook](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent-playbook)