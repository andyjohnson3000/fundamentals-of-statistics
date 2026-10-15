"""The EM algorithm on the 272 waiting times between eruptions of Old Faithful
(Yellowstone). Left: the histogram (density scale) with the fitted
two-component mixture: weight 0.36 on Gauss(54.6, 5.87^2) and 0.64 on
Gauss(80.1, 5.87^2) (the two standard deviations agree to two decimals).
Right: the log-likelihood at the start and after each EM step, from three different
starting points; it never decreases, and all three runs reach -1034.0,
far above the single best Gaussian's -1095.3."""
from _style import *
import csv, os
from math import pi as PI

w = []
with open(os.path.join(os.path.dirname(HERE), "data", "old_faithful.csv")) as f:
    for row in csv.DictReader(f):
        w.append(float(row["waiting"]))
w = np.array(w)

def em(mu1, mu2, s1=10.0, s2=10.0, p=0.5, it=40):
    ll = []
    for _ in range(it):
        a = p * norm_pdf(w, mu1, s1); b = (1 - p) * norm_pdf(w, mu2, s2)
        ll.append(np.log(a + b).sum())
        r = a / (a + b)
        p = r.mean(); mu1 = (r * w).sum() / r.sum(); mu2 = ((1 - r) * w).sum() / (1 - r).sum()
        s1 = np.sqrt((r * (w - mu1) ** 2).sum() / r.sum()); s2 = np.sqrt(((1 - r) * (w - mu2) ** 2).sum() / (1 - r).sum())
    return (p, mu1, mu2, s1, s2), ll

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
(pp, m1, m2, s1, s2), _ = em(50, 70, it=300)
ax1.hist(w, bins=np.arange(40, 100, 2.5), density=True, color=GRAY, alpha=0.35, edgecolor="white", lw=0.5)
x = np.linspace(40, 100, 600)
ax1.plot(x, pp * norm_pdf(x, m1, s1) + (1 - pp) * norm_pdf(x, m2, s2), color=BLUE, lw=1.4)
ax1.plot(x, norm_pdf(x, w.mean(), w.std()), color=ORANGE, lw=1.2, ls=DASHES[1])
ax1.set_xlabel("minutes between eruptions"); ax1.set_yticks([])
ax1.set_title("Old Faithful: data and two fits")
ax1.set_ylim(0, 0.052)
ax1.text(41, 0.05, "mixture of two Gaussians (EM)", color=BLUE, fontsize=7.5, va="top")
ax1.text(41, 0.045, "single Gaussian", color=ORANGE, fontsize=7.5, va="top")

for (a, b), c, ls in [((50, 70), BLUE, "-"), ((40, 95), AQUA, DASHES[2]), ((65, 75), YELLOW, DASHES[1])]:
    _, ll = em(a, b, it=25)
    ax2.plot(range(0, 25), ll, color=c, lw=1.3, ls=ls, marker="o", ms=2)
ax2.axhline(-1095.29, color=ORANGE, lw=0.8, ls=DASHES[1])
ax2.set_xlabel("EM steps completed"); ax2.set_ylabel("log-likelihood")
ax2.set_title("each step raises the log-likelihood")
ax2.set_ylim(-1420, -1010)
ax2.text(24, -1102, "best single Gaussian, $-1095.3$", fontsize=7.5, color=ORANGE, ha="right", va="top")
save(fig, "fig_em_faithful")
print(pp, m1, m2, s1, s2)
