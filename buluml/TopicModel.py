# encoding=utf-8
__author__ = 'LoveLYJ'
from Corpus import Corpus, Dictionary
from buluError import TypeError, CorpusPathError
import numpy as np

class pLSA():
    def __init__(self, corpus, number_of_topic):
        if not isinstance(corpus, Corpus):
            raise TypeError("corpus", Corpus)
        self.num_topic = number_of_topic
        self.num_docs = corpus.getDocNum()
        self.num_word = corpus.getWordNum()
        self.pz_w = self._rand_mat(self.num_topic, self.num_word)
        print self.pz_w

    def fit(self):
        """
        训练pLSA
        [
            [token1, token2],
            [token1, token2, token3, token4]
        ]
        :return:
        """
        pass

    def transform(self):
        # no use
        pass

    def _rand_mat(self, sizex, sizey):
        mat = np.random.rand(sizex, sizey)
        for r in range(sizex):
            s = np.sum(mat[r])
            for c in range(sizey):
                mat[r][c] = mat[r][c] / s
        return mat

if __name__ == "__main__":
    corpus = Corpus("../data/topic/corpus")
    plsa = pLSA(corpus, 5)