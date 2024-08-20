
import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('bike_sharing_model.pkl', 'rb'))

st.title('Bike Sharing Demand Prediction')

season = st.selectbox('Season', [1, 2, 3, 4])  
yr=st.selectbox('Year',[0,1])
mnth=st.selectbox('Month',[1,2,3,4,5,6,7,8,9,10,11,12])
hr=st.selectbox('Hour',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
#holiday=st.selectbox('Holiday',[0,1])
weekday = st.selectbox('Weekday', [0, 1, 2, 3, 4, 5, 6])  
workingday=st.selectbox('workingday',[0,1])
weathersit = st.selectbox('Weather Situation', [1, 2, 3,4])  
temp = st.slider('Temperature', -1.0, 1.0, 0.0)
atemp = st.slider('Feels-Like Temperature', -1.0, 1.0, 0.0)
hum = st.slider('Humidity', -1.0, 1.0, 0.0)
windspeed = st.slider('Windspeed', -1.0, 1.0, 0.0)
casual=st.slider('Casual',1,100)
registered=st.slider('registered',1,100)

input_data = np.array([[season,yr,mnth,hr,weekday,workingday,weathersit,temp,atemp,hum,windspeed,casual,registered]])


prediction = model.predict(input_data)


if st.button("Predict",):
    
    st.write(f'Predicted Bike Demand: {prediction[0]}')

