# Week 7 / Day 1: Neural Network Projects

## Overview

This project introduces Artificial Neural Networks (ANNs), builds a basic Multi-Layer Perceptron (MLP) classifier, and explores how activation functions, hidden-layer configurations, and training epochs affect model performance.

## Project 1: Neural Network Introduction

### Objective
Understand the fundamentals of artificial neural networks and build a simple MLP classifier.

### Dataset
Breast Cancer Wisconsin dataset from Scikit-learn.

### Concepts Covered
- Artificial Neural Networks (ANN)
- Neurons, weights, and biases
- Input, hidden, and output layers
- ReLU activation function
- Backpropagation and Adam optimizer
- Model evaluation

### Implementation Steps
1. Load the breast cancer dataset.
2. Split the data into training and testing sets.
3. Standardize the input features.
4. Build an MLP classifier with hidden layers containing 16 and 8 neurons.
5. Train the model and generate predictions.
6. Evaluate performance using accuracy, precision, recall, F1-score, and a confusion matrix.

### Expected Outcome
Understand how a neural network learns patterns from data and predicts whether a tumor is malignant or benign.

---

## Project 2: Perceptron or MLP Basics

### Objective
Build a basic Multi-Layer Perceptron classifier using a small classification dataset.

### Dataset
Iris dataset from Scikit-learn.

### Model Configuration
- Input features: 4
- Hidden layers: 1
- Hidden neurons: 10
- Activation function: ReLU
- Optimizer: Adam
- Maximum iterations: 1,000
- Output classes: 3

### Implementation Steps
1. Load the Iris dataset.
2. Divide the dataset into training and testing sets.
3. Standardize the features using StandardScaler.
4. Create an MLP classifier.
5. Train the model using the training data.
6. Predict the flower species using the test data.
7. Evaluate the model using accuracy, precision, recall, F1-score, and a confusion matrix.

### Expected Outcome
Understand how an MLP learns relationships between flower measurements and classifies flowers into three species.

---

## Project 3: Activation and Epoch Observation

### Objective
Experiment with different activation functions, hidden-layer sizes, and training iterations to observe their effects on MLP performance.

### Dataset
Iris dataset from Scikit-learn.

### Experiments

| Experiment | Hidden Layers | Activation | Maximum Iterations |
|---|---|---|---|
| 1 | (5,) | ReLU | 50 |
| 2 | (10,) | ReLU | 100 |
| 3 | (20,) | ReLU | 200 |
| 4 | (10,) | tanh | 100 |
| 5 | (10, 5) | ReLU | 200 |

### Implementation Steps
1. Load and split the Iris dataset.
2. Standardize the input features.
3. Train multiple MLP models using different configurations.
4. Record the actual training iterations for each model.
5. Calculate the test accuracy for each experiment.
6. Compare the results and identify the best-performing configuration.

### Expected Outcome
Understand how model architecture and activation functions influence training and classification performance.

### Observations
- Increasing the number of hidden neurons does not always improve accuracy.
- More training iterations can help the model learn, but do not guarantee better test performance.
- ReLU and tanh may produce different results.
- Deeper networks can learn more complex patterns but may require additional tuning.
- The best configuration should be selected using evaluation results rather than assumptions.

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

## Installation

Install the required libraries:

```bash
pip install numpy pandas scikit-learn matplotlib
```

## Project Folder Structure

```text
Week7/
├── Day1_NeuralNetworkIntro/
│   └── neural_network_intro.py
├── Day1_MLPBasics/
│   └── mlp_basics.py
├── Day1_MLPExperiments/
│   └── mlp_experiments.py
└── README.md
```

## How to Run

Run each Python program from the terminal:

```bash
python Day1_NeuralNetworkIntro/neural_network_intro.py
python Day1_MLPBasics/mlp_basics.py
python Day1_MLPExperiments/mlp_experiments.py
```