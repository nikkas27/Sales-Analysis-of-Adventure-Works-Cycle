import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


Vtargetbuy = pd.read_csv('F:/Cleveland State University/Fall 19/CIS 660/Assign 1/VTargetBuyUpdated_Occ.csv')

# print(Vtargetbuy)
# print(Vtargetbuy.columns)
BikeBuyList = pd.read_csv("F:/Cleveland State University/Fall 19/CIS 660/Assign 1/vTargetMailCustomer.csv", header=0,encoding = 'unicode_escape')
# print(BikeBuyList.columns)
bikebuy = BikeBuyList.values[:,31]
# print(bikebuy)
Vtargetbuy['BikeBuy'] = bikebuy

# print(Vtargetbuy.columns)

# Vtargetbuy.to_csv('F:/Cleveland State University/Fall 19/CIS 660/Assign 1/VTargetBuyUpdated_Occ.csv', sep=',')
#
# print(Vtargetbuy.columns)
Vtargetbuy.drop(['Unnamed: 0'], 1, inplace=True)
# Vtargetbuy.drop(['Unnamed: 0.1'], 1, inplace=True)
Vtargetbuy.drop(['Unnamed: 0.1.1'], 1, inplace=True)

Vtargetbuy.dropna(inplace=True)
print(Vtargetbuy.isnull().any())
# Vtargetbuy.to_csv('F:/Cleveland State University/Fall 19/CIS 660/Assign 1/VTargetBuyUpdated_Occ.csv', sep=',')
print(Vtargetbuy.columns)

train=Vtargetbuy.values[:,9:34] #Inc = 69.50 and RF: 69.44
test=Vtargetbuy.values[:,35]


y=test.astype('int')
X=train.astype('int')

print(test,train)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)

print("X_Train:",len(X_train),"XTest:",len(X_test),"YTest:",len(y_test),"YTrain:",len(y_train))

print("------------------Decision tree Classifier------------------------")
classifier = DecisionTreeClassifier(criterion='gini', random_state=0) # min_samples_split=8, min_impurity_split=0.3
classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)
print("Prediction of Decision Tree:",y_pred)
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix generated by the classifier:\n",cm)
accuracy_dt = accuracy_score(y_test, y_pred)
print("Accuracy of Decision Tree:",accuracy_dt)

print("--------------------------------------RF-----------------------------------------")

rf_classifier = RandomForestClassifier(n_estimators=400, criterion='entropy',min_samples_split=17, random_state=0) # ,
rf_classifier.fit(X_train, y_train)
y_pred=rf_classifier.predict(X_test)
print("Prediction of Random Forest:",y_pred)

cm=confusion_matrix(y_test, y_pred)

print("Confusion matrix generated by the classifier:\n",cm)
accuracy_rf = accuracy_score(y_test, y_pred)
print("Accuracy of Random Forest:",accuracy_rf)

print("---------------Extra credit PCA --------------------------------------------")


importance_rf = rf_classifier.feature_importances_
c=importance_rf*100
importance_rf = pd.DataFrame(c, index=Vtargetbuy.columns[9:34], columns=["Importance"])
print(importance_rf)



sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
# print(X_test,X_train)

pca=PCA(n_components=None)
X_train=pca.fit_transform(X_train)
X_test=pca.transform(X_test)
explained_variance=pca.explained_variance_ratio_
print("Explained variance:",explained_variance)

classifier = DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(X_train, y_train)
y_pred=classifier.predict(X_test)

cm=confusion_matrix(y_test, y_pred)

accuracy_dt = accuracy_score(y_test, y_pred)
print("Accuracy of Decision Tree with PCA:",accuracy_dt)
