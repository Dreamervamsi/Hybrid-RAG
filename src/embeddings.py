from fastembed import TextEmbedding

def embed_text(chunks:list) -> list:

    model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

    embeddings = list(model.embed(chunks))

    return embeddings