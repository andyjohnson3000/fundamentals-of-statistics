"""Shared plotting style for every figure in the book.

Every figure script does ``from _style import *`` and gets:
  - a fixed four-color categorical palette (colorblind-checked),
    always used in the same order, plus a neutral gray
  - serif fonts and Computer Modern math, to sit well in a LaTeX page
  - thin lines, no top/right spines, light grid
  - ``save(fig, name)`` which writes figures/<name>.pdf

House rules for a publication-quality figure (checked by rasterizing the
PDF and looking at it; see README):
  1. No text over data. A label never crosses a curve, a bar, a band or a
     marker. Put it in empty space, with a thin gray leader if it is far
     from what it names (``note``), or at the end of its line in the
     margin (``end_label``). If there is no empty space, the label goes
     in the caption instead.
  2. Prefer direct labels to legends. When a legend is unavoidable, place
     it in a corner you have checked is empty, or below the axes
     (``legend_below``). Never let a legend box cover data.
  3. Text sizes: title 9.5, axis labels 9, ticks 8, annotations and
     legends 7.5. Figures are printed at about their drawn width, so
     these are the sizes on the page. Do not go below 7.
  4. Titles are short and state the message; numbers, formulas and the
     explanation go in the LaTeX caption.
  5. Multi-panel figures use ``layout="constrained"`` so axis labels of
     neighboring panels never collide.
  6. Keep the palette order (BLUE first, ORANGE second, ...) and pair every
     color with a line style so the figure still reads in grayscale.
"""
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(os.path.dirname(HERE), "figures")
os.makedirs(FIGDIR, exist_ok=True)

BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
GRAY, INK = "#6b6b6b", "#222222"
YELLOW_TEXT = "#a26d00"  # text that labels a yellow line: YELLOW itself is too light to read as text
SERIES = [BLUE, ORANGE, AQUA, YELLOW]
DASHES = ["-", "--", "-.", ":"]  # second channel, so print in black and white still reads

plt.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "cm",
    "font.size": 9,
    "axes.titlesize": 9.5,
    "axes.labelsize": 9,
    "legend.fontsize": 7.5,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#888888",
    "axes.linewidth": 0.6,
    "xtick.color": "#555555",
    "ytick.color": "#555555",
    "axes.grid": True,
    "grid.color": "#dddddd",
    "grid.linewidth": 0.5,
    "lines.linewidth": 1.4,
    "legend.frameon": False,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
})

FULL = (6.0, 2.9)      # full text width, one row
TALL = (6.0, 4.6)      # full text width, two rows
SINGLE = (3.6, 2.7)    # one small panel


def save(fig, name):
    path = os.path.join(FIGDIR, name + ".pdf")
    fig.savefig(path)
    plt.close(fig)
    print("wrote", os.path.relpath(path, os.path.dirname(HERE)))


def rng(seed=18650):
    return np.random.default_rng(seed)


# ---- small numerical helpers (numpy only, so the scripts run anywhere)

def norm_pdf(x, mu=0.0, sd=1.0):
    z = (np.asarray(x, float) - mu) / sd
    return np.exp(-0.5 * z * z) / (sd * math.sqrt(2 * math.pi))


def norm_cdf(x, mu=0.0, sd=1.0):
    z = (np.asarray(x, float) - mu) / (sd * math.sqrt(2))
    return 0.5 * (1 + np.vectorize(math.erf)(z))


def gamma_pdf(x, shape, rate):
    """Density of Gamma(shape, rate); the sample mean of n Exp(1) is Gamma(n, n)."""
    x = np.asarray(x, float)
    out = np.zeros_like(x)
    pos = x > 0
    lx = np.log(x[pos])
    out[pos] = np.exp(shape * math.log(rate) + (shape - 1) * lx - rate * x[pos] - math.lgamma(shape))
    return out


def gamma_tail_outside(shape, rate, lo, hi, grid=200000):
    """P(X < lo or X > hi) for X ~ Gamma(shape, rate), by numerical integration."""
    x = np.linspace(lo, hi, grid)
    f = gamma_pdf(x, shape, rate)
    inside = float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(x)))  # trapezoid rule, works on old and new numpy
    return 1.0 - inside


def binom_pmf(n, p):
    """pmf of Bin(n, p) on 0..n, computed on the log scale."""
    k = np.arange(n + 1)
    logc = np.array([math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) for i in k])
    return np.exp(logc + k * math.log(p) + (n - k) * math.log(1 - p))


def label_line(ax, x, y, text, color, dx=0, dy=0, ha="left", va="center"):
    """Direct label next to a curve, in ink color (not the series color)."""
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points",
                ha=ha, va=va, fontsize=8, color=INK)


def end_label(ax, x, y, text, color=INK, dx=4, dy=0, va="center"):
    """Label at the end of a line, just past its last point (Wilke's direct
    labeling). Extend xlim a little so the text has room."""
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points",
                ha="left", va=va, fontsize=7.5, color=color,
                annotation_clip=False)


def note(ax, text, xy, xytext, ha="left", va="center", leader=True, fontsize=7.5):
    """An annotation placed in empty space, with a thin gray leader to the
    point it names. ``xy`` is the data point, ``xytext`` where the text goes
    (data coordinates)."""
    ax.annotate(text, xy, xytext=xytext, ha=ha, va=va, fontsize=fontsize, color=INK,
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkB=2) if leader else None)


def legend_below(ax, ncol=3, **kw):
    """Legend in a row under the axes, outside the data area."""
    return ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=ncol,
                     fontsize=7.5, frameon=False, **kw)
