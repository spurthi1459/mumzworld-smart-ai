from backend.retriever import retrieve
from backend.llm import call_llm
from backend.vision import describe_image


def get_response(query=None, image_bytes=None):

    # Step 1: Convert image → query
    if image_bytes:
        query = describe_image(image_bytes)

    # Safety check
    if not query:
        return {
            "reply": "Please provide a valid query",
            "products": []
        }

    # Step 2: Retrieve products
    products = retrieve(query)

    # Step 3: Handle no results
    if not products:
        return {
            "reply": "I couldn't find relevant products for this query.",
            "products": []
        }

    # Step 4: Generate response (LLM optional)
    try:
        reply = call_llm(query, products)
    except Exception:
        # fallback if LLM fails
        reply = f"Here are some recommended products for: {query}"

    return {
        "reply": reply,
        "products": products
    }