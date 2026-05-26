from rank_bm25 import BM25Okapi

class Tokenize:
    def __init__(self,chunks:list):
        if not chunks:
            raise ValueError('Text chunks not provided')

        self.org_chunks = chunks

        self.corpus=[chunks[i]['text'].lower().split() for i in range(len(self.org_chunks))]
    
        self.tokenize_corpus = BM25Okapi(self.corpus)

    def sparse_search(self,query:str,top_k):
    
        tokenized_query = query.lower().split()

        # scores = self.tokenize_corpus.get_scores(tokenized_query)

        res = self.tokenize_corpus.get_top_n(tokenized_query,self.org_chunks,n=top_k)

        return res
