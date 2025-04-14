import os
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def feature_engineer(df):
    if 'G1' in df.columns and 'G2' in df.columns:
        df['avg_G1_G2'] = (df['G1'] + df['G2']) / 2
    if 'famrel' in df.columns:
        df['high_family_support'] = (df['famrel'] > 3).astype(int)
    return df

def main():
    input_path = os.path.join('..', 'outputs', 'cleaned_data.csv')
    output_path = os.path.join('..', 'outputs', 'model_data.csv')
    df = load_data(input_path)
    df_fe = feature_engineer(df)
    df_fe.to_csv(output_path, index=False)

if __name__ == '__main__':
    main()
