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

##Naive Bayes

```python
from buluml.Corpus import Dictionary
from buluml.naive_bayes import BasicNB
```

训练：
```python
x = []
y = []
# 获取语料
with open("./data/spam_email/spam_train.txt") as f:
    for line in f:
        x.append(line[2:])
        y.append(int(line[0]))
# Dictionary
dictionary = Dictionary("../../data/stopwords.txt")
dictionary.fit(x)
# dictionary = Dictionary.load('nb.dict')
# doc2id
x = [dictionary[text] for text in x]
# NB
nb = BasicNB()
nb.fit(x, y)
```

测试
```python
# test
y_t = []
x_t = []
with open("./data/spam_email/spam_test.txt") as f:
    for line in f:
        x_t.append(line[2:])
        y_t.append(int(line[0]))
# doc2id
x_t = [dictionary[text] for text in x_t]
nb.predict(x_t, y_t)
```

效果：
> **0.969** on test corpus

 
性能（训练语料/data/spam_email/spam_train.txt）：

> 加载字典： 14.3309998512 s   
  训练： 0.146000146866 s   

 效果还不错

 ----
 
##Logistic 

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
