
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#przygotowanie danych

X = pd.read_csv("C:/Users/Kajetan/Desktop/pw/hm1/X.csv")
y = pd.read_csv("C:/Users/Kajetan/Desktop/pw/hm1/y.csv")

def accuracy(cv:int,X, y, wart = 0):
    if(cv <5):
        return "Podaj wartosc wieksza niz 5"
    else:
        wyniki1 = 0
        wyniki2 = 0
        wyniki3 = []
        wyniki4 = []
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state= 335723)
        Tree = tree.DecisionTreeClassifier(criterion = 'gini',
                                               random_state = 335723 )  
        scores = cross_val_score(Tree, X_train, y_train, cv = cv)
        wyniki1 = scores.mean()
        Tree = tree.DecisionTreeClassifier(criterion = 'entropy',
                                               random_state = 335723 )  
        scores = cross_val_score(Tree, X_train, y_train, cv = cv)
        wyniki2 = scores.mean()
        for i in range(1,wart + 1):
            Tree = tree.DecisionTreeClassifier(max_depth = i,
                                               random_state =335723 )  
            scores = cross_val_score(Tree, X_train, y_train, cv = cv)
            wyniki3.append(scores.mean())
            Tree = tree.DecisionTreeClassifier(min_samples_leaf = i,
                                               random_state=335723 )  
            scores = cross_val_score(Tree, X_train, y_train, cv = cv)
            wyniki4.append(scores.mean())
        plt.plot(wart,)
        return(" Dokładność na podstawie kryt. giniego to:",wyniki1,
               "\n Dokładność na podstawie kryt. etropii to:", wyniki2, 
               "\n Dokładność na podstawie głebokości drzewa to:", wyniki3,
               "\n Dokładność na podstawie min liczby obserwacji w lisciu to:"
               , wyniki4,
              )
    
    wyniki  = accuracy(8,X,y, 10 )
print(wyniki)