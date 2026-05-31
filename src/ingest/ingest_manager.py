from ingest.loaders import file_loader
from ingest.chunking import chunk_text
from index.index_dense import vector_store
from ingest.embeddings import dense_embed
from index.sparse_index import Tokenize
from src import config

def ingest(file_paths:list,reingest:bool=True):
    try:
        print("File loading.Extracting text..")
        # retriving text from document
        loader_res = file_loader(file_paths)
        print("Chunking the file..")
        # chunking
        data_chunks = chunk_text(loader_res)

        if not data_chunks:
            print("Cant extract the text")
            return {
                'message':'cant extract the text from given document'
            }

        print("Embedding the file chunks....")
        embeddings = dense_embed(data_chunks)

        collection = vector_store(data_chunks,embeddings,full_reingest=reingest)

        tokenize = Tokenize()
        tokenize.init_chunks(data_chunks)

        print("Saving chunks..")
        tokenize.save_chunks(data_chunks,config.CHUNK_FILE,full_reingest=reingest)

        print("Ingestion successful!, Full reingestion applied: ",reingest)

    except FileNotFoundError as e:
        print(e)
        raise SystemExit(1)
    except ValueError as e:
        print(e)
        raise SystemExit(1)
