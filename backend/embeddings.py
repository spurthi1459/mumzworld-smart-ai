import json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_products():
    with open("data/products.json", "r", encoding="utf-8") as f:
        return json.load(f)

def build_embeddings():
    products = load_products()

    texts = [
        f"{p['name']} {p['tags']} {p['description']}"
        for p in products
    ]

    embeddings = model.encode(texts)

    np.save("data/embeddings.npy", embeddings)

    print("Embeddings created!")

if __name__ == "__main__":
    build_embeddings()