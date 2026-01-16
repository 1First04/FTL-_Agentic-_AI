##Checker Agent (Validation & Refinement)
def checker_agent(answer, retrieved_docs):
    if "invent" in answer.lower():
        return "Answer rejected due to hallucination."

    if not retrieved_docs:
        return "Answer incomplete: no verified sources."

    # Safety & completeness check
    refined = answer + "\n\nNote: Prices may vary by region and seller."
    return refined

## Orchestration Logic
def agentic_rag_pipeline(query):
    # Step 1: Input Safety
    if not input_validator(query):
        return "Query rejected for safety reasons."

    # Step 2: Retrieve
    docs = retrieve_products(query, products)

    # Step 3: Maker
    draft = maker_agent(query, docs)

    # Step 4: Checker
    final_answer = checker_agent(draft, docs)

    # Step 5: Output Safety
    return output_filter(final_answer)
