# encoding=utf-8
__author__ = 'LoveLYJ'

import numpy as np
from buluml.Corpus import Dictionary, Corpus

class BasicNB(object):

    def __int__(self):
        self.p_w_s = 0
        self.p_s = 0
        self.p_h = 0
        self.p_w_h = 0

    def fit(self, x, y):
        # 默认输入的y的值域是0，1
        y = np.array(y, dtype=bool)
        # x: 特征
        # y: tag [0, 1]
        fn = len(x[0])          # 特征维度
        n = len(x)              # 样本个数
        n1 = np.sum(y)          # 负样本个数
        n0 = n - n1
        # 计算两个类别的概率
        self.p_s = (n1 + 1) / float(n + 2)
        self.p_h = 1 - self.p_s
        # p_w_s
        self.p_w_s = np.ones_like(x[0])
        self.p_w_h = np.ones_like(x[0])
        for i in range(len(y)):
            if y[i]:
                self.p_w_s += x[i]
            else:
                self.p_w_h += x[i]
        self.p_w_s = np.log((self.p_w_s) / (n1 + 1))
        self.p_w_h = np.log((self.p_w_h) / (n0 + 1))

    def predict(self, x, y):
        r = []
        z = np.zeros_like(x[0])
        for item in x:
            prob_s = np.sum(np.where(item, self.p_w_s, z)) + np.log(self.p_s)
            prob_h = np.sum(np.where(item, self.p_w_h, z)) + np.log(self.p_h)
            r.append((prob_s - prob_h) > 0 and 1 or  0)
        return r

import time
if __name__ == '__main__':
    s = time.time()
    texts = []
    tags = []
    # 获取语料
    with open("../../data/spam_email/spam_train.txt") as f:
        for line in f:
            texts.append(line[2:])
            tags.append(int(line[0]))
    # Dictionary
    dictionary = Dictionary("../../data/stopwords.txt")
    dictionary.fit(texts)
    # dictionary = Dictionary.load('nb.dict')
    # doc2id
    texts = [dictionary[text] for text in texts]
    e = time.time()
    print e - s
    # NB
    nb = BasicNB()
    nb.fit(texts, tags)
    print e - time.time()
    # test
    tags_t = []
    texts_t = []
    with open("../../data/spam_email/spam_test.txt") as f:
        for line in f:
            texts_t.append(line[2:])
            tags_t.append(int(line[0]))
    # doc2id
    texts_t = [dictionary[text] for text in texts_t]
    nb.predict(texts_t, tags_t)
