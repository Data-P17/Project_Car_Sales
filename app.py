#Project Car Sales

import pandas as pd
import streamlit as st 
import plotly.express as px 

# Read the dataset's CSV file
data_car_sales = pd.read_csv(r'/Data_P Github Repo/Project_Car_Sales/vehicles_us.csv')
print(data_car_sales.head())

# display the dataframe with Streamlit 
# creating a df header
st.header("Car Sales")
#display the df with streamlit
st.dataframe(data_car_sales)


# plotlyexpress histogram for vehicles that in good condition with low mileages
filtered_dcs= data_car_sales[(data_car_sales['condition'] == 'good') & (data_car_sales['odometer'] <= 30000 )]
fig_hist = px.histogram(filtered_dcs, x="odometer", nbins=5, title= "Good Condition Cars with Low Mileage")

fig_hist.show()

# histogram that shows the count of cars by their types
fig_hist2 = px.histogram(data_car_sales, x='type', title="Count of Cars By Vehicle Tpye")
fig_hist2.show()

#Scatter plot of Car Mileage vs. Years
fig_cmvy = px.scatter(data_car_sales, x="model_year", y="odometer", color="type", hover_data=["model", "paint_color"], title="Car Mileage vs Year")

fig_cmvy.show()

# Histogram of Condition vs Model_year
# The relationship between condition and model_year
fig_cmy = px.histogram(data_car_sales, x='model_year', color='condition')
st.header('Histogram of Condition vs Model_Year')
st.plotly_chart(fig_cmy)

# add a checkbox
# Create the checkbox widget to control whether to color by 'condition'
color_by_condition = st.checkbox('Color by Condition', value=True)

# Create the histogram based on the checkbox state
if color_by_condition:
    # Histogram with color by 'condition'
    fig_cmy = px.histogram(data_car_sales, x='model_year', color='condition', title="Histogram of Condition vs Model Year")
else:
    # Histogram without color by 'condition'
    fig_cmy = px.histogram(data_car_sales, x='model_year', title="Histogram of Model Year (No Condition Color)")

# Display the chart
st.header('Histogram of Condition vs Model Year')
st.plotly_chart(fig_cmy)

#violin plot of mileage by make
fig_vmm = px.violin(data_car_sales, x='model', y='odometer', title="Mileage Distribution by Make", box=True, points="all", color='model')

fig_vmm.update_layout(width=900, height=600)

fig_vmm.show()
 
