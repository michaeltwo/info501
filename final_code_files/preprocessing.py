#%% PACKAGE IMPORTS
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
import joblib
import seaborn as sns

#%% PREPROCESSING HELPER FUNCTIONS
def split_external_data(df):
    """
    df_uml = training data
    df_umg = external validation set
    note: external validation set is different from the test data from train test split
    """
    groups = df.groupby(by = 'Center')
    df_uml = groups.get_group('Leipzig')
    df_umg = groups.get_group('Greifswald')

    return df_uml, df_umg

def undersample_data(df):
    print(f'Count of each target variable before undersampling: {df['Diagnosis'].value_counts()}')

    groups = df.groupby(by = 'Diagnosis')
    sep = groups.get_group(1)
    ctrl = groups.get_group(0)

    rows = sep.shape[0]
    ctrl = ctrl.sample(n=rows, random_state=42)

    df = pd.concat([ctrl, sep], axis=0, ignore_index=True)
    df = df.copy()
    print(f'Count of each target variable after undersampling: {df['Diagnosis'].value_counts()}')

    return df

def rescale_dataset(df):
    df = df.copy()
    # print(f'Count of each target variable before rescaling: {df['Diagnosis'].value_counts()}')
    
    X_df = df.drop(columns=['Diagnosis'])
    y = df['Diagnosis']

    scaler = MinMaxScaler()
    X = scaler.fit_transform(X_df)
    X_df = pd.DataFrame(X, columns=X_df.columns)
    # joblib.dump(scaler, 'scaler.pkl')

    # print(f'Index check before adding Diagnosis: {X_df.index.equals(y.index)}')

    X_df = X_df.reset_index(drop=True)
    y = y.reset_index(drop=True)

    X_df['Diagnosis'] = y

  
    # After scaling
    print(f'Length of X_df after scaling: {len(X_df)}')


    print(f'Count of each target variable after rescaling: {X_df['Diagnosis'].value_counts()}')

    return X_df

def remove_outliers(df):
    #remove target
    X_df = df.drop(columns=['Diagnosis'])

    # get iqr
    q1 = X_df.quantile(0.25)
    q3 = X_df.quantile(0.75)
    iqr = q3 - q1

    # get bounds for dataset
    low_bound = q1 - 1.5 * iqr
    upp_bound = q3 + 1.5 * iqr

    #get index of non outliers
    non_outlier_boolean = ((X_df >= low_bound) & (X_df <= upp_bound)).all(axis=1)
    non_outlier_index = non_outlier_boolean[non_outlier_boolean].index

    # extract non outliers
    df = df.loc[non_outlier_index]
    print(f'Count of each target variable after outlier removal: {df['Diagnosis'].value_counts()}')

    return df

def clean(df):
    df = df.copy()

    # numeric encoding
    df['Sex'] = pd.factorize(df['Sex'])[0]
    df['Diagnosis'] = pd.factorize(df['Diagnosis'])[0]

    # Remove SIRS diagnosis
    df['Diagnosis'] = df['Diagnosis'][df['Diagnosis'] !=2]
    print(f'Count of each target variable before preprop: {df['Diagnosis'].value_counts()}')

    # Drop extraneous columns
    df = df.drop(columns=['Id','Center', 'Set', 'Sender', 'Episode', 'Time','TargetIcu', 'SecToIcu','PCT', 'CRP'])

    # remove duplicates and NA
    df = df.drop_duplicates()
    df.dropna(inplace=True)
    print(f'Count of each target variable after dropping na and duplicates: {df['Diagnosis'].value_counts()}')

    
    return df

#%% MAIN PREPROCESSING FUNCTION
def preprocess(df, save_csv = False):
    df = df.copy()
    datasets = split_external_data(df)

    preprops = []
    for df in datasets:
        df = clean(df)
        df = remove_outliers(df)
        df = rescale_dataset(df)
        df = undersample_data(df)
        preprops.append(df)

    df_uml = preprops[0]
    df_umg = preprops[1]
    # Save preprocessed data if desired
    if save_csv:
        df_uml.to_csv('sbcdata_preprocessed_training.csv', index=False)
        df_umg.to_csv('sbcdata_preprocessed_external_val.csv', index=False)

    preprops = tuple(preprops)
    return preprops


if __name__ == "__main__":
    file_path = r'G:\My Drive\School\Current Classes\SSIE 548 - Healtchare Data Science\Project\Data\sbcdata.csv'
    df = pd.read_csv(file_path)

    # to save dfs set save_csv to true
    df_uml, df_umg = preprocess(df, save_csv=False)