
# coding: utf-8

# In[149]:


import pandas as pd
import numpy as np
import ast
from sklearn.model_selection import train_test_split

#Data preparation and loading
#X = pd.read_csv("foo1.csv")
#Y = pd.read_csv("foo2.csv")

#result = pd.concat([X,Y], axis=1)
#result.to_csv('sample.csv')
sample=pd.read_csv("sample.csv")

#dfs = np.split(sample, [30], axis=1)
#dfs[1].astype(int)

#train and test split in the ratio 85:15
train, test = train_test_split(sample, test_size=0.15)
df = np.split(train, [30], axis=1)
dff = np.split(test, [30], axis=1)

from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)

#X1 = dfs[0]
#Y1 = dfs[1].astype(int)

X1=df[0]
Y1=df[1].astype(int)

# create model
model = Sequential()
model.add(Dense(40, input_dim=30, activation='sigmoid'))
model.add(Dense(30, activation='sigmoid'))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X1, Y1, epochs=150)
# evaluate the model
scores = model.evaluate(X1, Y1)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

model.evaluate(dff[0], y = dff[1].astype(int), verbose=1)

