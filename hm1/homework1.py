import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score,KFold, GridSearchCV
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score, roc_curve,roc_auc_score, auc, accuracy_score, recall_score, precision_score, f1_score, RocCurveDisplay

X = pd.read_csv("../pw/hm1/X.csv")
y = pd.read_csv("../pw/hm1/y.csv")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state= 335723)
def accuracy(cv:int,X, y, wart = 0):
    if(cv <5):
        return "Podaj wartosc wieksza niz 5"
    else:
        wyniki_train = []
        wyniki_test = []
        
        Tree = tree.DecisionTreeClassifier(criterion = 'gini',
                                               random_state = 335723 ) 
        kf = KFold(n_splits = cv, random_state =335723, shuffle = True )
        scores = cross_val_score(Tree, X_train, y_train, cv = kf)
        wyniki_train.append(scores.mean())
        scores = cross_val_score(Tree, X_test, y_test, cv = kf)
        wyniki_test.append(scores.mean())
        
        Tree = tree.DecisionTreeClassifier(criterion = 'entropy',
                                               random_state = 335723 )  
        scores = cross_val_score(Tree, X_train, y_train, cv = kf)
        wyniki_train.append(scores.mean())
        scores = cross_val_score(Tree, X_test, y_test, cv = kf)
        wyniki_test.append(scores.mean())
        
        for i in range(1,wart + 1):
            Tree = tree.DecisionTreeClassifier(max_depth = i,
                                               random_state =335723 )
            scores = cross_val_score(Tree, X_train, y_train, cv = kf)
            wyniki_train.append(scores.mean())
            scores = cross_val_score(Tree, X_test, y_test, cv = kf)
            wyniki_test.append(scores.mean())
            
            Tree = tree.DecisionTreeClassifier(min_samples_leaf = i,
                                               random_state=335723)
            scores = cross_val_score(Tree, X_train, y_train, cv = kf)
            wyniki_train.append(scores.mean())
            scores = cross_val_score(Tree, X_test, y_test, cv = kf)
            wyniki_test.append(scores.mean())
            
    return(wyniki_train,wyniki_test)
              
wyniki_train,wyniki_test  = accuracy(8,X,y,25)
print(wyniki_train,wyniki_test)

dt = tree.DecisionTreeClassifier()

param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [5, 10, 15, 20],
    'min_samples_leaf': [5, 10, 15, 20],
    'min_samples_split': [5, 10, 15, 20]
}
kf = KFold(n_splits = 8, random_state =335723, shuffle = True )
grid_search = GridSearchCV(dt, param_grid, cv=kf, scoring='accuracy', n_jobs=-1)

grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Najlepsze parametry na zbiorze treningowym:", best_params)
print("Najlepsza dokładność na zbiorze treningowym:", best_score)

best_dt = tree.DecisionTreeClassifier(**best_params)
best_dt.fit(X_train, y_train)
y_pred = best_dt.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)

print("Dokładność na zbiorze testowym:", test_accuracy)

Tree = tree.DecisionTreeClassifier(criterion= 'entropy', max_depth= 20, min_samples_leaf= 5, min_samples_split= 5,
                                               random_state = 335723 ) 
Tree = Tree.fit(X_train, y_train)
y_pred_test = Tree.predict(X_test)
print("accuracy:", accuracy_score(y_test, y_pred_test))
print("recall:", recall_score(y_test, y_pred_test))
print("precision:", precision_score(y_test, y_pred_test))

roc_auc_score(y_test, Tree.predict_proba(X_test)[:, 1])
RocCurveDisplay.from_estimator(Tree, X_test, y_test)