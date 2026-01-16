#Input Validation
def input_validator(query):
    blocked_terms = ["hack", "illegal", "explosive"]
    return not any(term in query.lower() for term in blocked_terms)
