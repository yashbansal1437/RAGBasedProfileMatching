import os

from src.config import RESUME_FOLDER
from src.loaders.resume_loader import load_resume
from src.processing.chunker import chunk_document
from src.processing.metadata_extractor import extract_metadata
from src.embeddings.embedding_model import generate_embeddings
from src.vectordb.chroma_store import store_embeddings


def build_resume_rag():

    for file in os.listdir(RESUME_FOLDER):

        path = os.path.join(RESUME_FOLDER, file)

        text = load_resume(path)

        chunks = chunk_document(text)

        metadata = extract_metadata(text)

        embeddings = generate_embeddings(chunks)

        store_embeddings(chunks, embeddings, metadata, file)
