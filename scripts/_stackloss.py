"""Loads Brownlee's stack loss data: 21 days of a plant oxidizing ammonia to
nitric acid. air = air flow, water = cooling water inlet temperature, acid =
acid concentration (coded), loss = stack loss (ten times the percentage of
ammonia escaping)."""
import csv, os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))


def stackloss():
    rows = list(csv.DictReader(open(os.path.join(os.path.dirname(_HERE), "data", "stackloss.csv"))))
    X = np.array([[1.0, float(r["air"]), float(r["water"]), float(r["acid"])] for r in rows])
    y = np.array([float(r["loss"]) for r in rows])
    return X, y


def lse(X, y):
    b = np.linalg.solve(X.T @ X, X.T @ y)
    r = y - X @ b
    return b, r
