# from flask import Flask,render_template,request
# import joblib
# import numpy as np

# app=Flask(__name__)
# model=joblib.load("model.pkl")

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/predict', methods=["POST"])
# def predict():
#     Year=int(request.form["Year"])
#     Mileage=int(request.form["Mileage"])

#     features=np.array([[Year,Mileage]])
#     prediction=model.predict(features)

#     result = f"predicted price: ${prediction[0]:,.2f}"
#     return render_template("index.html",prediction=result)
# if __name__=="__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")
model = joblib.load(model_path)


@app.route("/")
def home():
    return jsonify({
        "message": "Car Price Prediction API is running!"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        year = int(data["Year"])
        mileage = int(data["Mileage"])

        features = np.array([[year, mileage]])

        prediction = model.predict(features)[0]

        return jsonify({
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)