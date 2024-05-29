## Three phases
- Design
- Train
- Operate 

## configure the environment 
### So we either use codespaces or EC2 machine 
### I will go with the codespace env to save cost on EC2. 

```md
Either use codespaces or install locally 

codespaces come installed with python 3.10.13 
```

## Installation

```md
## Install anaconda version 3-2022.05-linux

wget  https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh

bash Anaconda3-2022.05-Linux-x86_64.sh


## The pront asks for initialization, say yes 
hence, it runs `conda init` for us
```

## Note from the anaconda terminal

```md

If you'd prefer that conda's base environment not be activated on startup, 
   set the auto_activate_base parameter to false: 

# conda config --set auto_activate_base false

Thank you for installing Anaconda3!

## check your bashrc to see what was installed

cat ~/.bashrc

## activate the anaconda shell,  i.e create a new terminal

bash

which python

## This is the python from anaconda

## Start a jupyter notebook server

jupyter notebook

```
## Create a new notebook 
```md
# create a new notebook from the notebook server

import pandas as pd

pd.__version__

## read pacquet data from public repo 

url = https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet

## install the lib for pacquet files

!pip install pyarrow

## you can do it on terminal as an option
pip install pyarrow

import sklearn

```

## Do not forget to stop codespaces 

## EC2 setUp vs Codespaces 
```md
## ec2
t2 large free tier
storage 30GB
Ubuntu OS

ssh into EC2

## configure the config file

vim .ssh/config 

```
## Image of config setup

![ssh config](https://github.com/sheyijojo/my_mlops_bootcamp/blob/main/assets/sshconfig.png?raw=true)


```md

## easy ssh 
ssh mlops-zoomcamp 

## memory error using DictVectorizer

Quote from a student 

"Hello, i've just submitted the first homework. One thing that i thought it worth mentioning for others running experiments on local environment: this first exercise required me to raise WSL memory to 24Gb because of DictVectorizer + fitting the model. If your kernel dies during cell execution, then this is probably the case."
```
## Terraform installation