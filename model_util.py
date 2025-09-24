# model_util.py

import joblib
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np

MODEL_FILENAME = 'delivery__time_model.pkl'

def load_model(model_path=MODEL_FILENAME):
    """
    Loads the machine learning model from the specified file path.

    Args:
        model_path (str): The path to the model file.

    Returns:
        The loaded model object.
    
    Raises:
        FileNotFoundError: If the model file does not exist at the given path.
    """
    if not os.path.exists(model_path):
        # If the model file is missing, the app cannot function.
        # Raising an error is the correct action.
        raise FileNotFoundError(
            f"Error: The model file '{model_path}' was not found. "
            "Please ensure the pre-trained model is in the same directory as your app."
        )
    
    print(f"Loading existing model from {model_path}...")
    model = joblib.load(model_path)
    return model

def _create_new_model():
    """
    (For development/setup only)
    Trains a new model on sample data and saves it. This function is not
    called by the Streamlit app but can be run manually.
    """
    print("--- Running Model Training (Development Only) ---")
    # Create a realistic dummy dataset
    np.random.seed(42)
    num_samples = 500
    data = {
        'Delivery_person_Age': np.random.randint(20, 50, size=num_samples),
        'Delivery_person_Ratings': np.round(np.random.uniform(2.5, 4.9, size=num_samples), 2),
        'distance': np.round(np.random.uniform(1, 25, size=num_samples), 2)
    }
    df = pd.DataFrame(data)

    # Create a target variable: Time taken in minutes
    df['Time_taken(min)'] = (
        15
        + df['distance'] * 2.5
        - df['Delivery_person_Ratings'] * 3
        + (df['Delivery_person_Age'] - 20) * 0.2
        + np.random.normal(0, 5, size=num_samples)
    )
    df['Time_taken(min)'] = df['Time_taken(min)'].apply(lambda x: max(10, x))

    # Define features and target
    feature_names = ['Delivery_person_Ratings', 'Delivery_person_Age', 'distance']
    X = df[feature_names]
    y = df['Time_taken(min)']

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save the model
    joblib.dump(model, MODEL_FILENAME)
    print(f"✅ Model trained and saved as '{MODEL_FILENAME}'")
    
    return model

if __name__ == '__main__':
    # This block allows you to run `python model_util.py` from your 
    # terminal to generate a new model file if needed.
    _create_new_model()