
import matplotlib.pyplot as plt
import seaborn as sns

# Class distribution
def plot_class_distribution(class_counts):
    plt.figure()
    plt.bar(class_counts.keys(), class_counts.values())
    plt.title("Class Distribution")
    plt.xlabel("Classes")
    plt.ylabel("Count")

# Missing values
def plot_missing(df):
    plt.figure()
    df.isnull().sum().plot(kind='bar')
    plt.title("Missing Values")
    plt.xlabel("Columns")
    plt.ylabel("Count")

# Correlation heatmap
def plot_correlation(df):
    plt.figure()
    sns.heatmap(df.corr(), annot=True)
    plt.title("Correlation Heatmap")