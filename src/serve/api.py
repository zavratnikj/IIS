from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'model.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/air/predict', methods=['POST'])
def predict():
    data = request.get_json()

    input_data = [[data['no2'], data['pm2.5'], data['benzen'], data['temp'], data['pressure'], data['humidity'], data['wind_speed'], data['year'], data['month'], data['day'], data['hour']]]

    prediction = model.predict(input_data)

    return jsonify({'prediction': prediction[0]}), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)