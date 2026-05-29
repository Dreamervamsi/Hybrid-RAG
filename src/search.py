import argparse
from src.sparse_index import Tokenize
from src import config
from src.index_dense import dense_search
from fastembed import TextEmbedding

def main():
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
        results = tokenizer.sparse_search(query,getattr(args,'top_k',3))
        # for idx, match in enumerate(results, start=1):
        #     print(f"\n[Result {idx}]")
        #     print(match.get('text', 'No text field found'))
        
        # dense search
        model = TextEmbedding(model_name=config.EMBED_MODEL)
        query_embedding = next(model.embed([query]))
        dense_results = dense_search(query_embedding,getattr(args,"top_k",3))
        print(dense_results)
    except FileNotFoundError as e:
        print(f"File not found error:{e}") 
    except Exception as e:
        # Left open as requested, but added a basic pass/print to avoid compilation crash
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()