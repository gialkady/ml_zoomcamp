# Load the model

import pickle

from flask import Flask
from flask import request
from flask import jsonify

input_file = 'film_rating_pred.bin'

with open(input_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('rating')


@app.route('/predict', methods=['POST'])


def predict():
    film = request.get_json()

    X = dv.transform([film])
    y_pred = model.predict(X)[0, 1]

    low_rate = y_pred < 5
#high_rate = y_pred >= 5

    result = {
        'film_rating': float(y_pred),
        'low_rate': bool(low_rate)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)






