from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

#Create flask server
app = Flask('__name__')

# Route for the home page
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

# Route for the prediction page
@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # Extract data from the form and create a CustomData instance
        data=CustomData(
            cylinders = request.form.get('cylinders'),
            displacement = request.form.get('displacement'),
            horsepower = request.form.get('horsepower'),
            weight = request.form.get('weight'),
            acceleration = request.form.get('acceleration')
        )
        
        # Convert the custom data to a DataFrame
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")
        
        # Create a PredictPipeline instance and make predictions
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        
        # Display the prediction results on the webpage
        return render_template('index.html',results= f"Predicted miles per gallon is {results[0]}")
    
# Run the Flask app
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)        
