# Sentiment Analysis with Machine Learning
A complete machine learning pipeline for sentiment analysis of text data using TF-IDF vectorization and classifiers like SVM, Logistic Regression, and Multinomial Naive Bayes.

---

## Overview

This project focuses on classifying text reviews into **positive**, **negative**, and **neutral** sentiments using traditional machine learning techniques. It includes:

- Data preprocessing (cleaning, lemmatization)
- Feature extraction using TF-IDF
- Model training and evaluation
- Performance comparison across multiple classifiers
- Model serialization for deployment

---

## Models Used

- Multinomial Naive Bayes
- Support Vector Machine (SVM)
- Logistic Regression

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Technologies

- Python
- Scikit-learn
- NLTK
- Pandas
- Matplotlib / Seaborn

---

## Deployment-Ready

The final model and vectorizer are saved using `pickle`, making it easy to integrate into:
- Web apps
- APIs
- Production systems

---

## Key Results

- **SVM** achieved the highest F1-score, particularly effective on negative sentiment detection.
- **Neutral reviews** were the hardest to classify correctly, indicating an area for improvement.
- Outperforms naive baselines by a significant margin.

---

## Future Work

- Integrate transformer-based models like BERT
- Experiment with LSTM/CNN architectures
- Add continuous learning and drift detection

---

## Dataset

The dataset used in this project is sourced from Kaggle and focuses on sentiment classification of financial text data.

- **Source**: [Financial Sentiment Analysis Dataset on Kaggle](https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis)
- **Classes**: Positive, Negative, Neutral
- **Type**: Text data extracted from financial articles, news headlines, and reports.

---

## Author

**Faizul Shaik**  
🎓 Data Science Student, GITAM Deemed University, Bengaluru  
📫 Email: fyzul1830@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/faizul-shaik131/)   

---

## 📌 Note

This project is solely for academic and portfolio-building purposes. The insights are exploratory and not intended for commercial decision-making.
