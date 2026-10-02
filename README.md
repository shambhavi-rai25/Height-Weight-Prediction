# Height-Weight-Prediction using Regression
1. Project Overview
This project uses Machine Learning 'regression' algorithms to predict a person's weight(kg) based on their height(cm).

The project starts with a Height and Weight dataset obtained from Kaggle. The original dataset contains height in inches and weight in pounds(lbs). For easier interpretation and a more practical application, the values are converted to:
Height → Centimeters (cm)
Weight → Kilograms (kg)

Multiple regression models are trained and evaluated to determine which model performs best. The selected model is then integrated into a Streamlit web application where users can enter their height and receive a predicted weight.

2. Dataset
The dataset contains information about people's:
* Gender
* Height
* Weight
The dataset contains 10,000 observations.

3. Correlation Analysis
The Pearson correlation coefficient between height and weight is:
0.924756
This indicates a strong positive linear relationship between height and weight in this dataset.

4. Machine Learning Models
Multiple regression algorithms are implemented and compared. The models include:
* Simple Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regression
* Random Forest Regression
The purpose of comparing multiple algorithms is to determine which model provides the best predictive performance on the test data.

5. Model Evaluation
The models are evaluated using several regression metrics.

* R² Score
Measures how well the model explains the variation in the target variable.
Higher R² is better.

* MAE - Mean Absolute Error
Measures the average absolute difference between actual and predicted values.
Lower MAE is better.

* MSE - Mean Squared Error
Measures the average squared prediction error.
Lower MSE is better.

* RMSE - Root Mean Squared Error
The square root of MSE and expresses the error in the same units as the target variable.
Lower RMSE is better.

6. Best Model Selection
The final model is selected based on its performance on the test dataset.
The final trained model is saved using Joblib.

7. Streamlit GUI
The trained model is integrated into a Streamlit application. The application allows the user to:
* Enter their height in centimeters.
* Click the Predict Weight button.
* Receive the predicted weight in kilograms.


8. Note
The model should primarily be used for predictions within the range represented in the training dataset.
The dataset has an observed height range of approximately: 137.83 – 200.66 cm
Predictions for heights far outside this range can be unreliable because they require the model to extrapolate beyond the data it learned from.

9. Conclusion
This project demonstrates how regression algorithms can be applied to predict weight from height.
The project also demonstrates an end-to-end machine learning workflow:
Data → Preprocessing → EDA → Regression → Evaluation → Model Selection → Deployment
The final Streamlit application provides a simple interface for making predictions using the selected regression model.
