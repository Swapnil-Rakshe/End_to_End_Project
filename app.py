from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app = Flask('__name__')

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data=CustomData(
            cylinders = request.form.get('cylinders'),
            displacement = request.form.get('displacement'),
            horsepower = request.form.get('horsepower'),
            weight = request.form.get('weight'),
            acceleration = request.form.get('acceleration')
        )
        
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('index.html',results= f"Predicted miles per gallon is {results[0]}")
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)        
