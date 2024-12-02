import joblib
import pandas as pd
from preprocessing import clean, split_external_data

def rescale_gui_input(df, file_path):
    df = df.copy()
    # print(f'Count of each target variable before rescaling: {df['Diagnosis'].value_counts()}')
    
    X_df = df.drop(columns=['Diagnosis'])
    y = df['Diagnosis']

    scaler = joblib.load(file_path)
    X = scaler.fit_transform(X_df)
    X_df = pd.DataFrame(X, columns=X_df.columns)

    # print(f'Index check before adding Diagnosis: {X_df.index.equals(y.index)}')

    X_df = X_df.reset_index(drop=True)
    y = y.reset_index(drop=True)

    X_df['Diagnosis'] = y

  
    # After scaling
    print(f'Length of X_df after scaling: {len(X_df)}')


    print(f'Count of each target variable after rescaling: {X_df['Diagnosis'].value_counts()}')

    return X_df


if __name__ == '__main__':
    
    df = pd.read_csv(r'G:\My Drive\School\Current Classes\SSIE 548 - Healtchare Data Science\Project\Data\sbcdata.csv')
    datasets = split_external_data(df)
    df = datasets[0]
    df = clean(df)
    test = rescale_gui_input(df,r'scaler.pkl')

