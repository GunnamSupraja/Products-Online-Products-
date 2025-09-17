import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("products.csv")
print("Price -> Mean:", np.mean(df['price']), "Median:", np.median(df['price']))
print("Rating -> Mean:", np.mean(df['rating']), "Median:", np.median(df['rating']))

plt.hist(df['price'], bins=20, color='skyblue')
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

plt.scatter(df['price'], df['rating'], color='purple')
plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")
plt.show()

df['category'].value_counts().plot(kind='bar', color='orange')
plt.title("Number of Products per Category")
plt.ylabel("Count")
plt.xlabel("Category")
plt.show()

pivot = df.pivot_table(values=['price','rating'], index='category', aggfunc='mean')
print("Pivot Table:", pivot)
pivot.plot(kind='bar')
plt.title("Average Price & Rating by Category")
plt.ylabel("Value")
plt.xlabel("Category")
plt.show()
