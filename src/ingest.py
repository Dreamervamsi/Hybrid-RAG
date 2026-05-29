import argparse
from src.loaders import file_loader
from src.chunking import chunk_text
from src.index_dense import vector_store
from src.embeddings import dense_embed
from src.sparse_index import Tokenize
from src import config

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
    parser.add_argument(
        "--reingest",
        type=bool,
        help="Used for full reingesting docs.(By default True)"
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

        embeddings = dense_embed(data_chunks)

        collection = vector_store(data_chunks,embeddings,full_reingest=getattr(args,'reingest',True))

        tokenize = Tokenize()
        tokenize.init_chunks(data_chunks)

        tokenize.save_chunks(data_chunks,config.CHUNK_FILE,full_reingest=getattr(args,'reingest',True))

    except FileNotFoundError as e:
        print(e)
        raise SystemExit(1)
    except ValueError as e:
        print(e)
        raise SystemExit(1)


if __name__ == '__main__':
    main()