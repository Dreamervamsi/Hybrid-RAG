from src.ingest.ingest_manager import ingest
from src.retrieve.search_manager import search
from src import config
import argparse

def main():
    parser = argparse.ArgumentParser(description='Hybrid RAG CLI tool')
    subparser = parser.add_subparsers(dest='command',required=True)

    ingest_parser = subparser.add_parser("ingest",help="Ingest documents")
    

    ingest_parser.add_argument(
        "--paths",
        type=str,
        nargs='+',
        required=True,
        help="Path to one or more files/directories"
    )
    
    search_parser = subparser.add_parser('search',help="Add search query string")

    search_parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="search query string"
    )
    search_parser.add_argument(
        "--top-k",
        type=int,
        default=3,
        help="For retriving top-k results"   
    )

    args = parser.parse_args()

    if args.command == 'ingest':
        print("Ingesting paths..")
        ingest(args.paths)
    elif args.command == 'search':
        print("Searching query...")
        search(args.query,getattr(args,"top_k",config.TOP_K))

    else:
        print("Enter valid command")


if __name__ == '__main__':
    main()