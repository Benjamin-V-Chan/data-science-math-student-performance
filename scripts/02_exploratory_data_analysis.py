import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_cleaned_data(filepath):
    return pd.read_csv(filepath)

def descriptive_stats(df):
    return df.describe(), df.corr()

def plot_histograms(df, output_dir):
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        df[col].hist(bins=30)
        plt.title(f'Histogram of {col}')
        plt.savefig(os.path.join(output_dir, f'hist_{col}.png'))
        plt.close()

