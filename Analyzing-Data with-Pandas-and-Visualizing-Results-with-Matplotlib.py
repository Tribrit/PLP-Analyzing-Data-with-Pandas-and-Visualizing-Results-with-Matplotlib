import pandas as pd  # Importing pandas for data handling
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting
import seaborn as sns  # Importing Seaborn for enhanced visualizations

# Task 1: Load and Explore the Dataset
try:
    # Load dataset (update 'your_dataset.csv' with actual filename)
    df = pd.read_csv('your_dataset.csv')
    print("Dataset loaded successfully!\n")
    
    # Display first few rows
    print("First five rows of the dataset:")
    print(df.head())
    
    # Display dataset info (structure)
    print("\nDataset Information:")
    print(df.info())
    
    # Checking for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Handling missing values (fill with mean for numerical, drop for categorical)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df.dropna(inplace=True)  # Drop remaining categorical missing values
    print("\nDataset cleaned successfully!\n")
    
except FileNotFoundError:
    print("Error: The file was not found. Please check the filename and try again.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Task 2: Basic Data Analysis
print("Basic Statistics:")
print(df.describe())

# Example grouping (modify column names accordingly)
if 'Category' in df.columns:
    print("\nAverage numerical values per category:")
    print(df.groupby('Category').mean())

# Task 3: Data Visualization
plt.figure(figsize=(10, 6))

# Line Chart (Trends over Time, assumes a 'Date' column exists)
if 'Date' in df.columns and 'Sales' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])  # Convert date column to datetime
    df.set_index('Date')['Sales'].plot(title="Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()

# Bar Chart (Comparison per Category)
if 'Category' in df.columns and 'Revenue' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Category', y='Revenue', data=df)
    plt.title("Revenue by Category")
    plt.xticks(rotation=45)
    plt.show()

# Histogram (Distribution of a Numerical Column)
if 'Price' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Price'], bins=20, kde=True)
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.show()

# Scatter Plot (Relationship between Two Numerical Variables)
if 'Quantity' in df.columns and 'Revenue' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Quantity', y='Revenue', data=df)
    plt.title("Quantity vs Revenue")
    plt.xlabel("Quantity Sold")
    plt.ylabel("Revenue Generated")
    plt.show()

print("\nAnalysis complete! Check the plots for insights.")
