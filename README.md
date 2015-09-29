# buluML
bulu Dog's Machine Learning Toolkit [Python]

# 更新
v0.0.1
* Logistic Regression简单demo更新

#  安装

> pip install buluml

or 下载源码

> python setup.py install

# Demo

###Logistic 

```
from buluml.LogisticRegression import LogisticRegression
```

训练：
```python
# load data
data = loadtxt('../data/train.txt')
x = data[:, :-1]
y = data[:, -1]

# fit
model = LogisticRegression()
model.fit(x, y)
```

测试：
```python
test = loadtxt('../data/test.txt')
x_t = test[:, :-1]
y_t = test[:, -1]
model.predict(x_t, y_t)
print model.accu
```
