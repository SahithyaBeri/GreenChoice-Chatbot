from embeddings.vector_store import search_query

def generate_response(user_query):

    question, answer, score = search_query(user_query)

    response = f"""
Eco Assistant Response:

Related Question: {question}

Advice:
{answer}
"""

    return response