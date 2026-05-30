from src.ingest import ingest
import argparse

def main():
    parser = argparse.ArgumentParser(description='Hybrid RAG CLI tool')
    subparser = parser.add_subparsers(dest='command',required=True)

    ingest_parser = subparser.add_parser("ingest","Ingest documents")
    

    ingest_parser.add_argument(
        "--paths",
        type=str,
        nargs='+',
        required=True,
        help="Path to one or more files/directories"
    )


if __name__ == '__main__':
    main()