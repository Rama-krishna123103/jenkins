import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Training function
def train_model():
    # Load dataset
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    X = data.drop('species', axis=1)
    y = data['species']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")

    # Save model
    joblib.dump(model, 'model.pkl')
    print("Model saved as 'model.pkl'")

# Prediction function
def predict(data):
    # Load model
    model = joblib.load('model.pkl')

    # Predict
    predictions = model.predict(data)
    return predictions

if __name__ == "__main__":
    train_model()
