# encoding=utf-8
__author__ = 'LoveLYJ'
import numpy as np

class PCA(object):
    def __init__(self, n_components):
        self.n = n_components

    def fit(self, mat):
        new, old = self.__zero_mean(mat)
        cov = np.cov(new, rowvar=0)
        eigVals,eigVects = np.linalg.eig(np.mat(cov))
        eigValIndice = np.argsort(eigVals)                # 对特征值排序
        n_eigValIndice = eigValIndice[-1:-(self.n+1):-1]  # 选择最大的n个特征值
                                                          # python里面，list[a:b:c]代表从下标a开始到b，步长为c
        n_eigVect = eigVects[:,n_eigValIndice]            # 最大的特征值对应的n个向量组成的矩阵
        lowDDataMat = new * n_eigVect                     # 低维特征空间的数据
        return lowDDataMat

    def __zero_mean(self, mat):
        """
        去均值化
        """
        mean = np.mean(mat, axis=0) # axis = 0 求列向量平均值
                                    #      = 1 求行向量平均值
        newMat = mat - mean
        return newMat, mat

if __name__ == "__main__":
    data = np.array([[2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2  , 1  , 1.5, 1.1],
                     [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9]]).T
    pca = PCA(1)
    print pca.fit(data)
