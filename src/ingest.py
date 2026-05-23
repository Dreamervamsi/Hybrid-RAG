import argparse
from .loaders import file_loader
from .chunking import chunk_text
import chunking

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
        loader_res = file_loader(args.file)

        content_chunks = chunking(loader_res)

        if not content_chunks:
            print("Cant extract the text")
            return
            
        print(content_chunks)
    except FileNotFoundError as e:
        print(e)
        raise SystemExit(1)
    except ValueError as e:
        print(e)
        raise SystemExit(1)

if __name__ == '__main__':
    main()