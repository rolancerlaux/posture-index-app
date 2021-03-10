# imports
import numpy as np
import pandas as pd
import streamlit as st

# Set the title
st.title('Clinical Measure for RSJC')

# Set the subheader
st.subheader('*This app predicts the amount of movement in the ankle foot complex*')

# Put a line to separate
st.write('***')

# Put the sidebar
st.sidebar.header('User Input Parameters') # user input

# Get the user parameters
neutral_calcaneus = st.sidebar.number_input('Neutral Calcaneus')
neutral_shank = st.sidebar.number_input('Neutral Shank')

# Calculate the first feature
neutral_cal_shank = neutral_calcaneus - neutral_shank
relaxed_calcaneus = st.sidebar.number_input('Relaxed Calcaneus')
relaxed_shank = st.sidebar.number_input('Relaxed Shank')

# Calculate the second feature
relaxed_cal_shank = relaxed_calcaneus - relaxed_shank
rotation = st.sidebar.number_input('Rotation')

# Calculate the difference
neutral_relaxed_dif = relaxed_cal_shank - neutral_cal_shank

def get_user_input():
	features = {'Calcâneo Neutro': neutral_calcaneus,
	'Perna Neutro': neutral_shank,
	'Rotação (°)': rotation,
	'Calcâneo Relaxado': relaxed_calcaneus,
	'DIFERENÇA NEUTRO - RELAXADO': neutral_relaxed_dif}

	data = pd.DataFrame(features, index =[0])
	return data

# Transform the raw data
user_input_df = get_user_input()

# Visualize the inputed parameters
st.subheader('See Inputed Parameters')
st.write(user_input_df)

# Let's calculate the results
result = (neutral_relaxed_dif + rotation)/2

# Calculate a new measure, the ratio (EV/TIR)
def ratio():
	try:
		return neutral_relaxed_dif/rotation
	except ZeroDivisionError:
		return 0
	
# Calculate the ratio
ratio_raw = ratio()

# Transform these variables
index = pd.Series(data = result, name = 'Posture Index')

ratio = pd.Series(data = ratio_raw, name = 'Posture Ratio')

# Put into a table
table = pd.concat([index, ratio],axis=1)

# Another line
st.write('***')

st.subheader('See Results')
st.write(table)

st.write('***')

# Explanation
st.write('The higher the index, more pronated the Rearfoot-Shank Joint Complex is')
st.write('The Posture Ratio indicates the relative axis of the subtalar joint')

st.write('***')
