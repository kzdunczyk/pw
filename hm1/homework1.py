
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

X = pd.read_csv("../pw/hm1/X.csv")
y = pd.read_csv("../pw/hm1/y.csv")

def accuracy(cv:int,X, y, wart = 0):
    """Function calculates accuracy

    Args:
        cv (int): _description_
        X (_type_): _description_
        y (_type_): _description_
        wart (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """
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
               , wyniki4,)
    
wyniki  = accuracy(8,X,y, 10)
print(wyniki)


fig, ax = plt.subplots()

# List of colors for the lines
colors = ['r', 'g', 'b','b','b','b','b','b','b','b','b','b',
          'y','y','y','y','y','y','y','y','y','y']


for y, color in zip(wyniki, colors):
    ax.axhline(y=y, color=color, linestyle='--')

# Add labels and a legend (optional)
ax.set_ylabel('Accuracy')
ax.set_ylim(0.63, 0.84)
ax.set_xticklabels([])
# Display the plot
plt.show()

largest_value = max(wyniki)
largest_index = wyniki.index(largest_value)
print(largest_value, largest_index)


X = pd.read_csv("C:/Users/Kajetan/Desktop/pw/hm1/X.csv")
y = pd.read_csv("C:/Users/Kajetan/Desktop/pw/hm1/y.csv")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state= 335723)
Tree = tree.DecisionTreeClassifier(criterion = 'entropy',
                                               random_state = 335723 ) 
Tree = Tree.fit(X_train, y_train)
y_pred_test = Tree.predict(X_test)
print("accuracy:", accuracy_score(y_test, y_pred_test))
print("recall:", recall_score(y_test, y_pred_test))
print("precision:", precision_score(y_test, y_pred_test))

roc_auc_score(y_test, Tree.predict_proba(X_test)[:, 1])
RocCurveDisplay.from_estimator(Tree, X_test, y_test)