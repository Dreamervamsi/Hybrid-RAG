from index.sparse_index import Tokenize
from src import config
from index.index_dense import dense_search
from ingest.embeddings import model
from retrieve.rrf_ranking import reciprocal_rank_fusion
from rag.LLM import generate_rag

def search(user_query:str,top_k:int=config.TOP_K):
    try:
        query = user_query
        # sparse search
        tokenizer = Tokenize()
        tokenizer.load_chunks(file_path=config.CHUNK_FILE)
        sparse_results = tokenizer.sparse_search(query,getattr(top_k,'top_k',config.TOP_K))
        
        # dense search
        query_embedding = next(model.embed([query]))
        dense_results = dense_search(query_embedding,top_k)
        
        res = reciprocal_rank_fusion(sparse_results,dense_results)

        generate_rag(query,res)

    except FileNotFoundError as e:
        print(f"File not found error:{e}") 
    except Exception as e:
        # Left open as requested, but added a basic pass/print to avoid compilation crash
        print(f"An error occurred: {e}")
