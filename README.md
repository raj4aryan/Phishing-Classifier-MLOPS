# 🛡️ Network Security Classifier

A production-oriented Machine Learning system for detecting phishing websites using supervised learning, cloud storage, experiment tracking, containerization, and modern web technologies.

The project implements a complete ML lifecycle:

- Data Ingestion from MongoDB
- Data Validation
- Data Transformation
- Model Training & Evaluation
- Experiment Tracking with MLflow & DagsHub
- Artifact Management with AWS S3
- REST API using FastAPI
- React Frontend for Batch Predictions
- Docker Containerization
- AWS Deployment
- CI/CD using GitHub Actions

---

## 📌 Project Overview

Phishing attacks are one of the most common cybersecurity threats, where malicious websites imitate legitimate websites to steal sensitive user information.

This project builds a Machine Learning pipeline capable of classifying websites as:

- ✅ Legitimate
- 🚨 Phishing

The system supports batch prediction using CSV uploads and provides confidence scores for every prediction.

---

## ✨ Features

### Machine Learning Pipeline

- Data Ingestion from MongoDB
- Data Validation using schema checks
- Data Transformation Pipeline
- Feature Engineering
- Model Training
- Model Evaluation
- Best Model Selection
- Model Serialization

### Prediction Service

- Batch CSV Prediction
- Confidence Score Generation
- REST API Support
- FastAPI Backend

### Frontend

- React-based User Interface
- CSV Upload Support
- Prediction Dashboard
- Confidence Visualization
- Summary Statistics

### MLOps & Deployment

- MLflow Experiment Tracking
- DagsHub Integration
- AWS S3 Artifact Storage
- Dockerized Application
- AWS ECR Container Registry
- AWS EC2 Deployment
- GitHub Actions CI/CD Pipeline

---

## 🏗️ System Architecture

```text
                    ┌────────────────────┐
                    │      MongoDB       │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ Data Ingestion     │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ Data Validation    │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ Data Transformation│
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ Model Training     │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ MLflow + DagsHub   │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ AWS S3 Storage     │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ FastAPI Backend    │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ React Frontend     │
                    └────────────────────┘
```

---

# 📂 Project Structure

```text
NETWORK SECURITY CLASSIFIER
│
├── .github/
│   └── workflows/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── ml-services/
│   │
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── setup.py
│   │
│   ├── artifacts/
│   ├── logs/
│   ├── models/
│   ├── notebook/
│   ├── test/
│   │
│   └── networkSecurity/
│       │
│       ├── cloud/
│       │   └── s3_syncer.py
│       │
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── data_transformation.py
│       │   └── model_trainer.py
│       │
│       ├── constants/
│       ├── entity/
│       ├── exceptions/
│       ├── logging/
│       ├── pipeline/
│       └── utils/
│
├── README.md
└── LICENSE
```

---

# 🧠 Machine Learning Workflow

## Data Ingestion

- Connects to MongoDB
- Extracts Network Security dataset
- Stores raw data artifacts

## Data Validation

- Schema Validation
- Missing Value Checks
- Dataset Integrity Verification

## Data Transformation

- Feature Processing
- Preprocessing Pipeline Creation
- Artifact Generation

## Model Training

Models Evaluated:

- Logistic Regression
- K-Nearest Neighbors
- Support Vector Machine
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting

Best model is automatically selected based on evaluation metrics.

---

## 📊 Model Performance

### Best Model

```text
Logistic Regression
```

### Training Metrics

| Metric | Score |
|----------|----------|
| Precision | 0.929 |
| Recall | 0.949 |
| F1 Score | 0.939 |

### Test Metrics

| Metric | Score |
|----------|----------|
| Precision | 0.920 |
| Recall | 0.931 |
| F1 Score | 0.926 |

The small gap between training and testing performance indicates strong generalization and limited overfitting.

---

# 🔬 Experiment Tracking

The project integrates:

## MLflow

Used for:

- Parameter Logging
- Metric Logging
- Artifact Tracking
- Model Tracking

## DagsHub

Used for:

- Experiment Visualization
- MLflow Backend
- Remote Tracking

---

# ☁️ AWS Integration

## AWS S3

Stores:

- Models
- Preprocessors
- Training Artifacts
- Logs

## AWS ECR

Stores:

- Docker Images

## AWS EC2

Hosts:

- FastAPI Service
- Docker Containers

---

# 🐳 Docker Support

Build Image

```bash
docker build -t network-security-classifier -f ml-services/Dockerfile ml-services
```

Run Container

```bash
docker run -p 8000:8000 network-security-classifier
```

---

# 🚀 API Endpoints

## Home

```http
GET /
```

Redirects to Swagger Documentation.

---

## Train Model

```http
GET /train
```

Triggers:

- Data Ingestion
- Validation
- Transformation
- Training
- Evaluation

---

## Predict

```http
POST /predict
```

### Request

CSV File Upload

### Response

```json
{
  "total_records": 10,
  "legitimate_count": 7,
  "phishing_count": 3,
  "results": [
    {
      "prediction": "Legitimate",
      "confidence": 99.23
    }
  ]
}
```

---

# 💻 Frontend

The React frontend provides:

- CSV Upload Interface
- Prediction Dashboard
- Summary Statistics
- Confidence Scores
- Batch Prediction Results

---

# ⚙️ CI/CD Pipeline

Implemented using GitHub Actions.

Workflow:

```text
GitHub Push
      │
      ▼

GitHub Actions
      │
      ▼

Docker Build
      │
      ▼

AWS ECR Push
      │
      ▼

AWS EC2 Deployment
```

---

# 🛠️ Tech Stack

## Frontend

- React
- Axios
- CSS

## Backend

- FastAPI
- Uvicorn

## Machine Learning

- Scikit-Learn
- Pandas
- NumPy

## Database

- MongoDB

## Experiment Tracking

- MLflow
- DagsHub

## Cloud

- AWS S3
- AWS ECR
- AWS EC2

## DevOps

- Docker
- GitHub Actions

---

# 🔮 Future Improvements

- Real-time URL Prediction
- Explainable AI (SHAP)
- Model Monitoring
- Drift Detection
- Automated Retraining
- Kubernetes Deployment
- Multi-Model Ensemble
- User Authentication

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Raj Aryan Tiwari

Bachelor of Technology

Machine Learning | MLOps | Full Stack Development | Cloud Computing

---