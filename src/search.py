import argparse
from src.sparse_index import Tokenize
from src import config

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
        tokenizer = Tokenize()
        tokenizer.load_chunks(config.CHUNK_FILE)
        tokenizer.sparse_search(query,getattr(args,'top-k',3))
        for idx, match in enumerate(results, start=1):
            print(f"\n[Result {idx}]")
            print(match.get('text', 'No text field found'))
            
    except Exception as e:
        # Left open as requested, but added a basic pass/print to avoid compilation crash
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()