# Sentiment Analysis API

A deployed machine learning model that classifies text as **Positive**, **Negative**, or **Neutral** using TF-IDF + SVM.

##  Run Locally
```bash
pip install -r requirements.txt
python app.py
```

##  Run with Docker
```bash
docker build -t sentiment-api .
docker run -p 5000:5000 sentiment-api
```

##  Example Request
```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "This is amazing!"}'
```

##  Output
```json
{
  "sentiment": "Positive",
  "confidence": 0.92
}
```