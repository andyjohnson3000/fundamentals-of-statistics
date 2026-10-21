"""Loads the kyphosis data (Chambers and Hastie, Statistical Models in S,
1992): 81 children after corrective spinal surgery. kyphosis = 1 if a
postoperative deformity was present, age in months, number of vertebrae
involved, start = the first (topmost) vertebra operated on."""
import csv, os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))


def kyphosis():
    rows = list(csv.DictReader(open(os.path.join(os.path.dirname(_HERE), "data", "kyphosis.csv"))))
    y = np.array([float(r["kyphosis"]) for r in rows])
    X = np.array([[1.0, float(r["age"]), float(r["number"]), float(r["start"])] for r in rows])
    return X, y


def logistic_fit(X, y, iterations=25):
    """Newton's method for logistic regression from beta = 0. Returns the
    estimate, its standard errors, the maximized log-likelihood and the
    list of (log-likelihood, beta) at each iteration."""
    b = np.zeros(X.shape[1]); hist = []
    for _ in range(iterations):
        eta = X @ b; p = 1 / (1 + np.exp(-eta))
        hist.append(((y * eta - np.log1p(np.exp(eta))).sum(), b.copy()))
        b = b + np.linalg.solve(X.T @ (X * (p * (1 - p))[:, None]), X.T @ (y - p))
    eta = X @ b; p = 1 / (1 + np.exp(-eta))
    cov = np.linalg.inv(X.T @ (X * (p * (1 - p))[:, None]))
    return b, np.sqrt(np.diag(cov)), (y * eta - np.log1p(np.exp(eta))).sum(), hist
