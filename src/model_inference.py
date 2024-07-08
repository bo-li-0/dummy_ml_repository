import pandas as pd
import joblib

def run(config):
    processed_data_path = config['processed_data_path']
    model_path = config['model_path']

    test_data = pd.read_csv(f"{processed_data_path}/test.csv")
    X_test = test_data.drop(columns=['target'])
    y_test = test_data['target']

    model = joblib.load(model_path)

    predictions = model.predict(X_test)

    print("Prediction:", predictions)
    print("Actuals:", y_test.values)