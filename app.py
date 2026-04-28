import streamlit as st
from backend.pipeline import get_response
import os
from PIL import Image

st.set_page_config(page_title="AI Gift Finder", layout="wide")

st.title("🛍️ AI Gift Finder for Moms")


# -------- IMAGE FIX FUNCTION --------
def show_images(image_list):
    cols = st.columns(len(image_list))

    for i, img in enumerate(image_list):
        try:
            img_path = os.path.join(os.getcwd(), img)

            if os.path.exists(img_path):
                image = Image.open(img_path)

                # ✅ FORCE SAME SIZE (clean UI)
                image = image.resize((180, 180))

                cols[i].image(image)
            else:
                cols[i].write("❌ Missing")

        except:
            cols[i].write("❌ Error")


# Tabs
tab1, tab2 = st.tabs(["Text Search", "Image Search"])


# ---------------- TEXT SEARCH ----------------
with tab1:
    query = st.text_input("Ask for a product...")

    if query:
        result = get_response(query=query)

        st.subheader("🤖 AI Recommendation")
        st.write(result["reply"])

        st.subheader("🛒 Suggested Products")

        for p in result["products"]:
            col1, col2 = st.columns([1, 2])

            with col1:
                show_images(p["images"])

            with col2:
                st.write(f"### {p['name']}")
                st.write(f"💰 {p['price_aed']} AED")
                st.write(p["description"])


# ---------------- IMAGE SEARCH ----------------
with tab2:
    uploaded_file = st.file_uploader("Upload product image", type=["jpg", "png"])

    if uploaded_file:
        image_bytes = uploaded_file.read()

        result = get_response(image_bytes=image_bytes)

        st.subheader("🤖 AI Recommendation")
        st.write(result["reply"])

        st.subheader("🛒 Suggested Products")

        for p in result["products"]:
            col1, col2 = st.columns([1, 2])

            with col1:
                show_images(p["images"])

            with col2:
                st.write(f"### {p['name']}")
                st.write(f"💰 {p['price_aed']} AED")
                st.write(p["description"])