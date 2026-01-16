## Assignmet 3: Agentic RAG with Safety Measures

### Architecture Overview – AI Shopping Assistant

### Project Overview

This project implements an Agentic Retrieval-Augmented Generation (RAG) system for an AI Shopping Assistant.
The system answers complex shopping queries using an external product knowledge base, while ensuring safety, correctness, and reliability through a Maker–Checker agent loop and layered safety controls.

### Objectives

Retrieve relevant product information from an external knowledge base

Generate grounded and explainable shopping recommendations

Prevent hallucinations and unsafe outputs

Enforce safety through input validation and output sanitization

Demonstrate agentic reasoning using a Maker–Checker loop

### == Architecture Overview ==

The AI Shopping Assistant follows a multi-layered agentic architecture designed for safety and reliability.

User Query
   │
   ▼
Input Safety Validator
   │
   ▼
Meta System Prompt Layer
   │
   ▼
Retrieval Module (RAG)
   │
   ▼
Maker Agent
   │
   ▼
Checker Agent
   │
   ▼
Output Safety Filter
   │
   ▼
Final Response

### Component Responsibilities
1️⃣ User Interface

Accepts natural-language shopping queries

No direct access to internal tools or databases

2️⃣ Input Safety Validator

Detects malicious or malformed queries

Blocks unsafe or out-of-scope requests

Prevents unsafe tool usage

3️⃣ Meta System Prompt Layer

Defines agent role, goals, and constraints

Enforces grounding and non-hallucination

Restricts advice to safe shopping recommendations

4️⃣ Retrieval Module (RAG Core)

Retrieves relevant product data from:

Structured product database

(Optional) vector-based similarity search

Operates in read-only mode

Provides grounding context for generation

5️⃣ Maker Agent

Generates the initial response

Uses only retrieved product information

Explains reasoning and trade-offs clearly

6️⃣ Checker Agent

Reviews the Maker’s output for:

Factual correctness

Completeness

Safety compliance

Refines or rejects unsafe or unverified responses

7️⃣ Output Safety Filter

Sanitizes exaggerated or misleading claims

Adds disclaimers where uncertainty exists

Ensures safe and responsible final output

🔁 Agentic Workflow (Maker–Checker Loop)

User submits a query

Query is validated for safety

Relevant products are retrieved

Maker Agent generates an initial answer

Checker Agent verifies and refines the answer

Output is sanitized and returned to the user

### Safety Mechanisms

Input validation for malicious queries

Read-only retrieval tools

Hallucination prevention via Checker Agent

Output sanitization and disclaimers

### Example Query
Find a safe Android phone under $300 with good battery life.

Example Output
Here are suitable options based on your needs:
- Samsung Galaxy A14 ($220), Battery: 5000mAh
- Xiaomi Redmi Note 12 ($280), Battery: 5000mAh

Note: Prices may vary by seller and location.

### Deliverables

✔ Source code (Python / Colab notebook)

✔ Agentic RAG implementation

✔ Meta system prompt

✔ Maker–Checker loop

✔ Safety mechanisms

✔ Architecture documentation

✔ Example queries and outputs

### Future Extensions

LangChain / LangGraph orchestration

Vector database integration (FAISS, Chroma)

Real e-commerce API integration

User preference memory

Automated evaluation metrics

## Final Summary

This AI Shopping Assistant demonstrates a safe, agentic RAG architecture that combines retrieval-grounded reasoning, multi-agent validation, and layered safety controls to deliver trustworthy and explainable shopping recommendations.
