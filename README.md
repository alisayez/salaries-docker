# salaries-docker

## 01 - Train  

Download .csv file from https://drive.google.com/file/d/1iSjWvv_Bsk55Bls5FEmNJHU674f60HYM/view?usp=sharing
Train model in docker container using docker-compose  
creates saved_steps.pkl file  
copy saved_steps.pkl to 03 - Deploy folder
  

## 02 - Model
  
Trained model file  
  
## 03 - Deploy
  
Web application using the saved_steps.pkl model file using docker-compose  
Created using streamlit
  
visit http://localhost:8501 


## code source  

https://github.com/python-engineer/ml-app-salaryprediction

  
## docker compose commands  
  
running all docker containers in the docker-compose.yaml file
docker-compose up

running all docker containers in the docker-compose.yaml file in background
docker-compose up -d

stopping and removing all containers
docker-compose stop 

stopping and removing all containers
docker-compose down 
