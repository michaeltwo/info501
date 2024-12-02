import joblib

def rescale_gui_input(df, file_path):
    df = df.copy()
    # print(f'Count of each target variable before rescaling: {df['Diagnosis'].value_counts()}')
    
    X_df = df.drop(columns=['Diagnosis'])
    y = df['Diagnosis']

    scaler = joblib.load(file_path)
    X = scaler.fit_transform(X_df)
    X_df = pd.DataFrame(X, columns=X_df.columns)
    joblib.dump(scaler, 'scaler.pkl')

    # print(f'Index check before adding Diagnosis: {X_df.index.equals(y.index)}')

    X_df = X_df.reset_index(drop=True)
    y = y.reset_index(drop=True)

    X_df['Diagnosis'] = y

  
    # After scaling
    print(f'Length of X_df after scaling: {len(X_df)}')


    print(f'Count of each target variable after rescaling: {X_df['Diagnosis'].value_counts()}')

    return X_df



