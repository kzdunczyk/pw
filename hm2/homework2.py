from sklearn.datasets import fetch_openml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

df = fetch_openml(data_id = 31)
df = pd.get_dummies(df)
y = df.target
X = df.data

# zbiór testowy i treningowy 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#model regresji logistycznej
model_lr = LogisticRegression(penalty = 'None' ) 


#model regresji logistycznej z regularyzacją L1
model_l1 = LogisticRegression(penalty='l1', solver = 'liblinear') 
param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100]
}

# Utwórz obiekt GridSearchCV
grid_search = GridSearchCV(model_l1, param_grid, cv=5, scoring='accuracy')

# Dopasuj model do danych treningowych
grid_search.fit(X_train, y_train)

# Wydrukuj najlepsze parametry
print("Najlepsze parametry:", grid_search.best_params_)

#model regresji logistycznej z regularyzacją L2
model_l2 = LogisticRegression(solver='liblinear', penalty='l2', C=1) 