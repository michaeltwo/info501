import joblib
import pandas as pd
from preprocessing import clean, split_external_data

def rescale_gui_input(df, file_path):
    df = df.copy()
    scaler = joblib.load(file_path)
    X = scaler.fit_transform(X_df)
    X_df = pd.DataFrame(X, columns=X_df.columns)

    return X_df


if __name__ == '__main__':
    
    df = pd.read_csv(r'G:\My Drive\School\Current Classes\SSIE 548 - Healtchare Data Science\Project\Data\sbcdata.csv')
    datasets = split_external_data(df)
    df = datasets[0]
    df = clean(df)
    test = rescale_gui_input(df,r'scaler.pkl')

