# -*- coding: utf-8 -*-
"""DecisionTree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16ZUuyqadAbqdaOjWvxyi5yxjTwHlZNWm
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import seaborn as sns  
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
import numpy as np

dataSetFin = pd.read_csv('dataSetFinal.csv')

X = dataSetFin.drop('Target', axis = 1).values

target = dataSetFin['Target'].values

X_train, X_test, y_train, y_test = train_test_split(X, target, test_size = 0.30, random_state = 42, stratify = target)

decTree = DecisionTreeClassifier(criterion = 'gini', random_state = 50)

decTree.fit(X_train, y_train)

# évaluons sa précision sur les données de test.
decTree.score(X_test, y_test)
y_pred = decTree.predict(X_test)

decTree.score(X_test, y_test)

# Evalution avec Matrice de Confusion 
cm = confusion_matrix(y_test, y_pred)

cm

def jean_func_conf_matrix(cf, group_names=None,categories='auto',count=True,
                          percent=True,cbar=True, xyticks=True,xyplotlabels=True,
                          sum_stats=True,figsize=None,cmap='Blues',title='Confusion matrix'):
   
    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names)==cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    if percent:
        group_percentages = ["{0:.2%}".format(value) for value in cf.flatten()/np.sum(cf)]
    else:
        group_percentages = blanks

    box_labels = [f"{v1}{v2}{v3}".strip() for v1, v2, v3 in zip(group_labels,group_counts,group_percentages)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0],cf.shape[1])


    
    if sum_stats:
       
        accuracy  = np.trace(cf) / float(np.sum(cf))

        
        if len(cf)==2:
            
            precision = cf[1,1] / sum(cf[:,1])
            recall    = cf[1,1] / sum(cf[1,:])
            f1_score  = 2*precision*recall / (precision + recall)
            stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy,precision,recall,f1_score)
        else:
            stats_text = "\n\nAccuracy={:0.3f}".format(accuracy)
    else:
        stats_text = ""


    if figsize==None:
        
        figsize = plt.rcParams.get('figure.figsize')

    if xyticks==False:
      
        categories=False

    plt.figure(figsize=figsize)
    sns.heatmap(cf,annot=box_labels,fmt="",cmap=cmap,cbar=cbar,xticklabels=categories,yticklabels=categories)

    if xyplotlabels:
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label' + stats_text)
    else:
        plt.xlabel(stats_text)
    
    if title:
        plt.title(title)

labels = ['True Negative','False Negative','False Positive','True Positive']
categories = ['0', '1']
jean_func_conf_matrix(cm, group_names=labels, categories=categories, cmap='Greens')

print(classification_report(y_test,y_pred))

#End