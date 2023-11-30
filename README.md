# Group 20 Phase-4-Project

# Students Names
* Frank Ruto Kiptoo
* Abhakim S Mohamed
* Lilian Ngige

# Project Overview

## Objective
To develop a time series forecasting model using Zillow data to assist real estate investors in making informed decisions about where to invest their capital. This model will provide predictions and insights into property price trends over time, helping investors identify regions and cities with potential for price appreciation.

## Business Context
Our client, a real-estate investment firm, aims to expand its portfolio with strategic investments in residential properties. The real estate market, being influenced by a myriad of factors, presents both opportunities and risks. The firm's success hinges on its ability to forecast future market trends and make data-driven decisions.

## Business Challenge
The real estate investment firm seeks to maximize its return on investment by strategically purchasing properties in areas predicted to experience significant value appreciation. The challenge lies in analyzing vast amounts of data to discern these profitable areas.

The firm needs insights into where the market is heading, not just where it has been.

### The Data

The data used was downlaoded from kaggle

# Methods Applied
* Loaded the data using python modules to read the data
* Data Understanding
* Data Processing
* EDA & Data Visualization
* Time Series Modelling
    * Removing Trends
    * Differencing
    * Decomposing
    * Correlation and Autocorrelation
* ARMA Model
    * Model 1: ARIMA(2,0) Model
    * Model 2: ARIMA(2,1) Model
    * Model 3: SARIMA Model
    * Model 4: PMDARIMA( auto_arima)
* Evaluation

# Results
<img width="1079" alt="Screenshot 2023-11-30 at 20 15 42" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/4c81030e-7c6a-41a0-b422-89e5b417a4c4">

<img width="982" alt="Screenshot 2023-11-30 at 20 18 55" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/7c97d5de-d7f4-4e04-b005-0898a40134d2">

<img width="823" alt="Screenshot 2023-11-30 at 20 20 25" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/f3fa427e-c823-4359-8adb-8feb97abd7da">

<img width="953" alt="Screenshot 2023-11-30 at 20 22 37" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/b58a82ee-8116-4b11-b7d1-c00723c6c3f1">

<img width="985" alt="Screenshot 2023-11-30 at 20 25 01" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/39860936-e5b3-4092-90b6-5e5e624a7d30">

<img width="689" alt="Screenshot 2023-11-30 at 20 27 08" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/e6cd4024-43bd-4fcc-82c7-b36eeb315162">

<img width="961" alt="Screenshot 2023-11-30 at 20 26 05" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/358ca586-1f0e-4ec5-9ade-05f7f758f374">

<img width="1002" alt="Screenshot 2023-11-30 at 20 28 43" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/e5e7189b-ebab-4d54-a7a3-ed00eb54bb8c">

<img width="860" alt="Screenshot 2023-11-30 at 20 23 33" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/17a55937-6646-472a-b768-1ba42706483e">

<img width="966" alt="Screenshot 2023-11-30 at 20 27 53" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/a9c3aa28-0aeb-4d78-bced-2f1c89ff3e50">

<img width="1002" alt="Screenshot 2023-11-30 at 20 28 43" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/9b27471b-745b-46f3-907b-af1deb3a68c9">

<img width="976" alt="Screenshot 2023-11-30 at 20 29 34" src="https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133906913/c209acd0-da15-4ddb-bccf-dccbac0f283b">


# Reccomendations
The top 5 zip codes ranked by highest return on investment (ROI) with the least amount of unpredictability and variation are:

* 11211: Kings County, New York
* 11222: Kings County, New York
* 11216: Kings County, New York
* 7302: Hudson County, Jersey City
* 11215: Kings County, New York
The regions selected share certain characteristics that yield attractive risk adjusted return. Each zip code is from a Tier 1 or 2 city. These cities share the characteristics of:

* Healthy employment and strong economics anchored by the higher than usual opportunity in these high tier cities.

* Proximity to amenities such as parks, entertainment, or transit.

* Population growth fueling housing demand.

We would recommend that future investment consideration adheres to these characteristics. Together, they create strong demand that results in efficient ROI. Further analysis that uses employment, income growth, and population growth may reveal other lucrative zip codes.

# Limitations
1. Property values are influenced by more than just time; they are also affected by the balance of supply and demand, which this study does not entirely encompass. While this is useful for understanding how real estate markets change over time, it does nothing to explain all the other factors that are driving changes in housing prices. Some next steps in this project include added exogenous factors to our model:
* Interest rates
* Crime data
* Median income over time
* Population growth
* Morgage rates
Nonetheless, incorporating these factors goes beyond the intended purpose of this particular project.

2. The Zillow dataset used for this analysis had its most recent data points in April 2018. Finding more recent data will allow us to more accurately forecast future home value into 2025 and beyond.

