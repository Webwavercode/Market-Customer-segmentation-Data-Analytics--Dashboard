import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.drop_duplicates()
    return df

def scale_features(df, features):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[features])
    return scaled
