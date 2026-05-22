import argparse
from .loaders import file_loader
from .chunking import chunk_text

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

    loader_res = file_loader(args.file)

    if loader_res is None:
        return

    chunk_res = chunk_text(loader_res)

    print(chunk_res)

if __name__ == '__main__':
    main()