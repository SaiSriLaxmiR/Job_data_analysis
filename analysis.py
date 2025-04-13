import pandas as pd

# Load the dataset
df = pd.read_csv("sample_jobs.csv")

# View top rows
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())
df["Salary (USD)"] = df["Salary (USD)"].fillna(df["Salary (USD)"].mean())
df.dropna(subset=["Job Title", "Company"], inplace=True)
df.drop_duplicates(inplace=True)
print(df.isnull().sum())
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x="Job Title", y="Salary (USD)", data=df)
plt.title("Average Salary by Job Title")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(x="Location", y="Salary (USD)", data=df)
plt.title("Salary Distribution by Location")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 6))
remote_counts = df["Remote"].value_counts()
plt.pie(remote_counts, labels=remote_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Remote vs On-site Job Distribution")
plt.tight_layout()
plt.show()
df.to_csv("cleaned_sample_jobs.csv", index=False)
