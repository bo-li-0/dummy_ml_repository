import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def run(config):
    processed_data_path = config['processed_data_path']

    # load in dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state=42)

    # Save the processed data
    train_data = pd.Dataframe(X_train, columns=iris.feature_names)
    train_data['target'] = y_train
    test_data = pd.Dataframe(X_test, columns=iris.feature_names)
    test_data['target'] = y_test

    train_data.to_csv(f"{processed_data_path}/train.csv", index=False)
    test_data.to_csv(f"{processed_data_path}/test.csv", index=False)
