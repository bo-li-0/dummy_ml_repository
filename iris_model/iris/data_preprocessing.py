import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from iris_model.iris import Config

class IrisDataProcessing():

    def _formating(self, df: pd.Dataframe) -> pd.Dataframe:
        df.columns = df.columns.str.lower()
        return df

    def _training_filtering(self, df: pd.Dataframe, config: Config) -> pd.Dataframe:
        df_filtered = df.loc[df["sepal_length"] < config.sepal_length_max]
        return df_filtered

    def _load_data(self) -> pd.Dataframe:
        # load in dataset
        iris = load_iris()
        X = iris.data
        y = iris.target

        df = pd.Dataframe(X, columns=iris.feature_names)
        df['target'] = y

        return df

    def _save_data(self, df: pd.Dataframe, config: Config) -> None:
        processed_data_path = config.processed_data_path
        df.to_csv(f"{processed_data_path}/train.csv", index=False)

    def _train_test_split(self, df: pd.Dataframe, config: Config):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(df.drop("target"),
                                                            df["target"],
                                                            test_size=config.test_size, random_state=42)

    train_data.to_csv(f"{processed_data_path}/train.csv", index=False)
    test_data.to_csv(f"{processed_data_path}/test.csv", index=False)
