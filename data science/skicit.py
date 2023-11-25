import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
url = "https://moodlecurrent.gre.ac.uk/mod/resource/view...."  # Replace with the actual URL
df = pd.read_csv(url, delimiter='\t')

# Assuming 'Lifespan' is your dependent variable, and other columns are features
X = df.drop('Lifespan', axis=1)
y = df['Lifespan']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Plot actual vs. predicted values
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Lifespan")
plt.ylabel("Predicted Lifespan")
plt.title("Actual vs. Predicted Lifespan")
plt.show()
