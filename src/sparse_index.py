import bm25s
from rank_bm25 import BM25Okapi


def tokenize(chunks:list):
    tokens=[]
    a=[]
    for i in range(len(chunks)):
        token = chunks[i]['text'].lower().split()
        tokens.append(token)
    print(tokens)

    return tokens