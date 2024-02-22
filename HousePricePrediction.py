# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load California housing dataset
housing = fetch_california_housing()

# Create a pandas dataframe
df = pd.DataFrame(housing.data, columns=housing.feature_names)

# Display first five rows of the dataframe
print(df.head())

# Add target column to the dataframe
df['MEDV'] = housing.target

# Confirm the addition of the column
print(df.head())

# Create KDE plot of different variables
sns.kdeplot(data=df, x='AveRooms', fill=True)
sns.kdeplot(data=df, x='AveBedrms', fill=True)

# Model implementation
features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population']
label = 'MEDV'

X = df[features]
y = df[label]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=5)

# Train linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Display actual vs predicted values
result_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(result_df)

# Model testing
# Calculate various metrics
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = metrics.r2_score(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')
print(f'R2 Score: {r2}')

# Use polyfit to get slope and intercept for regression line
m, b = np.polyfit(X_test['AveRooms'], y_pred, 1)

# Plot regression line
plt.plot(X_test['AveRooms'], m * X_test['AveRooms'] + b)
plt.plot(X_test['AveRooms'], y_pred, 'o')
plt.xlabel("Average Rooms")
plt.ylabel("Median Value")
plt.show()

# Create a pairplot
sns.pairplot(df, x_vars=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population'], y_vars='MEDV', height=9, aspect=0.6, kind='reg')
plt.show()
