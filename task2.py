import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Dataset .csv")

# Display basic information
print("===================================")
print("DATASET INFORMATION")
print("===================================")
print("Number of Rows and Columns:", df.shape)

# Statistical Summary
print("\n===================================")
print("STATISTICAL SUMMARY")
print("===================================")
print(df.describe())

# Mean
print("\n===================================")
print("MEAN")
print("===================================")
print(df.select_dtypes(include=['int64', 'float64']).mean())

# Median
print("\n===================================")
print("MEDIAN")
print("===================================")
print(df.select_dtypes(include=['int64', 'float64']).median())

# Standard Deviation
print("\n===================================")
print("STANDARD DEVIATION")
print("===================================")
print(df.select_dtypes(include=['int64', 'float64']).std())

# Country Code Distribution
print("\n===================================")
print("COUNTRY CODE DISTRIBUTION")
print("===================================")
country_distribution = df["Country Code"].value_counts()
print(country_distribution)

# City Distribution
print("\n===================================")
print("CITY DISTRIBUTION")
print("===================================")
city_distribution = df["City"].value_counts()
print(city_distribution)

# Top 10 Cities
print("\n===================================")
print("TOP 10 CITIES WITH HIGHEST NUMBER OF RESTAURANTS")
print("===================================")
top_cities = df["City"].value_counts().head(10)
print(top_cities)

# Cuisine Distribution
print("\n===================================")
print("CUISINE DISTRIBUTION")
print("===================================")
cuisine_distribution = df["Cuisines"].value_counts()
print(cuisine_distribution)

# Top 10 Cuisines
print("\n===================================")
print("TOP 10 CUISINES")
print("===================================")
top_cuisines = df["Cuisines"].value_counts().head(10)
print(top_cuisines)

# Bar Chart for Top Cities
plt.figure(figsize=(10, 5))
top_cities.plot(kind='bar')
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart for Top Cuisines
plt.figure(figsize=(12, 5))
top_cuisines.plot(kind='bar')
plt.title("Top 10 Cuisines by Number of Restaurants")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()