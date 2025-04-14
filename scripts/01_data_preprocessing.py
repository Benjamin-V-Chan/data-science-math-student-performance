import pandas as pd
import os

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna(method='ffill', inplace=True)
    cat_cols = df.select_dtypes(include=['object']).columns
    return pd.get_dummies(df, columns=cat_cols, drop_first=True)

def main():
    input_path = os.path.join('..', 'data', 'Math-Students.csv')
    output_path = os.path.join('..', 'outputs', 'cleaned_data.csv')
    df = load_data(input_path)
    df_clean = preprocess_data(df)
    df_clean.to_csv(output_path, index=False)

if __name__ == '__main__':
    main()
