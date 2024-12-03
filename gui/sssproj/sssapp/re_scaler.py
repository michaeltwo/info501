import joblib
import pandas as pd

def rescale_gui_input(df, file_path):
    df = df.copy()
    scaler = joblib.load(file_path)
    X = scaler.fit_transform(df)
    X_df = pd.DataFrame(X, columns=df.columns)

    return X_df


