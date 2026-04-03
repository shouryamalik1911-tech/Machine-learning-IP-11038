import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

def load_and_preprocess_data(file_path, output_dir='models/'):
    """
    Loads dataset, handles preprocessing, and saves encoders/scalers.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load dataset
    df = pd.read_csv(file_path)
    
    # Identify feature types
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    target_col = 'Suggested Job Role'
    
    if target_col in categorical_cols:
        categorical_cols.remove(target_col)
    
    # Store encoders for later use in Streamlit
    encoders = {}
    
    # Encode categorical features
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
        
    # Encode target
    target_le = LabelEncoder()
    df[target_col] = target_le.fit_transform(df[target_col])
    encoders[target_col] = target_le
    
    # Split features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Save the processed columns list (important for app consistency)
    feature_cols = X.columns.tolist()
    
    # Save objects
    joblib.dump(encoders, os.path.join(output_dir, 'encoders.joblib'))
    joblib.dump(scaler, os.path.join(output_dir, 'scaler.joblib'))
    joblib.dump(feature_cols, os.path.join(output_dir, 'feature_cols.joblib'))
    
    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test, encoders, feature_cols

if __name__ == "__main__":
    DATA_PATH = 'Dataset.csv'
    X_train, X_test, y_train, y_test, encoders, feature_cols = load_and_preprocess_data(DATA_PATH)
    print("Preprocessing completed.")
    print(f"X_train shape: {X_train.shape}")
    print(f"Features: {feature_cols}")