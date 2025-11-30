import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

HeartDisease = pd.read_csv("heart.csv")
HeartDisease = HeartDisease.replace('?', np.nan)
HeartDisease = HeartDisease.dropna()
HeartDisease = HeartDisease.astype(int)

print("Sample instances from the dataset are given below:")
print(HeartDisease.head())

print("\nAttributes and datatypes")
print(HeartDisease.dtypes)

model = BayesianModel([
    ('age', 'heartdisease'),
    ('sex', 'heartdisease'),
    ('exang', 'heartdisease'),
    ('cp', 'heartdisease'),
    ('heartdisease', 'restecg'),
    ('heartdisease', 'chol')
])

model.fit(HeartDisease, estimator=MaximumLikelihoodEstimator)

print('\nInferencing with Bayesian Network:')
infer = VariableElimination(model)

print('\n1. Probability of heartdisease given evidence = restecg')
q1 = infer.query(variables=['heartdisease'], evidence={'restecg': 1})
print(q1)

print('\n2. Probability of heartdisease given evidence = cp')
q2 = infer.query(variables=['heartdisease'], evidence={'cp': 2})
print(q2)
