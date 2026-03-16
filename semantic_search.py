from src.vectordb.chroma_store import collection
from src.embeddings.embedding_model import model


def search(job_description, top_k):

    embedding = model.encode(job_description).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results
