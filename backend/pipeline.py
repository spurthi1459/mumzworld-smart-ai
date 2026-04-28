from backend.retriever import retrieve
from backend.llm import call_llm
from backend.vision import describe_image


def get_response(query=None, image_bytes=None):

    # Step 1: If image is provided → convert to text
    if image_bytes:
        try:
            query = describe_image(image_bytes)
        except Exception as e:
            print("VISION ERROR:", e)
            query = "baby product"  # fallback

    # Step 2: Retrieve products
    try:
        products = retrieve(query)
    except Exception as e:
        print("RETRIEVER ERROR:", e)
        return {
            "reply": "Something went wrong while fetching products.",
            "products": []
        }

    # Step 3: Handle uncertainty
    if not products:
        return {
            "reply": "I don't have a product for that",
            "products": []
        }

    # Step 4: Generate response (LLM)
    try:
        reply = call_llm(query, products)
    except Exception as e:
        print("LLM ERROR:", e)
        reply = "Here are some recommended products based on your search."

    return {
        "reply": reply,
        "products": products
    }