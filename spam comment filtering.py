# Importing required libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

# Loading the dataset
data = pd.read_csv("yourdataset.csv")

# Selecting only the relevant columns
data = data[["CONTENT", "CLASS"]]

# Mapping class values to labels
data["CLASS"] = data["CLASS"].map({0: "Not Spam", 1: "Spam Comment"})

# Displaying a sample of the preprocessed data
print(data.sample(5))

# Splitting the data into features (x) and target (y)
x = np.array(data["CONTENT"])
y = np.array(data["CLASS"])

# Creating a CountVectorizer to convert text data into numerical features
cv = CountVectorizer()
x = cv.fit_transform(x)

# Splitting the data into training and testing sets
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

# Creating and training the Bernoulli Naive Bayes model
model = BernoulliNB()
model.fit(xtrain, ytrain)

# Evaluating the model on the test set
accuracy = model.score(xtest, ytest)
print(f"Model Accuracy: {accuracy}")

# Testing the model with sample comments
sample1 = "Check this out: https://thecleverprogrammer.com/"
sample2 = "Lack of information!"

data_sample1 = cv.transform([sample1]).toarray()
data_sample2 = cv.transform([sample2]).toarray()

prediction1 = model.predict(data_sample1)
prediction2 = model.predict(data_sample2)

print(f"Prediction for Sample 1: {prediction1}")
print(f"Prediction for Sample 2: {prediction2}")
