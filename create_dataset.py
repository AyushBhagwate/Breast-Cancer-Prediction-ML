# Script to generate and save dataset to data/breast_cancer.csv

#Lib
import pandas as pd
from sklearn.datasets import load_breast_cancer
import os

# Creating dir -
os.makedirs('data', exist_ok=True)

data = load_breast_cancer() #Loading dataset 

df = pd.DataFrame(data.data, columns=data.feature_names )
df['target'] = data.target

df.to_csv('data/breast_cancer.csv', index=False) # Converting into CSV-file

print('csv file created')