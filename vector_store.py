import chromadb
from config import VECTOR_DB_NAME

client = chromadb.Client()

collection = client.get_or_create_collection(
    name=VECTOR_DB_NAME
)


def store_embeddings(chunks, embeddings, metadata, file_name):

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i].tolist()],
            metadatas=[{
                "skills": ",".join(metadata["skills"]),
                "experience": metadata["experience"],
                "file": file_name
            }],
            ids=[f"{file_name}_{i}"]
        )
