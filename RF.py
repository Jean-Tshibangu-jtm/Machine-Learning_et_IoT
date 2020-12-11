# -*- coding: utf-8 -*-
"""RF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KdVfJ9zUc_CYgZDHKsmJlWk4k_JxuyxJ
"""

import statsmodels as stat
#mport seaborn as sbrn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.metrics import classification_report
#import sklearn.linear_model.LogisticRegression as LogisticRegression
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import RFE

from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif

dataSetFin = pd.read_csv('dataSetFinal.csv')

print(dataSetFin.shape)

dataSetFin.head(6)

target= dataSetFin.iloc[:,7].values

attributs_autres = dataSetFin.iloc[:,0:7].values

#RFE, SELECTION DES ATTRIBUTS PERTINENTS

selection_features = LogisticRegression()

rfe = RFE(selection_features, 3)

fit = rfe.fit(attributs_autres,target)

print("Feature Ranking: %s"% fit.ranking_)
print("Selected Features: %s"% fit.support_)
print("Feature Ranking: %s"% fit.ranking_)

dataSetFin.head()

#features_final=dataSetFin.iloc[:,[1,4,5]].values

x = dataSetFin.drop('Target', axis = 1).values

target = dataSetFin['Target'].values

target_final=dataSetFin.iloc[:,-1].values

features_data_train,features_data_test,target_data_train,target_data_test = train_test_split(x,target,test_size = 0.2,random_state = 0)

StdSc = StandardScaler()
features_data_train = StdSc.fit_transform(features_data_train)
features_data_test = StdSc.fit_transform(features_data_test)



target_final=dataSetFin.iloc[:,-1].values

target_data_train=target_data_train
target_data_test=target_data_test

#Visualisation

plt.hist(target_final[:,],bins=2,rwidth=0.60, color='pink')
#Labeliser l'Axes et Titre
plt.title('Proportion attack MITM and Normal')
plt.ylabel('  Echantillon')
plt.xlabel('Attack Distribution') 

donnee_ligne ={"attaque":["Normale","Anormale"]}
df= pd.DataFrame(donnee_ligne, columns=pd.Index(['attaque'],name='attribute'))
plt.savefig('Proportion Attack MITM et Normale.pdf', format='pdf')

#mplt.savefig('Proportion Attack MITM et Normale.pdf', format='pdf')

#######Create predictive data and data to predict

target_final=dataSetFin.iloc[:,-1].values

features_final=dataSetFin.iloc[:,[1,4,5]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, target, test_size = 0.30,random_state = 42, stratify = target)

X_test.shape

############ The next step is to create the random forest classifier.

from sklearn.ensemble import RandomForestClassifier

# Initialize a random forest classifier with default parameters

Random_FrsCls = RandomForestClassifier(random_state = 50)

Random_FrsCls.fit(X_train, y_train)

# assess its accuracy from the test data.

test_score = Random_FrsCls.score(X_test, y_test)

# Evalution With Confusion Matrix
from sklearn.metrics import confusion_matrix

print("Test score: %.2f%%" % (test_score * 100.0))

y_pred = Random_FrsCls.predict(X_test)

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
jean_func_conf_matrix(cm, group_names=labels, categories=categories, cmap='tab20_r')

print(classification_report(y_test,y_pred))

#End

