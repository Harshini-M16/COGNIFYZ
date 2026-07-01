import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Dataset .csv")   

print("===================================")
print("TABLE BOOKING AND ONLINE DELIVERY")
print("===================================")

# -----------------------------------
# 1. Percentage of Restaurants
# -----------------------------------

table_booking = (df["Has Table booking"] == "Yes").mean() * 100
online_delivery = (df["Has Online delivery"] == "Yes").mean() * 100

print("\nPercentage of Restaurants")
print("-------------------------")
print("Table Booking :", round(table_booking, 2), "%")
print("Online Delivery :", round(online_delivery, 2), "%")

# -----------------------------------
# 2. Average Ratings
# -----------------------------------

ratings = df.groupby("Has Table booking")["Aggregate rating"].mean()

print("\nAverage Ratings")
print("----------------")
print(ratings)

# -----------------------------------
# 3. Online Delivery by Price Range
# -----------------------------------

delivery = pd.crosstab(
    df["Price range"],
    df["Has Online delivery"],
    normalize="index"
) * 100

print("\nOnline Delivery Percentage by Price Range")
print("------------------------------------------")
print(delivery.round(2))

# -----------------------------------
# Graph 1
# -----------------------------------

plt.figure(figsize=(5,4))
plt.bar(
    ["Table Booking", "Online Delivery"],
    [table_booking, online_delivery]
)

plt.title("Restaurant Services")
plt.ylabel("Percentage")

#Save Graph 1
plt.savefig("graph1_restaurannt_services.png")
plt.show()

# -----------------------------------
# Graph 2
# -----------------------------------

ratings.plot(kind="bar")

plt.title("Average Rating by Table Booking")
plt.xlabel("Table Booking")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)

#Save Graph 2
plt.savefig("graph2_average_rating.png")
plt.show()

# -----------------------------------
# Graph 3
# -----------------------------------

delivery.plot(kind="bar")

plt.title("Online Delivery by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Percentage")
plt.xticks(rotation=0)

#Save Graph 3
plt.savefig("graph3_online_delivery.png")
plt.show()

print("\nTask Completed Successfully!")