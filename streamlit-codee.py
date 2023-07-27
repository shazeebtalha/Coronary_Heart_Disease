#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
with open('Coronary_Heart_Disease.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to make predictions using the loaded model
def make_prediction(age, sex, is_smoking, diabetes, totChol, BMI, heartRate):
    # Convert categorical variables to numeric using binary encoding
    is_smoking_encoded = 1 if is_smoking == 'Smoker' else 0
    sex_encoded = 1 if sex == 'Male' else 0
    diabetes_encoded = 1 if diabetes == 'Yes' else 0

    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex_encoded],
        'is_smoking': [is_smoking_encoded],
        'diabetes': [diabetes_encoded],
        'totChol': [totChol],
        'BMI': [BMI],
        'heartRate': [heartRate]
    })

    prediction = model.predict(input_data)
    return prediction[0]

# Set page title and layout
st.set_page_config(page_title='Coronary Heart Disease Prediction', layout='wide')

# Custom CSS for styling
custom_css = """
<style>
.stApp {
    background-color: #007c80; /* Dark Olive Green */
}
.stButton button {
    background-color: #3366cc;
    color: white;
    border: 1px solid #3366cc;
    border-radius: 5px;
}
.stButton button:hover {
    background-color: #1c4b82;
}
.stTextInput input {
    border-radius: 5px;
}
.stHeader {
    text-align: center;
    font-size: 24px;
    color: #444;
}
.stContainer {
    background-color: white;
    padding: 1rem;
    border-radius: 10px;
}
/* Custom CSS for age input */
.stAgeInput input[type="number"] {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 40px;
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 0.5rem 1rem;
    font-size: 16px;
    outline: none;
    transition: border-color 0.3s ease;
}

.stAgeInput input[type="number"]:focus {
    border-color: #3366cc;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Create the app using Streamlit
def main():
    # Title banner
    st.subheader('Coronary Heart Disease Prediction')

    # Add header for patient information
    st.subheader('Enter patient information:')
    st.write('Use the form below to enter patient information and predict the presence of Coronary Heart Disease.')

    # Add patient information inputs with custom styling using 'columns'
    col1, col2 = st.columns(2)
    with col1:
        # Explicitly set numerical arguments as float
        age = st.number_input('Age', min_value=1, max_value=100, value=30)
        sex = st.selectbox('Gender', ('Male', 'Female'))
        is_smoking = st.radio('Smoking status', ('Smoker', 'Non-Smoker'))
    with col2:
        diabetes = st.radio('Diabetes status', ('Yes', 'No'))
        totChol = st.number_input('Total Cholesterol', min_value=0.0, value=200.0)
        # Set default float values for BMI and heartRate
        BMI = st.number_input('BMI', min_value=0.0, value=25.0, step=0.1)
        heartRate = st.number_input('Heart Rate', min_value=0.0, value=75.0, step=1.0)

    # Add prediction button with custom styling
    if st.button('Predict', key='predict_button', help='Click to make the prediction'):
        # Show loading spinner while prediction is being calculated
        with st.spinner('Calculating...'):
            prediction = make_prediction(age, sex, is_smoking, diabetes, totChol, BMI, heartRate)

            # Add prediction result in a styled container
            with st.container():
                st.subheader('Prediction:')
                if prediction == 0:
                    st.error('Coronary Heart Disease: No')
                else:
                    st.success('Coronary Heart Disease: Yes')

                # Show an image based on the prediction with styled image
                if prediction == 0:
                    st.image('no_disease.png', width=200, caption='No Coronary Heart Disease')
                else:
                    st.image('disease.png', width=200, caption='Coronary Heart Disease Present')

if __name__ == '__main__':
    main()


# In[ ]:




