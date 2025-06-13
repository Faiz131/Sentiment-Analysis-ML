from flask import Flask, request, jsonify
import pickle

# Load the saved model and vectorizer
with open("model_pipeline.pkl", "rb") as f:
    data = pickle.load(f)
    vectorizer = data['vectorizer']
    model = data['model']

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Sentiment Analysis API is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Validate input
    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide text in JSON format like { "text": "your message" }'}), 400

    input_text = data['text']

    # Vectorize input and predict
    text_vector = vectorizer.transform([input_text])
    prediction = model.predict(text_vector)[0]
    confidence = model.predict_proba(text_vector).max()

    return jsonify({
        'sentiment': prediction,
        'confidence': round(float(confidence), 3)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
