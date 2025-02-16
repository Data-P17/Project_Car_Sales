import pandas as pd
import streamlit as st 
import plotly.express as px 

# Read the dataset's CSV file
data_car_sales = pd.read_csv('vehicles_us.csv')
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
st.write('''
         The Dataframe for Newer and Order Vehicles 
         ''')
#display the df with streamlit
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
st.header(PLOT_TITLE)
st.write('''
         Users are able to view the histogram where vehicles under 30,000 miles are in good condition.
         ''')
st.plotly_chart(fig_hist)

#Scatter plot of Car Mileage vs. Years
fig_cmvy = px.scatter(data_car_sales, x="model_year", y="odometer", color="type", hover_data=["model", "paint_color"])

st.write('''
         # Car Mileage vs Year
         Users can view the scatter plot to identify vehicles that meet their preferred balance of mileage and/or year, helping them find options with negotiable characteristics.
         ''')
st.plotly_chart(fig_cmvy)
# Histogram of Condition vs Model_year
# The relationship between condition and model_year
fig_cmy = px.histogram(data_car_sales, x='model_year', color='condition')
st.write('''
         # Condition vs Model_Year
        Users can use the histograms to select a vehicle based on their preferred condition and year.
         ''')
st.plotly_chart(fig_cmy)
#violin plot of mileage by make
fig_vmm = px.violin(data_car_sales, x='model', y='odometer', box=True, points="all", color='model')

fig_vmm.update_layout(width=900, height=600)

st. write('''
          # Mileage Distribution by Make
          Users can view a Violin plot to considering both mileage and vehicle model. This shows the best options of vehicles with lower mileage. 
          ''')
st.plotly_chart(fig_vmm)
# Exploring Vehicle Distribution by Model Year and Cylinders
# Here’s the code to allow a user to filter cars by model year and cylinder type
# Constants for filtering and titles
PLOT_TITLE2 = "Vehicle Distribution by Model Year and Cylinders"
MODEL_YEAR_RANGE = (2010, 2020)  # Default range for model years

# User Inputs: Model Year Range Slider
year_min, year_max = st.slider("Select Model Year Range", min_value=2000, max_value=2025, 
                               value=MODEL_YEAR_RANGE, step=1)

# User Input: Select Cylinders
cylinder_type = st.selectbox("Select Number of Cylinders", options=[4, 6, 8], index=0)

# Filter the dataset based on model year and cylinder type
filtered_data = data_car_sales[(data_car_sales['model_year'] >= year_min) & 
                               (data_car_sales['model_year'] <= year_max) &
                               (data_car_sales['cylinders'] == cylinder_type)]

# Create a bar chart to visualize the distribution of cars based on the filters
fig_bar = px.histogram(filtered_data, x="model_year", nbins=15, 
                       title=PLOT_TITLE2, 
                       labels={"model_year": "Model Year", "count": "Number of Cars"})

# Show the plot
st.header(PLOT_TITLE2)
st.write('''
         Users can use a plot chart to filter the vehicles by their year and its cylinder type. This assist in identifying a engine size relative to its year options. 
         ''')
st.plotly_chart(fig_bar)