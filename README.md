
# 🛡️ Optimisation de la détection des attaques Man-In-The-Middle (MIM) dans les réseaux IoT via le Machine Learning

## 📌 Contexte

L’essor massif de l’Internet des Objets (IoT) transforme notre quotidien, avec des applications allant des maisons intelligentes à la santé connectée. Cependant, cette connectivité accrue s’accompagne d’un accroissement significatif des menaces en cybersécurité, notamment les attaques **Man-In-The-Middle (MIM)**. Les dispositifs IoT, souvent peu sécurisés, deviennent des cibles faciles pour ces intrusions.

## ❗ Problématique

Malgré l’utilisation d’IDS (Intrusion Detection Systems) traditionnels, ces outils restent insuffisants face aux attaques MIM, en particulier dans des environnements à faible puissance de calcul comme les objets connectés. L’enjeu est donc de :
- Détecter efficacement les attaques MIM en environnement IoT,
- Optimiser le temps de détection pour permettre une réaction rapide,
- S’appuyer sur des modèles légers et performants de machine learning.

## 🧠 IA et Algorithmes Utilisés

Trois modèles de classification supervisée ont été développés pour détecter les paquets malveillants :
- **Random Forest (RF)** : obtient une précision et un F1-score de 100 %.
- **Decision Tree (DT)** : offre également une performance parfaite avec les paramètres par défaut.
- **Logistic Regression (LR)** : atteint une précision de 98,6 %, avec une sensibilité accrue aux erreurs sur les classes positives.

Chaque modèle a été évalué à l’aide de matrices de confusion, F1-score, précision et rappel.

## 🔧 Technologies & Outils

- **Langage** : Python  
- **Librairies** : `pandas`, `scikit-learn`, `matplotlib`, `seaborn`  
- **Environnement** : Google Colab, Jupyter Notebook  
- **Outils de capture de paquets** : Aircrack-ng  
- **Formats des données** : Fichiers `.pcap`, convertis en `.csv` après filtrage  

## 🧪 Environnement de Test (Testbed)

Le jeu de données utilisé provient du **HCRL (Hacking and Countermeasure Research Lab)**. L’infrastructure inclut :
- Dispositifs IoT réels : **caméra EZVIZ Wi-Fi** et **enceinte intelligente SKT NUGU**  
- Réseau local sans fil partagé avec smartphones et ordinateurs portables  
- Paquets capturés via mode moniteur Wi-Fi, nettoyés pour préserver la confidentialité  

Les attaques MIM ont été simulées à l’aide de Nmap et ARP Spoofing, et représentent un ensemble de 6 fichiers `.pcap`, totalisant 194 184 paquets, dont environ 52 % malveillants.

## 🧹 Prétraitement des Données

- Application de règles de filtrage via scripts shell pour extraire les flux MIM.
- Étiquetage des paquets :  
  - `Target = 1` → Attaque  
  - `Target = 0` → Trafic normal
- Fusion et nettoyage des fichiers `.csv` pour construire un ensemble final d'entraînement/test.
- Découpage : **70 % entraînement** / **30 % test**

## 📈 Résultats

| Modèle             | Précision | Rappel | F1-Score | Accuracy |
|--------------------|-----------|--------|----------|----------|
| Random Forest       | 100 %     | 100 %  | 100 %    | 100 %    |
| Decision Tree       | 100 %     | 100 %  | 100 %    | 100 %    |
| Logistic Regression | 99 %      | 99 %   | 99 %     | 98.6 %   |

Les modèles Random Forest et Decision Tree ont montré une efficacité parfaite sur les jeux de données testés.

## 📌 Contributions

- Conception d’un pipeline IA complet pour la détection des attaques MIM.
- Utilisation de données réelles IoT capturées en environnement simulé.
- Prototypage et validation de plusieurs modèles supervisés.
- Proposition d’un testbed IoT reproductible pour la recherche académique.

## 🔭 Perspectives

Le travail futur envisagé inclut :
- L’intégration de modèles Deep Learning (CNN, LSTM) pour détecter des attaques plus complexes.
- La mise en œuvre d’un système de détection en temps réel dans des environnements Edge/Fog Computing.
- L’enrichissement du dataset avec d’autres types d’attaques IoT (DoS, spoofing DNS, etc.).
