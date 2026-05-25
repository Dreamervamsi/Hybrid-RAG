import chromadb
from .embeddings import embed_text
from . import config

def vector_store(chunks:list,full_reingest:bool=False):
    
    client = chromadb.Client()
    collection = client.get_or_create_collection(name=config.INDEX_DIR,embedding_function=None)

    documents=[]
    ids=[]
    metadatas=[]
    embeddings = []

        
    for chunk in chunks:
        documents.append(chunk['text'])
        ids.append(chunk['chunk_id'])
        metadatas.append(chunk['metadata'])
        embeddings.append(embed_text(chunks['text']))
    
    collection.upsert(
        documents=documents,
        ids=ids,
        metadatas=metadatas,
        embeddings=embeddings
    )

    return collection


