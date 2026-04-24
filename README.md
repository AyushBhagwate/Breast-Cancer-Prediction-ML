# 🧠 Breast Cancer Prediction using Machine Learning

## 📌 Overview

This project predicts whether a tumor is **benign or malignant** using a Decision Tree classifier.
It demonstrates an end-to-end machine learning workflow including **EDA, preprocessing, model training, and evaluation**.

---

## 🚀 Features

* 📊 Manual + Automated EDA
* ⚙️ Pipeline-based preprocessing
* 🔍 Hyperparameter tuning using GridSearchCV
* 📈 Model evaluation with multiple metrics
* 📊 Feature importance visualization (Seaborn)

---

## 📂 Project Structure

```
breast_cancer_pj3/
│
├── data/
│   └── breast_cancer.csv
│
├── notebooks/

│   └── eda.ipynb
│
├── outputs/
│   ├── profile_report.html
│   ├── metrics.txt
│   └── predictions.csv
│
├── models/
│   └── best_model.pkl
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   ├── improve_model.py
│
├── creating_file.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔍 Exploratory Data Analysis (EDA)

### 📘 Manual EDA

* Located in: `notebooks/eda.ipynb`
* Includes:

  * Data distribution analysis
  * Correlation analysis
  * Feature relationships

### 🤖 Automated EDA

* Generated using **ydata-profiling**
* Saved at: `outputs/profile_report.html`

👉 Provides:

* Feature summaries
* Missing values analysis
* Correlations
* Data quality checks

---

## 📈 Model Performance

* ✅ Accuracy: ~95%
* ✅ Strong precision & recall
* ✅ Low prediction errors

---

## 📊 Visualization

### 🔹 Feature Importance

* Built using Seaborn
* Shows most influential features

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 🧠 Key Learnings

* Building ML pipelines
* Hyperparameter tuning with GridSearchCV
* Combining manual + automated EDA
* Interpreting feature importance
* Understanding model evaluation

---

## 📌 Future Improvements

* Add confusion matrix visualization
* Try Random Forest / XGBoost
* Add ROC-AUC curve
* Deploy using Streamlit

---

## 👤 Author

**Ayush Bhagwate**
