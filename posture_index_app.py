# imports
import numpy as np
import pandas as pd
import joblib
import streamlit as st
import xgboost as xgb

# Set the title
st.title('Clinical Measure for RSJC')

# Set the subheader
st.subheader('*This app predicts the amount of movement in the ankle foot complex*')

# Put a line to separate
st.write('***')

# Put the sidebar
st.sidebar.header('User Input Parameters') # user input

# Get the parameters
def get_user_input():
	neutral_calcaneus = st.sidebar.number_input('Neutral Calcaneus')
	neutral_shank = st.sidebar.number_input('Neutral Shank')
	neutral_cal_shank = neutral_calcaneus - neutral_shank
	relaxed_calcaneus = st.sidebar.number_input('Relaxed Calcaneus')
	relaxed_shank = st.sidebar.number_input('Relaxed Shank')
	relaxed_cal_shank = relaxed_calcaneus - relaxed_shank
	rotation = st.sidebar.number_input('Rotation')

	# Calculated variable
	neutral_relaxed_dif = relaxed_cal_shank - neutral_cal_shank


	features = {'Calcâneo Neutro': neutral_calcaneus,
	'Perna Neutro': neutral_shank,
	'Rotação (°)': rotation,
	'Calcâneo Relaxado': relaxed_calcaneus,
	'DIFERENÇA NEUTRO - RELAXADO': neutral_relaxed_dif}

	data = pd.DataFrame(features, index =[0])
	return data

# Transform the raw data
user_input_df = get_user_input()

# Visualize the data
st.subheader('See Inputed Parameters')
st.write(user_input_df)

# Define the func that predict
model = joblib.load('XG_boost.joblib')
def prediction():
	predictions = model.predict(user_input_df)
	return predictions

# Let's show the results
result = prediction()

# Calculate a new measure, the ratio
# ratio_raw = neutral_relaxed_dif/rotation

# Transform these variables
index = pd.Series(data = result, name = 'Posture Index')

# ratio = pd.Series(data = ratio_raw, name = 'Posture Ratio')

# Put into a table
# table = pd.concat([index, ratio])

# Another line
st.write('***')

st.subheader('See Results')
st.write(index)

st.write('***')

st.write('Explanation: The higher the index, more pronated are the Rearfoot-Shank Joint Complex is')

st.write('***')
