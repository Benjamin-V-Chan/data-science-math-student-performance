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

def plot_heatmap(corr, output_dir):
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
    plt.close()

def main():
    input_path = os.path.join('..', 'outputs', 'cleaned_data.csv')
    output_dir = os.path.join('..', 'outputs', 'eda_plots')
    os.makedirs(output_dir, exist_ok=True)
    df = load_cleaned_data(input_path)
    desc, corr = descriptive_stats(df)
    desc.to_csv(os.path.join('..', 'outputs', 'descriptive_stats.csv'))
    corr.to_csv(os.path.join('..', 'outputs', 'correlation.csv'))
    plot_histograms(df, output_dir)
    plot_heatmap(corr, output_dir)

if __name__ == '__main__':
    main()
