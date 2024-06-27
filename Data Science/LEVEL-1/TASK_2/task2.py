#level-1 Task-2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Read the dataset from CSV file

df = pd.read_csv(r'C:\Users\haris\OneDrive - Vasireddy Venkatadri Institute of Technology\Desktop\internship certificates\Cognifyz Technologies\Data Science\Dataset.csv')


# Calculate basic statistics for numerical columns
numerical_stats = df.describe()
print("Basic Statistical Measures for Numerical Columns:")
print(numerical_stats)

# Explore categorical variables
country_counts = df['Country Code'].value_counts()
city_counts = df['City'].value_counts()
cuisine_counts = df['Cuisines'].value_counts()

# Visualize distribution of categorical variables
plt.figure(figsize=(10, 6))
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.title('Distribution of Country Codes')
plt.xlabel('Country Code')
plt.ylabel('Count')
plt.show()


# Repeat similar visualization for 'City' and 'Cuisines'
top_cuisines = df['Cuisines'].value_counts().head(10)
print("Top cuisines with the highest number of restaurants:")
print(top_cuisines)

# Top cities with the highest number of restaurants
top_cities = df['City'].value_counts().head(10)

print("\nTop cities with the highest number of restaurants:")
print(top_cities)
