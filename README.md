# Car Sales Analysis and Visualization

Car Sales Analysis and Visualization
Project Overview:
This project aims to provide an interactive analysis and visualization platform for a car sales dataset, with a focus on exploring vehicle attributes such as mileage, condition, and model year. The goal is to help users identify trends and patterns in the data, such as which cars are in good condition, have low mileage, or are priced competitively. The project utilizes Streamlit for interactive visualization and Plotly Express for dynamic plotting.

Key Features:
1.	Interactive Filtering: Users can filter the dataset based on various conditions, such as vehicle condition (e.g., "good", "fair") and mileage range (e.g., cars with mileage under 30,000 miles).
2.	Data Visualization: 
o	Histograms are generated to display distributions of vehicle attributes like mileage (odometer) and model year.
o	The data can be visualized by different conditions, allowing users to explore how car condition influences pricing and mileage.
3.	Real-Time User Inputs: The Streamlit application allows users to interact with data through checkboxes and sliders, enabling them to customize the views and analyze specific segments of the car sales data.
4.	Conditional Styling: Users can choose to color the plots by specific conditions (e.g., "Color by Condition" checkbox), offering deeper insights into how different factors like condition impact the overall distribution of attributes.


Technologies Used:
  •	Pandas- python’s open-source library for data analysis
  •	Streamlit- an open-source app framework that helps create beautiful performant web app quickly with minimal code.
  •	plotly.express- is a high-level API for creating interactive and visually appealing figures.
  •	Altair- is a declarative statistical visualization library that creates meaningful, elegant, and effective visualizations with minimal code.
  •	Python: The primary language used for data analysis and building the application.


Data Description:
  The dataset contains information about car sales, including:
    •	model_year: The year the car model was manufactured.
    •	cylinders: The number of cylinders the vehicle's engine has.
    •	odometer: The number of miles the vehicle has been driven.
    •	condition: The condition of the vehicle (e.g., "good", "fair", "excellent").
    •	type: The type of car (e.g., sedan, SUV, truck).
    •	price: The price of the car. 

•	model: the description of the model type (e.g., “bmw x5”, “ford f-150”, “Chrysler 200”)

Sample Use Case:
•	A user wants to see a histogram of vehicles in "good" condition with mileage under 30,000 miles. 
They can check the "Color by Condition" option to differentiate the cars based on their condition, 
allowing for a deeper understanding of how condition affects the distribution of mileage.
•	A car dealership wants to explore the distribution of vehicles by model year and engine type (cylinders) to understand which types of cars are most common in the market, and which may need to be priced competitively.
•	

Project Structure:
•	app.py: The main Streamlit app containing all the interactive widgets and visualizations.
•	Vehicles_us.csv: the file of raw car sales data.
•	requirements.txt: List of all required Python packages.


Future Improvements:
•	Price Analysis: Extend the analysis to include the price distribution of cars based on their condition and mileage.
•	Interactive Filtering: Add more filtering options, such as the ability to filter by car type, price range, or model year.
•	Modeling: Incorporate machine learning models to predict car prices based on features like mileage, condition, and type.

The know how to building an interactive web apps from a beginners perspective. The step-by-step instructions

1.	Using VS code and Python interpreter to set up and upload the project’s structure to connect to the project’s github.
2.	Clone the project’s git repository to my local machine, to commit and push the changes to my Git Hub repository.
3.	Build an interactive web application using streamlit
4.	Deploying this web application using the cloud platform Render, to be accessible to users.

Libraries to import and run in presenting data visualization.
-	Pandas- python’s open-source library for data analysis
-	Streamlit- an open-source app framework that helps create beautiful performant web app quickly with minimal code.
-	plotly.express- is a high-level API for creating interactive and visually appealing figures.
-	Altair- is a declarative statistical visualization library that creates meaningful, elegant, and effective visualizations with minimal code.

Here is my URL for Project Car Sales:
https://project-car-sales-wxh3.onrender.com
