"""Loads the 272 Old Faithful eruptions: x = eruption duration (minutes),
y = waiting time to the next eruption (minutes)."""
import csv, os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))


def faithful():
    x, y = [], []
    with open(os.path.join(os.path.dirname(_HERE), "data", "old_faithful.csv")) as f:
        for row in csv.DictReader(f):
            x.append(float(row["eruptions"]))
            y.append(float(row["waiting"]))
    return np.array(x), np.array(y)


def fit(x, y):
    xb, yb = x.mean(), y.mean()
    sxx = ((x - xb) ** 2).sum()
    b = ((x - xb) * (y - yb)).sum() / sxx
    a = yb - b * xb
    return a, b, sxx
