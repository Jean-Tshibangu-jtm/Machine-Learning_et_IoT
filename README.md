
# Optimization of Man-In-The-Middle (MIM) Attack Detection in IoT Networks Using Machine Learning

## Context

The rapid growth of the Internet of Things (IoT) is transforming our daily lives, with applications ranging from smart homes to connected healthcare. However, this increased connectivity also brings a significant rise in cybersecurity threats, especially **Man-In-The-Middle (MIM)** attacks. IoT devices, often poorly secured, are easy targets for such intrusions.

## Problem Statement

Despite the use of traditional Intrusion Detection Systems (IDS), these tools remain insufficient against MIM attacks, particularly in resource-constrained environments like connected objects. The challenge is therefore to:
- Effectively detect MIM attacks in IoT environments,
- Optimize detection time for quick reaction,
- Leverage lightweight and efficient machine learning models.

## AI & Algorithms Used

Three supervised classification models were developed to detect malicious packets:
- **Random Forest (RF)**: achieved 100% precision and F1-score.
- **Decision Tree (DT)**: also delivered perfect performance with default parameters.
- **Logistic Regression (LR)**: achieved 98.6% accuracy, with higher sensitivity to errors on positive classes.

Each model was evaluated using confusion matrices, F1-score, precision, and recall.

## Technologies & Tools

- **Language**: Python  
- **Libraries**: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`  
- **Environment**: Google Colab, Jupyter Notebook  
- **Packet capture tools**: Aircrack-ng  
- **Data formats**: `.pcap` files, converted to `.csv` after filtering  

## Testbed Environment

The dataset used originates from the **HCRL (Hacking and Countermeasure Research Lab)**. The infrastructure includes:
- Real IoT devices: **EZVIZ Wi-Fi camera** and **SKT NUGU smart speaker**  
- Wireless LAN shared with smartphones and laptops  
- Packets captured using Wi-Fi monitor mode and sanitized to preserve privacy  

MIM attacks were simulated using Nmap and ARP Spoofing, resulting in 6 `.pcap` files totaling 194,184 packets, with approximately 52% malicious content.

## Data Preprocessing

- Filtering rules applied via shell scripts to extract MIM flows.
- Packet labeling:  
  - `Target = 1` → Attack  
  - `Target = 0` → Normal traffic
- Merged and cleaned `.csv` files to build a final training/test dataset.
- Split: **70% training** / **30% test**

## 📈 Results

| Model              | Precision | Recall | F1-Score | Accuracy |
|--------------------|-----------|--------|----------|----------|
| Random Forest       | 100%      | 100%   | 100%     | 100%     |
| Decision Tree       | 100%      | 100%   | 100%     | 100%     |
| Logistic Regression | 99%       | 99%    | 99%      | 98.6%    |

Random Forest and Decision Tree models showed perfect efficiency on the test dataset.

## 📌 Contributions

- Designed a complete AI pipeline for detecting MIM attacks.
- Used real IoT data captured in a simulated environment.
- Prototyped and validated multiple supervised learning models.
- Proposed a reproducible IoT testbed for academic research.

## Future Work

Future directions include:
- Integration of Deep Learning models (CNN, LSTM) for detecting more complex attacks.
- Implementation of a real-time detection system in Edge/Fog Computing environments.
- Enrichment of the dataset with other IoT attack types (DoS, DNS spoofing, etc.).
