import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from recommendation import get_recommendations

# Page config
st.set_page_config(
    page_title="Career Guidance System",
    page_icon="🎓",
    layout="wide"
)

MODELS_DIR = "models"


# ✅ Load assets safely
@st.cache_resource
def load_assets():
    encoders = joblib.load(os.path.join(MODELS_DIR, "encoders.joblib"))
    scaler = joblib.load(os.path.join(MODELS_DIR, "scaler.joblib"))
    feature_cols = joblib.load(os.path.join(MODELS_DIR, "feature_cols.joblib"))

    with open(os.path.join(MODELS_DIR, "best_model.txt"), "r") as f:
        best_model_name = f.read().strip()

    model = None

    # Try Deep Learning safely
    if best_model_name == "DeepLearning":
        try:
            import tensorflow as tf
            model = tf.keras.models.load_model(os.path.join(MODELS_DIR, "DL_model.h5"))
        except Exception:
            st.warning("⚠️ DL model failed. Switching to RandomForest.")
            best_model_name = "RandomForest"
            model = joblib.load(os.path.join(MODELS_DIR, "RandomForest_model.joblib"))
    else:
        model = joblib.load(os.path.join(MODELS_DIR, f"{best_model_name}_model.joblib"))

    return encoders, scaler, feature_cols, model, best_model_name


# ✅ Load models
try:
    encoders, scaler, feature_cols, model, best_model_name = load_assets()
except Exception as e:
    st.error(f"❌ Model loading failed. Please train models first.\n\nError: {e}")
    st.stop()


# Header
st.title("🎓 Career Path Prediction & Guidance System")
st.write("---")

col1, col2 = st.columns([1, 2])

# 🔹 INPUT
with col1:
    st.subheader("Student Profile")

    inputs = {}

    for col in feature_cols:
        if col in encoders:
            options = encoders[col].classes_.tolist()
            inputs[col] = st.selectbox(col, options)
        else:
            inputs[col] = st.slider(col, 0, 10, 5)

    predict_btn = st.button("🚀 Predict Career Path")


# 🔹 OUTPUT
with col2:
    if predict_btn:

        input_df = pd.DataFrame([inputs])

        # Encode
        for col, le in encoders.items():
            if col in input_df.columns:
                try:
                    input_df[col] = le.transform(input_df[col])
                except:
                    input_df[col] = 0

        # Scale
        input_scaled = scaler.transform(input_df[feature_cols])

        # Predict
        if best_model_name == "DeepLearning":
            try:
                probs = model.predict(input_scaled)
                pred_idx = np.argmax(probs, axis=1)[0]
                confidence = np.max(probs) * 100
            except:
                st.error("❌ DL model prediction failed.")
                st.stop()
        else:
            pred_idx = model.predict(input_scaled)[0]

            if hasattr(model, "predict_proba"):
                confidence = np.max(model.predict_proba(input_scaled)) * 100
            else:
                confidence = 100.0

        # Decode
        career = encoders["Suggested Job Role"].inverse_transform([pred_idx])[0]

        # Results
        st.success(f"🎯 Predicted Career Path: **{career}**")
        st.info(f"Confidence: {confidence:.2f}%")

        # Recommendations
        recs = get_recommendations(career)

        st.subheader("📚 Recommended Learning Path")

        tab1, tab2, tab3 = st.tabs([
            "Courses & Skills",
            "Projects & Certifications",
            "Internships & Roadmap"
        ])

        with tab1:
            st.markdown("### 📘 Courses")
            for c in recs["Courses"]:
                st.write(f"- {c}")

            st.markdown("### 🛠 Skills")
            st.write(", ".join(recs["Skills"]))

        with tab2:
            st.markdown("### 💡 Projects")
            for p in recs["Projects"]:
                st.write(f"- {p}")

            st.markdown("### 📜 Certifications")
            for cert in recs["Certifications"]:
                st.write(f"- {cert}")

        with tab3:
            st.markdown("### 🏢 Internships")
            for i in recs["Internships"]:
                st.write(f"- {i}")

            st.markdown("### 🗺 Roadmap")
            for step in recs["Roadmap"]:
                st.write(f"✅ {step}")

    else:
        st.info("👈 Fill in your details and click Predict to get career guidance.")

# Footer
st.write("---")
st.markdown("<p style='text-align:center;'>Built with Streamlit & Machine Learning</p>", unsafe_allow_html=True)