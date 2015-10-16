# encoding=utf-8
__author__ = 'LoveLYJ'

import os
import StringIO
import cPickle as pickle
from collections import defaultdict
from buluError import CorpusPathError

# 暂时没考虑编码问题，默认英文语料

class Dictionary(object):
    PUNCTUATION = ['(', ')', ':', ';', ',', '-', '!', '.', '?', '/', '"', '*']
    CARRIAGE_RETURNS = ['\n', '\r\n']

    def __init__(self):
        self.word_num = 0
        self._tf = defaultdict(int)                  # global TF dictionary
        self._token2id = defaultdict(int)            # token2id
        #stop words
        self._stopword = set()
        # load stopwords
        with open("../data/stopwords.txt") as f:
            for word in f:
                self._stopword.add(word.strip())
        # init dictionary

    def __filter(self, word):
        """
        判断word是否是标点
        :param word: token 单词
        :return:
        """
        for punc in Dictionary.PUNCTUATION + Dictionary.CARRIAGE_RETURNS:
            word = word.replace(punc, '').strip()
        return word if (len(word) > 0) and word not in self._stopword else None

    @classmethod
    def tokenize(self, sent):
        # tokenizer
        # sent to word list
        return sent.lower().split()

    def fit(self, docs):
        # 统计TF 词频
        for doc in docs:
            words = self.tokenize(doc)        # 暂时简单实用split
            for word in words:
                clean = self.__filter(word)
                # clean <= 有意义的词
                if clean : self._tf[clean] += 1
        word_list = self._tf.keys()
        self.word_num = len(word_list)
        # token -> tid
        for i in range(self.word_num):
            self._token2id[word_list[i]] = i

    def __getitem__(self, item):
        tokens = None
        if type(item) == str:
            tokens = self.tokenize(item)
        if type(item) == list:
            tokens = item
        doc = dict([(self._token2id[token], self._tf[token]) for token in tokens if self._tf[token] > 0])
        return doc

    @classmethod
    def load(clj, filename):
        """
        load Dictionary info from disk
        :param clj:
        :param filename: 导入的pickle文件
        :return:
        """
        info = pickle.load(file(filename))
        return info

    def save(self, filename):
        """
        save dictionary
        :param filename: path
        """
        try:
            pickle.dump(self, file(filename, "w"))
        except:
            print "Error"
"""
Corpus类
读取语料
单文件，每行一个doc
多文件，传入文件所在文件夹（单文件夹），每个文件一个doc
"""
class Corpus(object):
    def __init__(self, path):
        self.docs = list()
        self.corpus = list()
        self.path = path
        self.file_list = []
        self.dictionary = Dictionary()
        self.__load_file()
        self.__load()
        self.__doc2id()

    def load(self):
        pass

    def __load_file(self):
        if os.path.isfile(self.path) and os.path.exists(self.path):
            # single file
            self.file_list.append(self.path)
        elif os.path.isdir(self.path) and os.path.exists(self.path):
            # directory
            for filename in os.listdir(self.path):
                self.file_list.append(os.path.join(self.path, filename))
        else:
            raise CorpusPathError(self.path)
        return

    def __load(self):
        if len(self.file_list) > 1:
            # 多个文件，默认每个文件是一个doc
            for filename in self.file_list:
                with open(filename) as f:
                    doc = StringIO.StringIO()
                    for line in f:
                        if len(line) > 0:
                            doc.write(line.strip() + " ")
                    self.docs.append(doc.getvalue())
            self.dictionary.fit(self.docs)

    def __doc2id(self):
        for doc in self.docs:
            self.corpus.append(self.dictionary[doc])

    def getDict(self):
        return self.dictionary

    def getWordNum(self):
        return self.dictionary.word_num

    def getCorpus(self):
        return self.corpus

    def getDocNum(self):
        return len(self.corpus)

if __name__ == "__main__":
    corpus = Corpus("../data/topic/corpus")
    print corpus.getCorpus()