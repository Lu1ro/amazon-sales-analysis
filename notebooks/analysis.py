import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CONFIGURATION & SETUP ---
# Set styling for professional report quality
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

# Ensure directories exist
os.makedirs('../images', exist_ok=True)
os.makedirs('../data', exist_ok=True)

# --- 1. DATA LOADING & CLEANING ---
def load_and_clean_data(filepath):
    """
    Loads data and performs cleaning: currency conversion, 
    handling missing values, and type casting.
    """
    print("Loading data...")
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}. Please check the path.")
        return None

    # Helper functions for cleaning
    def clean_currency(x):
        if isinstance(x, str):
            x = x.replace('₹', '').replace(',', '').strip()
            return float(x) if x else np.nan
        return x

    def clean_percentage(x):
        if isinstance(x, str):
            x = x.replace('%', '').strip()
            return float(x) if x else np.nan
        return x

    # Apply cleaning
    print("Cleaning pricing and ratings...")
    df['discounted_price'] = df['discounted_price'].apply(clean_currency)
    df['actual_price'] = df['actual_price'].apply(clean_currency)
    df['discount_percentage'] = df['discount_percentage'].apply(clean_percentage)
    
    # Handle rating counts (remove commas)
    df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '', regex=False)
    df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')
    
    # Handle ratings (some have anomalies like '|')
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

    # Extract Main Category for higher-level analysis
    df['main_category'] = df['category'].astype(str).str.split('|').str[0]

    # Drop rows with critical missing data for this analysis
    df_clean = df.dropna(subset=['discounted_price', 'rating', 'rating_count', 'main_category'])
    
    print(f"Data cleaned. Rows remaining: {len(df_clean)}")
    return df_clean

# --- 2. VISUALIZATION FUNCTIONS ---

def plot_top_categories(df):
    """Visualizes top 10 categories by product volume."""
    plt.figure(figsize=(12, 6))
    top_cat = df['main_category'].value_counts().nlargest(10)
    
    ax = sns.barplot(x=top_cat.values, y=top_cat.index, palette='viridis', hue=top_cat.index, legend=False)
    plt.title('Top 10 Product Categories by Inventory Volume', fontsize=16, fontweight='bold')
    plt.xlabel('Number of Products')
    plt.ylabel('')
    
    # Add value labels
    for i in ax.containers:
        ax.bar_label(i, padding=3)
        
    plt.tight_layout()
    plt.savefig('../images/1_top_categories.png', dpi=300)
    print("Saved: 1_top_categories.png")
    plt.close()

def plot_discount_distribution(df):
    """Analyzes the distribution of discount percentages."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['discount_percentage'], bins=20, kde=True, color='teal')
    plt.title('Distribution of Discount Percentages', fontsize=16, fontweight='bold')
    plt.xlabel('Discount (%)')
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    plt.savefig('../images/2_discount_distribution.png', dpi=300)
    print("Saved: 2_discount_distribution.png")
    plt.close()

def plot_price_vs_rating(df):
    """Scatter plot to check if higher price means higher rating."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='discounted_price', y='rating', alpha=0.5, color='darkblue')
    plt.xscale('log') # Log scale because prices vary wildly
    plt.title('Price vs. Product Rating (Log Scale)', fontsize=16, fontweight='bold')
    plt.xlabel('Discounted Price (Log Scale)')
    plt.ylabel('Rating (0-5)')
    
    plt.tight_layout()
    plt.savefig('../images/3_price_vs_rating.png', dpi=300)
    print("Saved: 3_price_vs_rating.png")
    plt.close()

def plot_correlation(df):
    """Heatmap of correlations between numerical features."""
    plt.figure(figsize=(8, 6))
    cols = ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']
    corr = df[cols].corr()
    
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix', fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('../images/4_correlation_heatmap.png', dpi=300)
    print("Saved: 4_correlation_heatmap.png")
    plt.close()

# --- 3. MAIN EXECUTION ---

if __name__ == "__main__":
    # Path assumes script is in 'notebooks' folder and data in 'data' folder
    data_path = '../data/amazon.csv' 
    
    df = load_and_clean_data(data_path)
    
    if df is not None:
        # Generate all plots
        plot_top_categories(df)
        plot_discount_distribution(df)
        plot_price_vs_rating(df)
        plot_correlation(df)
        
        # Calculate key insights
        avg_rating = df['rating'].mean()
        avg_discount = df['discount_percentage'].mean()
        
        print("\n--- EXECUTIVE SUMMARY ---")
        print(f"Average Product Rating: {avg_rating:.2f} / 5.0")
        print(f"Average Discount Offered: {avg_discount:.1f}%")
        print("Analysis complete. Images saved to 'images/' folder.")
