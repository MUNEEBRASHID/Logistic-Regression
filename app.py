import pickle
import streamlit as st
import pandas as pd
from PIL import Image

# Load the trained model
model = pickle.load(open('./model.sav', 'rb'))

# Page Title and Sidebar
st.title('Advertisement Prediction App')
st.sidebar.header('User Data')

# Load an image for the header
image = Image.open('ad.jpg')
st.image(image, caption='Advertisement Image', use_column_width=True)

# Function to collect user input
def user_report():
    time_spent = st.sidebar.slider('Time Spent On Site (minutes)', 0.0, 100.0, 0.0, 0.5)
    age = st.sidebar.slider('Age', 0, 100, 25)
    income = st.sidebar.slider('Income', 0, 100000, 50000)
    internet_usage = st.sidebar.slider('Internet Usage (minutes)', 0, 300, 150)
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])

    user_data_report = {
        'Daily Time Spent on Site': time_spent,
        'Age': age,
        'Area Income': income,
        'Daily Internet Usage': internet_usage,
        'Male': 1 if gender == 'Male' else 0  # Encode gender
    }
    return pd.DataFrame([user_data_report])

# Display User Input
user_data = user_report()
st.header('User Data')
st.write(user_data)

# Predict Advertisement Click
if st.button('Predict Advertisement Click'):
    prediction = model.predict(user_data)
    st.subheader('Predicted Advertisement Click')
    if prediction[0] == 1:
        st.success('User will click on the ad!')
    else:
        st.error('User will not click on the ad.')

# Feedback Section
st.sidebar.header('Feedback')
feedback = st.sidebar.radio('Was the prediction accurate?', ('Yes', 'No'))
if feedback == 'Yes':
    st.sidebar.success('Thank you for the feedback!')
else:
    st.sidebar.warning('Sorry to hear that. We will improve.')

# Footer
st.sidebar.markdown('---')
st.sidebar.markdown('Made with ❤️ by MUNEEB')