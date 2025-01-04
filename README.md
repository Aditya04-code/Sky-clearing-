# Sky-Clearing Prediction

## Project Overview  
In this captivating project, I aimed to harness the power of machine learning algorithms to predict optimal weather conditions for JFK Airport, particularly focusing on predicting clear skies. By analyzing weather data sourced from the **National Oceanic and Atmospheric Administration (NOAA)**, I sought to uncover patterns that lead to clear skies, improving operational planning at JFK Airport.

## Objective  
The primary objective of this project was to develop a predictive model that can forecast clear sky conditions at JFK Airport. This would empower decision-makers at the airport with valuable insights, helping them optimize operations and improve passenger experiences.

## Methodology  
1. **Data Collection**:  
   The dataset was sourced from the **NOAA**, containing historical weather data relevant to JFK Airport.
   
2. **Data Cleaning**:  
   Ensuring data integrity was crucial. I conducted a rigorous data cleaning process, addressing inconsistencies, handling missing values, and eliminating noise, which elevated the model's predictive accuracy.

3. **Algorithm Comparison**:  
   Several machine learning algorithms were tested and compared for their performance on the dataset. The models evaluated included:
   - **Linear Regression**
   - **Ridge Regression**
   - **Lasso Regression**
   - **Elastic Net**
   - **Support Vector Regression (SVR)**
   - **Random Forest**

   The models were compared using performance metrics such as **RMSE** (Root Mean Squared Error) and **MAPE** (Mean Absolute Percentage Error) to determine which algorithm performed best in predicting clear skies. Among these, **Random Forest** was chosen as the final model due to its superior performance.

4. **Model Saving and Reusability**:  
   The trained **Random Forest** model was saved using the **pickle** library. This allows the model to be reused and called multiple times for analysis without the need for retraining, ensuring efficiency and consistency.

5. **Model Development**:  
   The final model was integrated into a user-friendly web application using **Streamlit**, making it easy to interact with and access predictions for JFK Airport weather conditions.

## Key Outcomes  
- Developed a predictive algorithm capable of forecasting clear skies with high accuracy.
- Helped ensure that decision-makers at JFK Airport can optimize their operations with insights into weather patterns, ultimately enhancing passenger experience and flight scheduling.
- **Random Forest** was selected as the best model based on its accuracy metrics (RMSE and MAPE).

## Live Demo  
Explore the live version of the project:  
[Sky-Clearing Prediction App](https://aditya04-code-sky-clearing--app-qk3w8i.streamlit.app/)

## Technologies Used  
- **Python**  
- **Streamlit**  
- **Pandas**  
- **Scikit-learn**  
- **NOAA Weather Data**  
- **Matplotlib / Seaborn** (for data visualization)  
- **Pickle** (for saving and loading the trained model)

## Conclusion  
This project blends meteorology and machine learning to provide actionable insights for airport operations, ultimately helping to ensure smoother and more efficient travel experiences.

