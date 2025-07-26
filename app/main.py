import warnings
warnings.filterwarnings('ignore')
import os
from flask import Flask, jsonify, request
from PIL import Image
import numpy as np
from utility import NutritionData, OCR


google_api_key = os.getenv("GOOGLE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

nut = NutritionData(google_api_key, groq_api_key)
ocr = OCR()

app = Flask(__name__)

@app.route('/nutrition', methods=['POST'])
def get_nutrition():
    req_data = request.get_json()

    if not req_data or 'product' not in req_data:
        return jsonify({"error": "Missing 'product' in request body"}), 400

    product = req_data['product']

    try:
        _, heading, data = nut(product)
        return jsonify({
            "heading": heading,
            "data": data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/product-name', methods=['POST'])
def get_product_name():
    if 'product' not in request.files:
        return jsonify({"error": "Missing 'product' image in form-data"}), 400

    file = request.files['product']

    try:
        img = Image.open(file.stream)
        product_name = ocr(np.array(img))
        
        return jsonify({
            "name": product_name
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
