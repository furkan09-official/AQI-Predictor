from flask import Flask , request , jsonify
import joblib
import numpy as np

app = Flask(__name__)


#load the train model
model = joblib.load('models/aqi_model.pkl')

@app.route('/predict', methods =['POST'])
def predict():
    #get the data from the request
    data = request.get_json()

    #convert the data to the appropriate formate
    input_data = np.array([data['features']]).reshape(1,-1)

    #make prediction
    prediction = model.predict(input_data)

    # return in json
    return jsonify({'predicted_aqi': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)