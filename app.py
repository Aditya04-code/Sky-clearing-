from operator import index
import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image
from sklearn.preprocessing import MinMaxScaler
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
# importing the model
loaded_model = open("best.pkl","rb")
classifier = pickle.load(loaded_model)
st.sidebar.header('User input Parameters')
st.markdown("<h1 style='color: black;'>Skyclearance Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='color: black;'>This app predicts the clear sky based on various parametrs</h6>", unsafe_allow_html=True)
# st.write("""


# This app predicts the clear sky based on various parametrs





# """)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://source.unsplash.com/vzGQlsZ-ZhY");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)         

def prediction(input_data):
    input_data_as_np = np.asarray(input_data)
    input_data_reshape = input_data_as_np.reshape(1,-1)
    prediction = classifier.predict(input_data_reshape)
    return prediction


def user_interface():
    #elevation = st.sidebar.slider('ELEVATION', 3,3,3)
    #latitude = st.sidebar.slider('LATITUDE', min_value=40, max_value=40)
    #longitude = st.sidebar.slider('LONGITUDE', min_value=-73, max_value=-73)
    temp = st.sidebar.slider('HOURLY DRY BULB TEMPF', min_value=0, max_value=102)
    wet_temp = st.sidebar.slider('HOURLY WETBULBTEMPF', min_value=-1, max_value=85)
    dew_temp = st.sidebar.slider('HOURLY DewPoint TempF', min_value=-19, max_value=84)
    humidity = st.sidebar.slider('HOURLY Relative Humidity', min_value=0, max_value=100)
    wind_speed = st.sidebar.slider('HOURLY WindSpeed', min_value=0, max_value=53)
    wind_direction = st.sidebar.slider('HOURLY WindDirection', min_value=0, max_value=360)
    pressure = st.sidebar.slider('HOURLY Station Pressure', min_value=0, max_value=30)
    sunrise = st.sidebar.slider('DAILY Sunrise', min_value=423, max_value=719)
    sunset = st.sidebar.slider('DAILY Sunset', min_value=1628, max_value=1930)
    # max_pressure_date = st.sidebar.slider('MonthlyMaxSeaLevelPressureDate',-9999.0,-9999.0)
    # max_pressure_time = st.sidebar.slider('MonthlyMaxSeaLevelPressureTime',-9999.0,-9999.0)
    # min_pressure_date = st.sidebar.slider('MonthlyMinSeaLevelPressureDate',-9999.0,-9999.0)
    #min_pressure_time = st.sidebar.slider('MonthlyMinSeaLevelPressureTime',0,14)
    data_dict = {
    'ELEVATION':3 ,
    'LATITUDE':-40 ,
    'LONGITUDE':-73 ,
    'HOURLYDRYBULBTEMP F': temp,
    'HOURLYWETBULBTEMPF':wet_temp ,
    'HOURLYDewPointTempF':dew_temp,
    'HOURLYRelativeHumidity':humidity,
    'HOURLYWindSpeed':wind_speed ,
    'HOURLYWindDirection':wind_direction ,
    'HOURLYStationPressure':pressure ,
    'DAILYSunrise':sunrise,
    'DAILYSunset':sunset ,
    'MonthlyMaxSeaLevelPressureDate': -9999.0,
    'MonthlyMaxSeaLevelPressureTime':-9999.0 ,
    'MonthlyMinSeaLevelPressureDate':-9999.0 ,
    'MonthlyMinSeaLevelPressureTime':-9999.0 
    }
    features = pd.DataFrame(data_dict,index=[0])
    return features

df = user_interface()
st.markdown("<h3 style='color: black;'>User input parameters</h3>", unsafe_allow_html=True)
#st.subheader("User input parameters")
st.write(df)
st.markdown("<h3 style='color: black ;'>Predictions</h3>", unsafe_allow_html=True)
st.subheader("predictions")
st.write(prediction(df))
st.write()
    
