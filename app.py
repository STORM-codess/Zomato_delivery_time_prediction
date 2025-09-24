# app.py

import streamlit as st
import pandas as pd
import numpy as np
from model_util import load_model
from plot_util import generate_time_vs_feature_chart

# --- Page Configuration ---
st.set_page_config(
    page_title="Delivery Time Predictor",
    page_icon="🏍️",
    layout="centered"
)

# --- Load Model ---
model = load_model()

# --- Initialize Session State ---
if 'distance' not in st.session_state:
    st.session_state.distance = 10.0
if 'ratings' not in st.session_state:
    st.session_state.ratings = 4.5
if 'age' not in st.session_state:
    st.session_state.age = 25

# --- UI Elements ---
st.title("🏍️ Delivery Time Prediction")
st.write("Enter delivery details to get an estimated time of arrival.")
st.markdown("---")

# --- Sidebar for Inputs ---
with st.sidebar:
    st.header("Delivery Features")
    st.write("Adjust with the slider or type the value directly.")
    st.markdown("---")

    st.write("**Distance (in km)**")
    c1, c2 = st.columns([3, 2])
    with c1:
        st.session_state.distance = st.slider("dist", 0.1, 50.0, st.session_state.distance, 0.1, label_visibility="collapsed")
    with c2:
        st.session_state.distance = st.number_input("dist_num", 0.1, 50.0, st.session_state.distance, 0.1, format="%.1f", label_visibility="collapsed")

    st.write("**Delivery Person Ratings**")
    c1, c2 = st.columns([3, 2])
    with c1:
        st.session_state.ratings = st.slider("rate", 1.0, 5.0, st.session_state.ratings, 0.1, label_visibility="collapsed")
    with c2:
        st.session_state.ratings = st.number_input("rate_num", 1.0, 5.0, st.session_state.ratings, 0.1, format="%.1f", label_visibility="collapsed")

    st.write("**Delivery Person Age**")
    c1, c2 = st.columns([3, 2])
    with c1:
        st.session_state.age = st.slider("age", 18, 60, st.session_state.age, 1, label_visibility="collapsed")
    with c2:
        st.session_state.age = st.number_input("age_num", 18, 60, st.session_state.age, 1, label_visibility="collapsed")


# --- Prediction and Visualization ---
if st.button("Predict Delivery Time"):
    try:
        feature_names = ['Delivery_person_Ratings', 'Delivery_person_Age', 'distance']
        
        current_inputs = {
            'Delivery_person_Ratings': st.session_state.ratings,
            'Delivery_person_Age': st.session_state.age,
            'distance': st.session_state.distance
        }
        
        user_input_df = pd.DataFrame([current_inputs])[feature_names]
        predicted_time = model.predict(user_input_df)[0]
        
        hours, minutes = divmod(predicted_time, 60)
        st.subheader(f"Estimated Delivery Time: {int(hours)} hr {int(round(minutes))} min")
        
        st.markdown("---")
        st.header("📊 Feature Impact Visualizations")

        tab1, tab2, tab3 = st.tabs(["Distance vs. Time", "Rating vs. Time", "Age vs. Time"])

        with tab1:
            chart = generate_time_vs_feature_chart(
                model=model,
                feature_names=feature_names,
                current_inputs=current_inputs,
                feature_to_vary='distance',
                feature_range=np.linspace(1, 50, 100),
                title='Time vs. Distance',
                x_axis_title='Distance (km)'
            )
            st.altair_chart(chart, use_container_width=True)

        with tab2:
            chart = generate_time_vs_feature_chart(
                model=model,
                feature_names=feature_names,
                current_inputs=current_inputs,
                feature_to_vary='Delivery_person_Ratings',
                feature_range=np.linspace(1, 5, 100),
                title='Time vs. Rating',
                x_axis_title='Delivery Person Rating'
            )
            st.altair_chart(chart, use_container_width=True)

        with tab3:
            chart = generate_time_vs_feature_chart(
                model=model,
                feature_names=feature_names,
                current_inputs=current_inputs,
                feature_to_vary='Delivery_person_Age',
                feature_range=np.arange(18, 61),
                title='Time vs. Age',
                x_axis_title='Delivery Person Age'
            )
            st.altair_chart(chart, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("---")