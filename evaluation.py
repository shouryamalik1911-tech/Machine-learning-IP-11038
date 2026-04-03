import joblib
import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from preprocessing import load_and_preprocess_data


def evaluate_models(X_test, y_test, output_dir='models/'):
    os.makedirs(output_dir, exist_ok=True)

    metrics = []

    # ✅ Evaluate ML models
    ml_models = ['RandomForest', 'LogisticRegression', 'SVM', 'XGBoost']

    for name in ml_models:
        model_path = os.path.join(output_dir, f'{name}_model.joblib')

        if os.path.exists(model_path):
            model = joblib.load(model_path)
            y_pred = model.predict(X_test)

            metrics.append({
                'Model': name,
                'Accuracy': accuracy_score(y_test, y_pred),
                'Precision': precision_score(y_test, y_pred, average='weighted'),
                'Recall': recall_score(y_test, y_pred, average='weighted'),
                'F1': f1_score(y_test, y_pred, average='weighted')
            })
        else:
            print(f"{name} model not found at {model_path}")

    # ✅ Optional Deep Learning model (SAFE)
    dl_model_path = os.path.join(output_dir, 'DL_model.h5')

    if os.path.exists(dl_model_path):
        try:
            import tensorflow as tf
            model = tf.keras.models.load_model(dl_model_path)

            y_prob = model.predict(X_test)
            y_pred = np.argmax(y_prob, axis=1)

            metrics.append({
                'Model': 'DeepLearning',
                'Accuracy': accuracy_score(y_test, y_pred),
                'Precision': precision_score(y_test, y_pred, average='weighted'),
                'Recall': recall_score(y_test, y_pred, average='weighted'),
                'F1': f1_score(y_test, y_pred, average='weighted')
            })

        except Exception as e:
            print("⚠️ TensorFlow error, skipping DL model:", e)

    # ✅ Convert to DataFrame
    if len(metrics) == 0:
        print("❌ No models found. Train models first.")
        return None

    metrics_df = pd.DataFrame(metrics)

    print("\n📊 Model Evaluation Summary:")
    print(metrics_df)

    # ✅ Select best model
    best_model_name = metrics_df.loc[metrics_df['Accuracy'].idxmax(), 'Model']
    print(f"\n🏆 Best Model: {best_model_name}")

    # ✅ Save best model
    with open(os.path.join(output_dir, 'best_model.txt'), 'w') as f:
        f.write(best_model_name)

    return metrics_df


if __name__ == "__main__":
    DATA_PATH = "Dataset.csv"

    X_train, X_test, y_train, y_test, encoders, feature_cols = load_and_preprocess_data(DATA_PATH)

    evaluate_models(X_test, y_test)