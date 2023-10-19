import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score


#przygotowanie danych

X = pd.read_csv("../hm1/X.csv")
y = pd.read_csv("../hm1/y.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state= 335723)

def accuracy(n_splits,X, y, kryt: str):
    if (n_splits <5):
        return "Podaj wartosc wieksza niz 5"
    else:
        if kryt == 'gini'or kryt == 'entropy':
            #kryterium podziału gini lub entropia
            Tree = tree.DecisionTreeClassifier(criterion = kryt)  
            Tree.fit(X_train, y_train)
            kfold = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=None)
            y_pred = Tree.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            return accuracy

entropia = accuracy(8,X_test,y_test,kryt = 'entropy')
gini = accuracy(8,X_test,y_test,kryt = 'gini')
print(entropia,gini )