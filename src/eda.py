import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../data/Telco-Customer-Churn.csv")
print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True))
# Average tenure by churn
print(df.groupby("Churn")["tenure"].mean())
print(df.groupby("Churn")["MonthlyCharges"].mean())
print(pd.crosstab(df["Contract"], df["Churn"], normalize="index"))
# Customers who churn tend to have lower tenure
# Month-to-month contracts show higher churn rates
