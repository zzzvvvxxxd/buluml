# encoding=utf-8
__author__ = 'LoveLYJ'

import os
import cPickle as pickle
from collections import defaultdict

class CorpusPathError(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return repr("path:\"" + self.path + "\" is invalid")

# 暂时没考虑编码问题，默认英文语料

"""
Corpus类
读取语料，默认单文件，每行一个doc
"""
class Dictionary(object):
    PUNCTUATION = ['(', ')', ':', ';', ',', '-', '!', '.', '?', '/', '"', '*']
    CARRIAGE_RETURNS = ['\n', '\r\n']

    def __init__(self):
        self.word_num = 0
        self._tf = defaultdict(int)                 # global TF dictionary
        self._token2id = defaultdict(int)            # token2id
        #stop words
        self._stopword = None

        # init dictionary

    def is_punc(self, word):
        """
        判断word是否是标点
        :param word: token 单词
        :return:
        """
        for punc in Dictionary.PUNCTUATION + Dictionary.CARRIAGE_RETURNS:
            word = word.replace(punc, '').strip()
        return word if (len(word) > 0) else None

    def tokenize(self, sent):
        # tokenizer
        # sent to word list
        return sent.lower().split()

    def fit(self, docs):
        # 统计TF 词频
        for doc in docs:
            words = self.tokenize(doc)        # 暂时简单实用split
            for word in words:
                clean = self.is_punc(word)
                # clean <= 有意义的词
                if clean : self._tf[clean] += 1
        word_list = self._tf.keys()
        # token -> tid
        for i in range(len(word_list)):
            self._token2id[word_list[i]] = i

    def __getitem__(self, item):
        tokens = None
        if type(item) == str:
            tokens = self.tokenize(item)
        if type(item) == list:
            tokens = item
        doc = dict([(self._token2id[token], self._tf[token]) for token in tokens if self._tf[token] > 0])
        return doc

    def save(self, filename):
        """
        save dictionary
        :param filename: path
        """
        try:
            pickle.dump(self, file(filename, "w"))
        except:
            print "Error"

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


class Corpus(object):
    def __init__(self, path):
        self.doc = list()
        self.path = path
        self.file_list = []
        self.__load_file()

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


if __name__ == "__main__":
    corpus = Corpus("../data/topic/corpus")
    print corpus.file_list