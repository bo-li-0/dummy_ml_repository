import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

def run(config):
    processed_data_path = config['processed_date_path']
    model_path = config['model_path']
    parameters = config['parameters']

    # Load the training dataset
    train_data = pd.read_csv(f"{processed_data_path}/train.csv")
    X_train = train_data.drop(columns=['target'])
    y_train = train_data['target']

    # Train
    model = RandomForestClassifier(n_estimators=parameters['n_estimators'], max_depth=parameters['max_depth'])
    model.fit(X_train, y_train)

    joblib.dump(model, model_path)