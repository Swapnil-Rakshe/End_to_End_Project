# Predict Fuel Efficiency with Machine Leaning

## Objective
The goal is to develop a machine learning model capable of predicting car miles per gallon (mpg) based on various car features. These features include the number of cylinders, engine displacement, power produced by the engine, acceleration, and weight of the car. The developed model is then deployed on Amazon Web Services (AWS) to enable easy and scalable access. The model is trained using a suitable machine learning algorithm and evaluated using relevant performance metrics. The final trained model will be saved as a file and deployed on AWS using a suitable platform, such as AWS Elastic Beanstalk. The developed machine learning model has been containerized using Docker. The Docker image has been created and published on Docker Hub, a container registry, with the name "swapnil1997rakshe/predict_fuel_efficiency:latest". This image can be used to easily deploy the model on any system or cloud platform that supports Docker containers. By making the image available on Docker Hub, other users can easily access and use the model in their own applications.

## Content
* `Artifacts` contains train, test datasets and trained model, preprocessor pickel files.
* `notebook` contains code files in Jupyter Notebook..
* `src` contains source code.
* `templates` folder has the index.html file, which is a webpage for the user interface.
* `app.py & application.py` files contain the main code for running a web application built using Flask framework.


  
## Steps Performed

* Data was collected from Kaggle platform.
* Exploratory Data Analysis (EDA) was performed to identify any outliers and explore relationships between the variables or features.
* Hyperparameter tuning using GridSearchCV was performed to select the best model with optimal parameters for the given problem.
* A Docker image was built for the developed machine learning model.
* The Docker image was pushed to Docker Hub for public availability.
* A web application was built using Flask to serve the developed model.
* The web application was deployed using Elastic Beanstalk, a cloud computing platform provided by Amazon Web Services (AWS).


## Web Application
![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Web%20application.png)
