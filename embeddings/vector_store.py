import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

data = pd.read_csv("data/sustainability_knowledge.csv")

questions = data["question"].tolist()
answers = data["answer"].tolist()

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(questions)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

print("Vector database ready")

def search_query(query):

    query_vector = model.encode([query])

    distances, indices = index.search(query_vector, 1)

    idx = indices[0][0]

    return questions[idx], answers[idx], distances[0][0]