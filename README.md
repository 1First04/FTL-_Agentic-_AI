## Assignmet 3: Agentic RAG with Safety Measures

#Architecture Overview – AI Shopping Assistant

The AI Shopping Assistant is designed as a safe, agentic Retrieval-Augmented Generation (RAG) system that combines external product knowledge with multi-agent reasoning and safety enforcement.

🔹 High-Level Architecture
┌──────────────────┐
│   User Interface │
│ (Text Query)     │
└────────┬─────────┘
         │
         ▼
┌────────────────────────┐
│ Input Safety Validator │
│ - Malicious detection  │
│ - Query sanitization   │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────────┐
│ Meta System Prompt Layer   │
│ - Agent role & constraints │
│ - Safety rules             │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Retrieval Module (RAG)     │
│ - Product Knowledge Base   │
│ - Vector / keyword search  │
│ - Read-only access         │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Maker Agent                │
│ - Generates initial answer │
│ - Uses retrieved context   │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Checker Agent              │
│ - Verifies correctness     │
│ - Detects hallucinations   │
│ - Enforces safety rules    │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Output Safety Filter       │
│ - Removes unsafe claims    │
│ - Adds disclaimers         │
└────────┬───────────────────┘
         │
         ▼
┌──────────────────┐
│ Final Response   │
│ (Safe & Reliable)│
└──────────────────┘

🔹 Component Responsibilities
1️⃣ User Interface

Accepts natural-language shopping queries

No direct access to internal tools or databases

2️⃣ Input Safety Validator

Blocks malicious or malformed queries

Prevents unsafe tool invocation

Enforces allowed-domain usage (shopping only)

3️⃣ Meta System Prompt Layer

Defines agent identity and behavior

Sets strict constraints against hallucination

Ensures the assistant remains an advisor, not a decision-maker

4️⃣ Retrieval Module (RAG Core)

Retrieves relevant product data from:

Structured product database

(Optional) Vector embeddings

Guarantees grounded generation

Operates in read-only mode
