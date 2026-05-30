import argparse
from src.sparse_index import Tokenize
from src import config
from src.index_dense import dense_search
from src.embeddings import model
from src.rrf_ranking import reciprocal_rank_fusion

def search():
    parser = argparse.ArgumentParser(
        description="quering the files"
    )

    parser.add_argument(
        '-q',
        type=str,
        required=True,
        help="Used for providing query"
    )

    parser.add_argument(
        '--top-k',
        type = int,
        help="Used for retriving top-k results (default k=3)"
    )

    args = parser.parse_args()

    try:
        query = args.q
        # sparse search
        tokenizer = Tokenize()
        tokenizer.load_chunks(file_path=config.CHUNK_FILE)
        sparse_results = tokenizer.sparse_search(query,getattr(args,'top_k',config.TOP_K))
        # for idx, match in enumerate(sparse_results, start=1):
        #     print(f"\n[Result {idx}]")
        #     print(match.get('text', 'No text field found'))
        
        # dense search
        query_embedding = next(model.embed([query]))
        dense_results = dense_search(query_embedding,getattr(args,"top_k",3))
        
        res = reciprocal_rank_fusion(sparse_results,dense_results)

        print(res)

    except FileNotFoundError as e:
        print(f"File not found error:{e}") 
    except Exception as e:
        # Left open as requested, but added a basic pass/print to avoid compilation crash
        print(f"An error occurred: {e}")
