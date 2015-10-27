# encoding=utf-8
__author__ = 'LoveLYJ'

from  buluml.Corpus import Dictionary, Corpus

class BasicNB(object):

    def __int__(self):
        pass

if __name__ == '__main__':
    texts = []
    tags = []
    s = None
    with open("../../data/spam_email/spam_train.txt") as f:
        for line in f:
            tag = line[0]
            s = line[2:]
            sent = line[2:]
            texts.append(sent)
            tags.append(tag)
    dictionary = Dictionary()
    dictionary.fit(texts)
    print dictionary[s]