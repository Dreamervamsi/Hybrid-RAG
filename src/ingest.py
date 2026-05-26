import argparse
from .loaders import file_loader
from .chunking import chunk_text
from .index_dense import vector_store
from .embeddings import dense_embed
from .sparse_index import Tokenize

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

        # dense search
        embeddings = dense_embed(data_chunks)

        collection = vector_store(data_chunks,embeddings,full_reingest=False)

        # sparse search
        token = Tokenize(data_chunks)
        print(token.sparse_search(query="of",top_k=1))

    except FileNotFoundError as e:
        print(e)
        raise SystemExit(1)
    except ValueError as e:
        print(e)
        raise SystemExit(1)


if __name__ == '__main__':
    main()