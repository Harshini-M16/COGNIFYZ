import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Restaurant.csv")

# 1. Explore Dataset
print("Dataset Shape:", df.shape)
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nFirst 5 Rows:")
print(df.head())

# 2. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Values
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        try:
            df[col].fillna(df[col].mean(), inplace=True)
        except:
            pass

# 3. Data Types
print("\nData Types:")
print(df.dtypes)

# 4. Distribution of Aggregate Rating
print("\nAggregate Rating Distribution:")
print(df["Aggregate rating"].value_counts())

# 5. Percentage Distribution (Class Imbalance)
print("\nPercentage Distribution:")
print(df["Aggregate rating"].value_counts(normalize=True) * 100)

# 6. Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Aggregate rating"], bins=10)
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Aggregate Rating")
plt.ylabel("Frequency")
plt.show()