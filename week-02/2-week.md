## Week 2

## Homework
To get started with MLflow you'll need to install the MLflow Python package.gooch


```md
## conda env
`https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-envs`

```

##
pip install or requirements.txt



```md
## create a seperate python environment and the n install the pacjage with pip or conda

## create mloflow env
conda create -n <env-name>

conda create -n mlflow python=3.9

# To activate this environment, use

 conda activate mlflow

# To deactivate an active environment, use
 conda deactivate


pip install mlflow

## homeworkq1

mlflow --version
```
##homework2

```md
## preprocess the data 
- download three files including Green tripdata for Jan, Feb, March 2023 and store in a folder called Taxii_data_folder 


## run the script 
python preprocess_data.py --raw_data_path <TAXI_DATA_FOLDER> --dest_path ./output
```
## Q3    - Train the model

```md

## there is a training script 
train.py

The script will:

load the datasets produced by the previous step,
train the model on the training set,
calculate the RMSE score on the validation set.


## Task 
Q3. Train a model with autolog
We will train a RandomForestRegressor (from Scikit-Learn) on the taxi dataset.

We have prepared the training script train.py for this exercise, which can be also found in the folder homework.


Your task is to modify the script to enable autologging with MLflow, execute the script and then launch the MLflow UI to check that the experiment run was properly tracked.

Tip 1: don't forget to wrap the training code with a with mlflow.start_run(): statement as we showed in the videos.

Tip 2: don't modify the hyperparameters of the model to make sure that the training will finish quickly.

What is the value of the min_samples_split parameter:
```
```md

## choose your env kernel

mlflow kernel3 python is mine 
## setting up mlflow

pip install -r requirements

## congifure backend to prevent fails, just for experiments
!mlflow ui --backend-store-uri sqlite:///mflow.db

## copy output
copy output and place in a browser
http://127.0.0.1:5000

##
import mlflow  

mlfow.set_tracking_uri("sqlite://mflow.db")

mlflow.set_experiment("my-brand-new-experiment")

run it 
```

## debugging
```md
pip show scikit-learn

pip install scikit-learn==<desired_version>


```

![ssh config](https://github.com/sheyijojo/my_mlops_bootcamp/blob/main/assets/exp-001.png?raw=true)

