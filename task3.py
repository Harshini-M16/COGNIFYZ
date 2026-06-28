# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv("Dataset .csv")

# Display first 5 rows
print(df.head())

# -------------------------------
# 1. Restaurant Locations on Map
# -------------------------------
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Restaurant Name",
    title="Restaurant Locations"
)

fig.show()

# -------------------------------------
# 2. Distribution of Restaurants by City
# -------------------------------------
city = df["City"].value_counts()

print("\nRestaurants in Each City:")
print(city)

plt.figure(figsize=(10,5))
city.head(10).plot(kind="bar")
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.show()

# ----------------------------------------
# 3. Distribution of Restaurants by Country
# ----------------------------------------
country = df["Country Code"].value_counts()

print("\nRestaurants in Each Country:")
print(country)

plt.figure(figsize=(8,5))
country.plot(kind="bar")
plt.title("Restaurants by Country")
plt.xlabel("Country Code")
plt.ylabel("Number of Restaurants")
plt.show()

# ---------------------------------------
# 4. Correlation Between Location & Rating
# ---------------------------------------
plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x="Longitude",
    y="Latitude",
    hue="Aggregate rating"
)

plt.title("Restaurant Location vs Rating")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# -------------------------
# 5. Average Rating by City
# -------------------------
rating = df.groupby("City")["Aggregate rating"].mean()

print("\nAverage Rating by City:")
print(rating.sort_values(ascending=False))

plt.figure(figsize=(10,5))
rating.sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top 10 Cities by Average Rating")
plt.xlabel("City")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.show()