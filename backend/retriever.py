import numpy as np
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# LOAD MODEL
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

# LOAD DATA
@st.cache_data
def load_data():
    with open("data/products.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    embeddings = np.load("data/embeddings.npy")

    return products, embeddings


# RETRIEVER
def retrieve(query, top_k=3):
    model = load_model()
    products, embeddings = load_data()

    query_lower = query.lower()

    # Step 1: Embedding similarity
    query_emb = model.encode([query])
    sim_scores = cosine_similarity(query_emb, embeddings)[0]

    final_scores = []

    for i, product in enumerate(products):
        score = sim_scores[i]  # base score

        #  Combine text fields
        text = (
            product.get("name", "") + " " +
            product.get("description", "") + " " +
            " ".join(product.get("tags", []))
        ).lower()

        #  Keyword match boost
        for word in query_lower.split():
            if word in text:
                score += 0.2

        #  Tag boost (strong signal)
        for tag in product.get("tags", []):
            if tag in query_lower:
                score += 0.5

        #  Intent rules
        if "cheap" in query_lower or "under" in query_lower:
            if product.get("price_aed", 9999) <= 100:
                score += 0.7

        if "gift" in query_lower and "gift" in product.get("tags", []):
            score += 0.7

        if "toy" in query_lower and "toy" in product.get("tags", []):
            score += 0.7

        if "newborn" in query_lower and "newborn" in product.get("tags", []):
            score += 0.7

        final_scores.append((score, i))

    # Step 2: Sort
    final_scores.sort(reverse=True)

    # Step 3: Diversity (category-wise)
    selected = []
    used_categories = set()

    for score, idx in final_scores:
        product = products[idx]
        category = product.get("category", "unknown")

        if category not in used_categories:
            selected.append(product)
            used_categories.add(category)

        if len(selected) == top_k:
            break

    # Step 4: Uncertainty handling
    if not selected or final_scores[0][0] < 0.3:
        return []

    return selected