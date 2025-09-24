Delivery Time Prediction App
A web application built with Streamlit that predicts food delivery time based on several features. The app also provides interactive visualizations to help understand the impact of each feature on the final prediction.

(You should take a screenshot of your running application, name it app_screenshot.png, and place it in your project folder for the image above to display correctly.)

Features
Real-time Prediction: Get an estimated delivery time in hours and minutes based on your inputs.

Interactive UI: Use a combination of sliders and manual number inputs to set feature values.

Feature Impact Analysis: Interactive Altair charts show how changes in one feature affect the delivery time while others are held constant.

Modular Codebase: The code is cleanly separated into modules for the user interface, model handling, and plotting logic.

Technologies Used
Python: The core programming language.

Streamlit: For building and running the interactive web application.
--   Scikit-learn: For using the Random Forest Regressor model.

Pandas: For data manipulation and creating DataFrames.

NumPy: For numerical operations, especially for generating chart data.

Joblib: For loading the pre-trained .pkl model file.

Altair: For creating declarative and interactive data visualizations.

Setup and Installation
Follow these steps to get the application running on your local machine.

Prerequisites
Python 3.8 or higher

pip package manager

1. Clone the Repository
Clone this repository to your local machine.

git clone [https://github.com/your-username/delivery-time-predictor.git](https://github.com/your-username/delivery-time-predictor.git)
cd delivery-time-predictor

2. Create a Virtual Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

4. Place the Model File
Make sure your pre-trained model file, delivery_time_model.pkl, is present in the root directory of the project.

How to Run the App
Once the setup is complete, run the following command in your terminal from the project's root directory:

streamlit run app.py

The application should automatically open in a new tab in your default web browser.

File Structure
The project is organized into several files, each with a specific responsibility:

.
├── app.py                  # Main Streamlit application file (UI and orchestration)
├── model_util.py           # Handles loading the machine learning model
├── plot_util.py            # Generates the visualizations using Altair
├── delivery__time_model.pkl # The pre-trained machine learning model
├── requirements.txt        # Lists all project dependencies for installation
└── README.md               # This file

How It Works
UI Initialization: app.py starts and builds the user interface using Streamlit, including the sidebar with input widgets.

Model Loading: app.py calls the load_model() function from model_util.py to load the delivery_time_model.pkl into memory.

User Input: The user adjusts the values for distance, delivery person's age, and ratings in the sidebar.

Prediction: When the user clicks the "Predict Delivery Time" button, app.py creates a Pandas DataFrame with the current inputs and passes it to the loaded model to get a time prediction.

Visualization: app.py then calls the generate_time_vs_feature_chart() function from plot_util.py three times—once for each feature. This function generates the necessary data and creates an Altair chart, which is then returned to app.py.

Display: The final prediction and the three charts are displayed to the user on the main page.

License
This project is licensed under the MIT License.
