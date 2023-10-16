from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

# preparing the data
def load_and_prepare_data():
    df = pd.read_csv("C:\\Users\\Owner\\Desktop\\Coding\\Xtern Application\\AI Prompt\\XternAIChallenge\\data.csv") # the given dataset (csv format)

    # Encode categorical variables
    for column in ['Year', 'Major', 'University']:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column]) # converts categorical data in all columns to numerical data that the model can accept as input

    X = df.drop('Order', axis=1)
    y = df['Order']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # try random state = 79

    return X_train, X_test, y_train, y_test

# running the model
def run_model():
    X_train, X_test, y_train, y_test = load_and_prepare_data() # training and testing data

    clf = RandomForestClassifier(n_estimators=100, random_state=42) # using a Random Forest Classifier
    clf.fit(X_train, y_train)
    pickle_model(clf) # save the model to a file so that it can be accessed later without having to retrain it from scratch

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return f"Model Accuracy: {accuracy * 100:.2f}%"

# converting model to a byte stream and saving it as a file 
def pickle_model(model):
    # creates/overrides file named 'model.pkl'. 
    pickle.dump(model, open('model.pkl', 'wb')) # 'wb' means binary write mode. (writing to a file)

# loading the model from an already-existing .pkl file (not used here, but relevant nevertheless)
def load_model(path):
    # converts the specified file with filepath 'path' back into a model, and returns the model object
    return pickle.load(open(path, 'rb')) # 'rb' means binary read mode. (reading a file)

# printing the results
print(run_model())
