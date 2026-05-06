# University Knowledge Assistant (Generative + Data Store)

## Objective
Build a conversational agent that helps students navigate university information using a **Generative Playbook + Cloud Storage Data Store**.

---

## Scenario: University Help Desk Bot

Your agent will act as a **University Student Support Assistant** that answers questions about:

- Courses and departments
- Professors
- Campus services

---

## Requirements

You must:

1. Create a Generative Playbook
2. Connect a Cloud Storage Data Store
3. Ensure responses are grounded in stored documents
4. Provide fallback answers when data is missing
5. Format responses clearly and concisely

---

## Step-by-Step Instructions

### 1. Create Data Store
- Create a Cloud Storage bucket
- Upload the provided dataset files (check the resources folder)
- Connect bucket to your agent as a Data Store

---

### 2. Create Generative Playbook

Name:
> **University_Assistant_Playbook**

### Behavior:
- Always search Data Store first
- Summarize relevant results
- If multiple matches exist, group by category (courses, services, etc.)
- If nothing is found:
  > "I couldn’t find that information in the university knowledge base. Please try rephrasing your question."

---

## Example Capabilities

Your agent should be able to:

- List departments and courses
- Provide professor information
- Describe campus services

---

## Example Questions

- What computer science courses are available?
- Who teaches Data Structures?
- What tutoring services are available?
- Which departments offer AI-related courses?

---

## Evaluation Criteria

- Accurate retrieval from Data Store
- Clean structured responses
- Proper fallback handling
- Good summarization of multiple results