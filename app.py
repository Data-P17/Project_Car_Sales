import pandas as pd
import streamlit as st 
import plotly.express as px 

# Read the dataset's CSV file
data_car_sales = pd.read_csv('../vehicles_us.csv')
print(data_car_sales.head())
# Converting the floats and booleans to integers:
# the 1 repersent yes for four wheel drive and the 0 represents the contrary.
data_car_sales['is_4wd'] = data_car_sales['is_4wd'].fillna(0).astype(int)

#filling in missing value for car color with 'unknown'.
data_car_sales['paint_color'] = data_car_sales['paint_color'].fillna('unknown')

#Filling the Cylinders missing values compared to the type of car it is.
data_car_sales['cylinders'] = data_car_sales[['cylinders', 'type']].groupby('type').transform(lambda x:x.fillna(x.median()))

#Filling in the Model_year missing values compared to the type of car it is. 
data_car_sales['model_year'] = data_car_sales[['model_year', 'type']].groupby('type').transform(lambda x:x.fillna(x.median()))

#Filling in the Odometer missing values compared to the year.
data_car_sales['odometer'] = data_car_sales[['odometer', 'model_year']].groupby('model_year').transform(lambda x:x.fillna(x.median()))

# display the dataframe with Streamlit 
# creating a df header
st.header("Car Sales")
#diplay the df with streamlit
st.dataframe(data_car_sales)
# Constants for configurations and conditions
CONDITION_GOOD = 'good'
MILEAGE_THRESHOLD = 30000
NBINS = 5
PLOT_TITLE = "Good Condition Cars with Low Mileage"
CHECKBOX_LABEL = 'Color by Condition'

# Define the checkbox for selecting color by condition
color_by_condition = st.checkbox(CHECKBOX_LABEL, value=True)

# Filter the dataset based on condition and mileage
filtered_dcs = data_car_sales[(data_car_sales['condition'] == CONDITION_GOOD) & 
                              (data_car_sales['odometer'] <= MILEAGE_THRESHOLD)]

# Create the histogram using Plotly Express
fig_hist = px.histogram(filtered_dcs, x="odometer", nbins=NBINS)

# Set the plot header and display the plot
st.header("Good Condition Cars with Low Mileage")
st.plotly_chart(fig_hist)
#Scatter plot of Car Mileage vs. Years
fig_cmvy = px.scatter(data_car_sales, x="model_year", y="odometer", color="type", hover_data=["model", "paint_color"], title="Car Mileage vs Year")

st.plotly_chart(fig_cmvy)
# Histogram of Condition vs Model_year
# The relationship between condition and model_year
fig_cmy = px.histogram(data_car_sales, x='model_year', color='condition')
st.header('Histogram of Condition vs Model_Year')
st.plotly_chart(fig_cmy)
#volin plot of mileage by make
fig_vmm = px.violin(data_car_sales, x='model', y='odometer', title="Mileage Distribution by Make", box=True, points="all", color='model')

fig_vmm.update_layout(width=900, height=600)

st.plotly_chart(fig_vmm)