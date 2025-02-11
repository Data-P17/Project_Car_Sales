import pandas as pd
import streamlit as st 
import plotly.express as px 

# Read the dataset's CSV file
data_car_sales = pd.read_csv(r'/Data_P Github Repo/Project_Car_Sales/vehicles_us.csv')
print(data_car_sales.head())

# display the dataframe with Streamlit 
# creating a df header
st.header("Car Sales")
#diplay the df with streamlit
st.dataframe(data_car_sales)
# Checkbox to toggle between showing "condition" or "type" in histograms
color_by_condition = st.checkbox('Color by Condition', value=True)

# Plotly Express histogram for vehicles that are in good condition with low mileage
filtered_dcs = data_car_sales[(data_car_sales['condition'] == 'good') & (data_car_sales['odometer'] <= 30000)]
fig_hist = px.histogram(filtered_dcs, x="odometer", nbins=5, title="Good Condition Cars with Low Mileage")

st.plotly_chart(fig_hist)

# Histogram that shows the count of cars by their types, with checkbox control
if color_by_condition:
    fig_hist2 = px.histogram(data_car_sales, x='type', color='condition', title="Count of Cars By Vehicle Type and Condition")
else:
    fig_hist2 = px.histogram(data_car_sales, x='type', title="Count of Cars By Vehicle Type")

st.plotly_chart(fig_hist2)
# histogram that shows the count of cars by their types
fig_hist2 = px.histogram(data_car_sales, x='type', title="Count of Cars By Vehicle Tpye")
st.plotly_chart(fig_hist2)

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