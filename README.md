# 🧠 Smart Nutrition API

## 📌 Overview
Extract product names from image uploads and retrieve structured, health-focused nutritional information using Google Search + LLM (Groq API) pipeline.

## 📁 Directory Structure
```graphql
.
├── app/
│   ├── easyocr_model/             # EasyOCR pre-trained models (downloaded manually)
│   ├── utility/
│   │   ├── google_api.py          # Uses Google's SERP to fetch nutritional product info
│   │   ├── llm.py                 # Interfaces with Groq LLM for structured JSON output
│   │   ├── nutrition_data.py      # Core logic to fetch and clean nutrition data
│   │   └── ocr.py                 # Extracts product name from image using EasyOCR
│   └── main.py                    # Flask API entry point
├── .gitignore
├── Dockerfile
└── requirements.txt
```

## 🔌 API Endpoints
1. `/product-name`
Purpose: Extract product name from an uploaded image.
    - Method: `POST`
    - Payload: Form-data with key "product" as the image file.
    - Returns:
      ```json
      {
        "name": "quaker oats"
      }
      ```

3. `/nutrition`
Purpose: Get nutritional information for a given product name.
    - Method: `POST`
    - Payload (JSON):
      ```json
        {
          "product": "quaker oats"
        }
      ```
    - Returns:
      ```json
      {
        "heading": "Quaker Oats Nutritional Summary",
        "data": {
          "Calories": "150 kcal",
          "Protein": "5g",
          "Carbs": "27g",
          "Fat": "3g"
        }
      }
      ```

## 🔄 Flow Overview
```scss
[Image Upload] ─┐
                └──> OCR (EasyOCR) ──> Product Name ──┐
                                                      ↓
                                           Google Search API (SERP)
                                                      ↓
                                            Groq LLM (via prompt)
                                                      ↓
                                      Structured JSON Table of Nutrients
```

## 📦 Setup Instructions
### ✅ Requirements
  - Python 3.9+
  - EasyOCR model pre-downloaded to ./easyocr_model/
  - .env file or environment variables:
      - GOOGLE_API_KEY
      - GROQ_API_KEY
   
### ⚙️ Installation
```bash
git clone https://github.com/yourusername/nutrition-extractor.git
cd nutrition-extractor

# Install dependencies
pip install -r requirements.txt

# Run the API
python app/main.py
```

### 🐳 Docker Support (Optional)
```bash
# Build docker image
docker build -t nutrition-api .

# Run the container
docker run -p 5000:5000 \
  -e GOOGLE_API_KEY=your_key \
  -e GROQ_API_KEY=your_key \
  nutrition-api
```
The already built [image in dockerhub](https://hub.docker.com/repository/docker/tkdutta/smart-nutrition-api/general) can also be used instead.

## 🛠️ Tech Stack

| Component        | Tool/Service             |
|------------------|--------------------------|
| OCR              | EasyOCR                  |
| Image Processing | Pillow, NumPy            |
| LLM Interface    | Groq (LLaMA 3.1)         |
| Search API       | Google SERP (unofficial) |
| Web API          | Flask                    |
| Containerization | Docker                   |


## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. For more details and updates, visit the GitHub Repository.


