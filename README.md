# MumzWorld AI – Smart Baby Product Recommender

An AI-powered product recommendation system that helps moms find the right baby products using **text queries or images**.

Built using **RAG (Retrieval-Augmented Generation)** with semantic search and optional LLM enhancement.

---
## 🎥 Demo Video

Watch the 3-minute walkthrough here:

👉 https://www.loom.com/share/1eec033668454096bf3d6f8cdbb63b0f

##  Features

-  **Text Search**
  - Ask natural queries like *“gift for newborn”* or *“cheap baby toy”*

-  **Image Search**
  - Upload an image → get similar product recommendations

-  **Hybrid Retrieval System**
  - Semantic embeddings (Sentence Transformers)
  - Tag-based filtering
  - Diversity-aware results (no repeated categories)

-  **LLM Integration (Gemini)**
  - Generates human-like responses
  - Includes fallback if API fails or quota exceeds

-  **Robust System Design**
  - Works even without LLM
  - Handles unknown queries safely

- **Multilingual Support (English & Arabic)**
  - Displays product names and descriptions in both English and Arabic
  - Enhances accessibility for a broader user base
  - Leverages multilingual product metadata without requiring translation APIs
- 

---

##  Architecture

```

User Input (Text / Image)
↓
Image → Vision Model → Query
↓
Retriever (Embeddings + Rules)
↓
Top K Products
↓
LLM (Optional Enhancement)
↓
Final Response + UI Display

```

---

### Tools Used

- **Sentence Transformers (all-MiniLM-L6-v2)**  
  Used for generating semantic embeddings for both queries and products.

- **Scikit-learn (cosine similarity)**  
  Used to compute similarity scores between query and product embeddings.

- **Streamlit**  
  Used to quickly build an interactive UI for both text and image-based search.

- **Gemini API (optional LLM layer)**  
  Used to generate natural language recommendations. The system includes fallback logic to remain functional without it.

- **NumPy**  
  Used for efficient embedding storage and vector operations.

---

### Workflow

1. **Data Preparation**  
   Created a structured dataset with product metadata, tags, and multilingual fields.

2. **Embedding Generation**  
   Precomputed product embeddings using Sentence Transformers and stored them for fast retrieval.

3. **Query Processing**  
   - Text input is directly encoded  
   - Image input is converted into a semantic query  

4. **Retrieval Layer**  
   Combined semantic similarity with rule-based scoring (tags, price, intent).

5. **Response Generation**  
   Used an optional LLM to generate user-friendly responses with fallback handling.

6. **Evaluation**  
   Built a custom evaluation pipeline to measure retrieval quality using keyword-based scoring.

---

### Design Philosophy

- Prefer **robust systems over API dependency**
- Combine **semantic + rule-based retrieval** for better accuracy
- Ensure **graceful degradation** when LLM fails

##  Project Structure

```

mumzworld-ai/
│
├── backend/
│   ├── retriever.py
│   ├── pipeline.py
│   ├── llm.py
│   ├── vision.py
│   └── prompts.py
│
├── data/
│   ├── products.json
│   └── embeddings.npy
│
├── images/               # Local product images
│
├── evals/
│   ├── run_evals.py
│   └── test_cases.py
│
├── app.py                # Streamlit UI
├── requirements.txt
└── README.md

````

---

##  Evaluation

We evaluated the system using 10 diverse test queries.

| Metric | Value |
|------|------|
| PASS | 3 |
| PARTIAL | 4 |
| LOW | 3 |
| **Average Score** | **0.55** |

###  Observations

-  Strong performance on clear intent queries  
  *(e.g., "stroller for travel", "feeding bottle")*

-  Partial matches due to limited dataset tags  
  *(missing tags like "gift", "affordable")*

-  System remains stable even when LLM fails  

---

##  Key Design Decisions

- Used **hybrid retrieval (semantic + rules)** instead of pure embeddings  
- Added **fallback logic** for LLM failures (quota / API issues)  
- Implemented **category diversity filtering**  
- Decoupled **retrieval and generation** for robustness  

---

##  Limitations

- Limited dataset size  
- Missing tags affect accuracy  
- LLM dependent on API quota  

---

##  Future Improvements

- Add richer product tags (gift, budget, premium, etc.)
- Implement price-aware ranking
- Improve intent classification
- Replace deprecated Gemini SDK (`google.generativeai → google.genai`)

---

##  Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
````

---

##  Run Evaluation

```bash
python -m evals.run_evals
```

---

##  Environment Variables
```
GEMINI_API_KEY=your_api_key_here
```

##  Example Queries

* gift for newborn
* cheap baby toy
* stroller for travel
* baby skincare product
* feeding bottle for infant

---

##  Tech Stack

* Python
* Streamlit
* Sentence Transformers
* Scikit-learn
* Gemini API (LLM)
* NumPy

---

##  Author

Spurthi Pattanashetti


---

### Text Search
<img width="1820" height="818" alt="text search" src="https://github.com/user-attachments/assets/e5b89d3b-bee5-42cf-bf25-1f0b16403087" />

### Image Search
<img width="1875" height="837" alt="input image" src="https://github.com/user-attachments/assets/4deaa41f-dd25-45d6-b589-cf06da29b653" />

```

---

