# Group 20 Phase-4-Project

# Student Names
* Frank Kiptoo Ruto
* Abdihakim S Mohamed
* Lilian Ngige

# Project Overview

## Objective
To develop a time series forecasting model using Zillow data to assist real estate investors in making informed decisions about where to invest their capital. This model will provide predictions and insights into property price trends over time, helping investors identify regions and cities with potential for price appreciation.

## Business Context
Our client, a real estate investment firm, aims to expand its portfolio with strategic investments in residential properties. The real estate market, being influenced by a myriad of factors, presents both opportunities and risks. The firm's success hinges on its ability to forecast future market trends and make data-driven decisions.

## Business Challenge
The real estate investment firm seeks to maximize its return on investment by strategically purchasing properties in areas predicted to experience significant value appreciation. The challenge lies in analyzing vast amounts of data to discern these profitable areas.

The firm needs insights into where the market is heading, not just where it has been.

### The Data

The data used was downloaded from [Zillow Research Data](https://www.zillow.com/research/data/)

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

## Top 5 Zipcodes with the Highest ROI

![Screenshot 2023-12-01 032403](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/bc0d9fc2-aa6b-468a-a7e7-2c54265ebc5e)

## Time Series Plot Showing the Monthly Average Housing Prices Following the 2008 Housing Crisis

![Screenshot 2023-12-01 032325](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/7cdc3979-ab4e-46d0-aabe-1a766962e288)

## Plot Showing the Differenced Housing Prices series

![Screenshot 2023-12-01 032244](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/dd48a719-8478-465e-95fe-ac420d6f3944)

## Decomposition Plot

![Screenshot 2023-12-01 032519](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/f92d296d-8bac-4ab5-8894-82f640f0375d)

## Rolling Mean & Standard Deviation Plot

![Screenshot 2023-12-01 032706](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/4f2428a4-52a9-4577-b2f7-cac85073d073)

## ARIMA(2,0) Model

![Screenshot 2023-12-01 032813](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/9280f75a-accd-4b3f-ae48-489ec0733dfd)

## ARIMA(2,1) Model

![Screenshot 2023-12-01 032923](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/2d28cfdc-982c-4f1f-ba21-0053ed42a046)

## SARIMA Model

![Screenshot 2023-12-01 033024](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/af098146-4637-4163-9388-ad7d84c08210)

## PMDARIMA( auto_arima)

![Screenshot 2023-12-01 033100](https://github.com/frankkiptoo/Group-20-Phase-4-Project/assets/133040810/d997b779-d26f-46ce-85ea-a3f1e0c502e1)


# Recommendations
The top 5 zip codes ranked by highest return on investment (ROI) with the least amount of unpredictability and variation are:

* 11211: Kings County, New York
* 11222: Kings County, New York
* 11216: Kings County, New York
* 7302: Hudson County, Jersey City
* 11215: Kings County, New York
The regions selected share certain characteristics that yield attractive risk-adjusted returns. Each zip code is from a Tier 1 or 2 city. These cities share the characteristics of:

* Healthy employment and strong economics anchored by the higher-than-usual opportunity in these high-tier cities.

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

