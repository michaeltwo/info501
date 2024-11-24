#%% LOAD DATA

import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def split_external_data(df):
    groups = df.groupby(by = 'Center')
    df_uml = groups.get_group('Leipzig')
    df_umg = groups.get_group('Greifswald')

    return df_umg, df_uml

def undersample_data(df):
    groups = df.groupby(by = 'Diagnosis')
    sep = groups.get_group(1)
    ctrl = groups.get_group(0)

    rows = sep.shape[0]
    ctrl = ctrl.sample(n=rows, random_state=42)

    df = pd.concat([ctrl, sep], axis=0, ignore_index=True)
    df = df.copy()
    return df


def preprocess(df, undersample = False ):
    import pandas as pd
    df = df.copy()

    #Remove CBC taken in ICU
    # df = df[df['SecToIcu'] > 0]

    # Make cetgoricicalel to numeric
    df['Sex'] = pd.factorize(df['Sex'])[0]
    df['Diagnosis'] = pd.factorize(df['Diagnosis'])[0]

    # Remove SIRS diagnosis
    df['Diagnosis'] = df['Diagnosis'][df['Diagnosis'] !=2]

    # Drop extraneous columns
    df = df.drop(columns=['Id','Center', 'Set', 'Sender', 'Episode', 'Time','TargetIcu', 'SecToIcu','PCT'])
    df = df.drop_duplicates()

    if undersample:
        df = undersample_data(df)
    #split into crp and no crp (CRP is in about half of the sepsis cases)
    df_crp = df
    df_no_crp = df_crp.drop(columns=['CRP'])

    df_crp.dropna(inplace=True)
    df_no_crp.dropna(inplace=True)

    return df, df_crp, df_no_crp

def clean_normalize_balance_data(df, undersample=True):

    if undersample:
        df = undersample_data(df)

    df_without_diagnosis = df.drop(columns=['Diagnosis'])

    z_scores = np.abs(zscore(df_without_diagnosis))
    df_no_outliers = df[(z_scores < 3).all(axis=1)]  # Keeps only rows where all values' Z-score < 3

    scaler = MinMaxScaler()
    df_no_outliers_scaled = pd.DataFrame(scaler.fit_transform(df_no_outliers.drop(columns=['Diagnosis'])), columns=df_no_outliers.columns[:-1])

    df_no_outliers_scaled['Diagnosis'] = df_no_outliers['Diagnosis'].reset_index(drop=True)

    return df_no_outliers_scaled

