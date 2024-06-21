import os
import pickle
import click
import mlflow
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from mlflow.sklearn import autolog

# mlflow.sklearn.autolog(disable=True)
# mlflow.autolog()
with mlflow.start_run(): 


        mlflow.set_tag("dev", "Sheyi")
        #mlflow.log_param("train-data-path", "week-02/TAXI_DATA_FOLDER/week-02/TAXI_DATA_FOLDER/green_tripdata_2023-02.parquet")
        def load_pickle(filename: str):
                with open(filename, "rb") as f_in:
                        return pickle.load(f_in)


        @click.command()
        @click.option(
                "--data_path",
                default="./week-02/output",
                help="Location where the processed NYC taxi trip data was saved"
        )
        def run_train(data_path: str):
                
                #mlflow.sklearn.autolog()

                X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
                X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

        
                rf = RandomForestRegressor(max_depth=10, random_state=0)
                rf.fit(X_train, y_train)
                y_pred = rf.predict(X_val)

                rmse = mean_squared_error(y_val, y_pred, squared=False)
                mlflow.log_metric("rmse", rmse)
                print("The script is working ")
                print(rmse)

        ## Sheyi added this 
        #def dump_pickle(filename: str):
        # with open(filename, "rb") as f_out:
                # return pickle.load(f_out)


        #@click.command()
        #@click.option(
        #  "--data_path",
        # default="./output",
        # help="Location where the processed NYC taxi trip data was saved"


        if __name__ == '__main__':
                run_train()

                