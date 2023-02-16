# Project Name
- author(s): Kwang Heum Yeon
- date created: May 10, 2022
- class: CIS 9440

Project Objective: Follow the Kimball Lifecycle to design and develop a public, cloud-based Data Warehouse with a functioning BI Applications

Project Tools:
The tools used to build this Data Warehouse were: 
1. For data integration - python
2. For data warehousing - Google BigQuery
3. For Business Intelligence - Tableau

## Kimball Lifecycle Project Stages

### Project Planning

Motivation for project:
I’d love my neighbors to have a healthy life and save time by having the current bicycle operating system optimized.

Description of the issues or opportunities the project will address:
New York City is one of the most densely populated areas having lots of traffic congestion at 
almost every street over the year. To alleviate the traffic jam and promote an eco-friendly policy
to residences, the city has been installed and executed a bicycle self-check-in and out system.
However, it is questionable if the number of available bicycles is demographically optimized
considering my previous experience.
To answer this question, New York City Bicycle Operation Data Warehouse will combine bicycle
count, location, zip code, and census to uncover insights regarding bicycle count per a New
York City resident.

Project Business or Organization Value:
The primary value of this project is to reduce the city's budget through optimization of the
current bicycle management system. It is expected to save the city's budget by
decreasing carbon dioxide emissions and alleviating traffic congestion and establishing a
healthy bicycle-loving culture in New York City.

Data Sources:
There are three separate datasets to get the KPI's. Two of them were extracted from the NYC open
data(https://opendata.cityofnewyork.us/) and the other referred to New York Demographics by
Cubit.
1. https://data.cityofnewyork.us/Transportation/Bicycle-Counts/uczf-rk3c
2. https://data.cityofnewyork.us/Transportation/Bicycle-Counters/smn3-rzf9
3. https://www.newyork-demographics.com/zip_codes_by_population

### Business Requirements Definition

List of Data Warehouse KPI's:
1. Bicycle service key locations
2. Bicycle counts per key location
3. Bicycle counts per month
4. Linear regression between bicycle counts and population
5. Population per a bicycle by location


### Dimensional Model

This project's Dimensional Model consists of 2 Facts and 3 Dimensions

This project's Dimensional Model:
https://github.com/cpasean/DataWarehouse/blob/main/Dimensional%20Model.png

This project's Kimball Bus Matrix:
https://github.com/cpasean/DataWarehouse/blob/main/Kimball%20Bus%20Matrix.png

### Business Intelligence Design and Development

List of Visualizations for each KPI:

1. Bicycle service key locations: Map
Because we have an altitude and longitude in our location dimension, 
we can plot the exact location on the map, which will visually aid this KPI.

2. Bicycle counts per key location: Map
We will adjust the size of the circle pointing at each location per the number of counts because
we can deliver a piece of combined information for those two KPI’s; the location and bicycle counts.

3. Bicycle counts per month: Area Chart
I would like to understand the seasonal fluctuations that might have at each location to balance it 
with the overall demand for bike usage. I believe an area chart will depict this purpose enough.

4. Linear regression between bicycle counts and population: Scatter chart
We will draw a trend line on the scatterplot between the population and the bicycle counts each per location. 
We believe the trend line containing coefficient, p-value, and r-squared, can be well depicted on the scatterplot.

5. Population per a bicycle by location: Bubble chart

This is the main KPI we’d like to deliver. As an idea of how to efficiently manage the NYC bicycle system, 
the bubble chart will highlight the importance of balancing the number of bicycles in real-time. 
The bigger the circle is, the more it's required to increase the number of bicycles.


BI Application Wireframe design:
https://github.com/cpasean/DataWarehouse/blob/main/wireframe_design.png

Picture of final Dashboard:
https://github.com/cpasean/DataWarehouse/blob/main/final%20dash%20board.png

### Deployment

The project was deployed on Tableau Public: 
https://public.tableau.com/app/profile/sean.yeon/viz/cis9440_finalProject/Dashboard1?publish=yes
