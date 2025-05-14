# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set seaborn style for prettier plots
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset

# Load Iris dataset from sklearn
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# No missing values in this dataset, so no cleaning is needed

# Task 2: Basic Data Analysis

# Basic statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species and calculate mean of numerical features
grouped = df.groupby('species').mean()
print("\nMean of features grouped by species:")
print(grouped)

# Observations
print("\nObservations:")
print("- Setosa has the smallest average petal length and width.")
print("- Virginica has the largest average values for most features.")

# Task 3: Data Visualization

# Line Chart (simulated time-series using index)
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title('Sepal and Petal Lengths Over Index')
plt.xlabel('Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

# Bar Chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df, estimator='mean', ci=None)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# Histogram: Distribution of sepal width
plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter Plot: Sepal length vs petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()
