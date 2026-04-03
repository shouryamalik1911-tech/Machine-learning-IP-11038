import pandas as pd
import numpy as np
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier

from preprocessing import load_and_preprocess_data


def train_ml_models(X_train, y_train, output_dir='models/'):
    os.makedirs(output_dir, exist_ok=True)

    models = {
        'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
        'LogisticRegression': LogisticRegression(max_iter=1000, random_state=42),
        'SVM': SVC(probability=True, random_state=42),
        'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42)
    }

    trained_models = {}

    for name, model in models.items():
        print(f"🚀 Training {name}...")
        model.fit(X_train, y_train)

        model_path = os.path.join(output_dir, f'{name}_model.joblib')
        joblib.dump(model, model_path)

        trained_models[name] = model
        print(f"✅ Saved {name} at {model_path}")

    return trained_models


# ✅ Optional Deep Learning (SAFE)
def train_dl_model_safe(X_train, y_train, input_dim, num_classes, output_dir='models/'):
    os.makedirs(output_dir, exist_ok=True)

    try:
        import tensorflow as tf
        from tensorflow.keras.models import Sequential # type: ignore
        from tensorflow.keras.layers import Dense, Dropout # type: ignore

        print("🧠 Training Deep Learning Model...")

        model = Sequential([
            Dense(64, input_dim=input_dim, activation='relu'),
            Dropout(0.2),
            Dense(32, activation='relu'),
            Dropout(0.2),
            Dense(num_classes, activation='softmax')
        ])

        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        model.fit(
            X_train,
            y_train,
            epochs=30,  # reduced for faster training
            batch_size=32,
            validation_split=0.1,
            verbose=1
        )

        model_path = os.path.join(output_dir, 'DL_model.h5')
        model.save(model_path)

        print(f"✅ DL Model saved at {model_path}")

        return model

    except Exception as e:
        print("⚠️ TensorFlow not working, skipping DL model:", e)
        return None


if __name__ == "__main__":
    DATA_PATH = "Dataset.csv"

    X_train, X_test, y_train, y_test, encoders, feature_cols = load_and_preprocess_data(DATA_PATH)

    # ✅ Train ML Models (MAIN PART)
    train_ml_models(X_train, y_train)

    # ✅ Train DL Model (OPTIONAL)
    num_classes = len(encoders['Suggested Job Role'].classes_)
    train_dl_model_safe(X_train, y_train, X_train.shape[1], num_classes)

    print("\n🎯 All models trained and saved successfully!")