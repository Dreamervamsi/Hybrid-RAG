from fastembed import TextEmbedding
from . import config

# if we put this inside a function, model is created on every function call, which increases latency
model = TextEmbedding(model_name=config.EMBED_MODEL)

def dense_embed(chunks:list) -> list:

    text = [chunk['text'] for chunk in chunks]

    embeddings = list(model.embed(text))

    return embeddings

