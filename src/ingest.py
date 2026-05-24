import argparse
from .loaders import file_loader
from .chunking import chunk_text
from .embeddings import embed_text

def main():
    parser=argparse.ArgumentParser(
        description="Ingesting documents through CLI"
    )
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Used for ingesting docs"
    )

    args = parser.parse_args()

    try:
        # retriving text from document
        loader_res = file_loader(args.file)

        # chunking
        data_chunks = chunk_text(loader_res)

        if not data_chunks:
            print("Cant extract the text")
            return {
                'message':'cant extract the text from given document'
            }

        # embeddings
        embeddings = embed_text(data_chunks[0]['text'])
        

    except FileNotFoundError as e:
        print(e)
        raise SystemExit(1)
    except ValueError as e:
        print(e)
        raise SystemExit(1)

if __name__ == '__main__':
    main()