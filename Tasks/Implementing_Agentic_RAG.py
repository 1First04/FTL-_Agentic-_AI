products = [
    {
        "name": "Samsung Galaxy A14",
        "price": 220,
        "battery": "5000mAh",
        "safety": "Certified",
        "category": "Android Phone"
    },
    {
        "name": "Xiaomi Redmi Note 12",
        "price": 280,
        "battery": "5000mAh",
        "safety": "Certified",
        "category": "Android Phone"
    }
]

##Retrieval Step
def retrieve_products(query, product_db):
    return [
        p for p in product_db
        if "phone" in query.lower() and p["price"] <= 300
    ]

## Maker Agent (Initial Answer)
def maker_agent(query, retrieved_docs):
    if not retrieved_docs:
        return "No suitable products found based on your query."

    response = "Based on your requirements, here are good options:\n"
    for p in retrieved_docs:
        response += (
            f"- {p['name']} (${p['price']}), "
            f"Battery: {p['battery']}\n"
        )
    return response
