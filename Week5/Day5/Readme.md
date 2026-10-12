
# Student Performance Prediction

## Project Overview
This project uses machine learning to predict whether a student will pass or fail based on study hours, attendance, and previous exam scores.

## Problem Statement
The objective is to build and compare machine learning models to predict student performance using available student data.

## Dataset
The sample dataset contains the following features:

- **StudyHours:** Hours spent studying.
- **Attendance:** Student attendance percentage.
- **PreviousScore:** Previous examination score.
- **Pass:** Target variable (1 = Pass, 0 = Fail).

Note: This project uses a small sample dataset created for practice.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Jupyter Notebook
- Git and GitHub

## Data Preprocessing
- Separated features and target variable.
- Split data into training and testing sets.
- Scaled numerical features using StandardScaler.
- Prepared data for machine learning models.

## Machine Learning Models
1. Logistic Regression
2. Random Forest Classifier

## Evaluation Metrics
The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score

The model with the better test performance is selected.

## Project Workflow
1. Load the dataset.
2. Prepare features and target.
3. Split the dataset.
4. Preprocess the features.
5. Train two machine learning models.
6. Compare evaluation metrics.
7. Select the best-performing model.

## Project Files
- `student_performance.py` — Python implementation.
- `student_performance.ipynb` — Jupyter Notebook.
- `requirements.txt` — Required Python libraries.
- `README.md` — Project documentation.

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Python script:

```bash
python student_performance.py
```

Alternatively, open `student_performance.ipynb` in Jupyter Notebook and run the cells.

## Conclusion
This project demonstrates an end-to-end machine learning classification workflow, including preprocessing, model training, prediction, and evaluation. Logistic Regression and Random Forest are compared using test metrics to identify the better-performing model.

Since the dataset is small and illustrative, further evaluation on real-world data is required before using the model for actual student performance predictions.