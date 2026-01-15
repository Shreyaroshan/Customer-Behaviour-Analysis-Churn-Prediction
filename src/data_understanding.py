import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/Telco-Customer-Churn.csv")

print(df.head())
print(df.shape)
print(df.info())
