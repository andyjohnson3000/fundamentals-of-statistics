"""Three losses and the three averages they define. Left: the losses
rho(x - mu) as functions of the residual x - mu: squared (blue), absolute
(orange, dashed) and Huber with delta = 1 (aqua, dash-dot), which is
quadratic inside [-1, 1] and linear outside. Right: the empirical loss
(1/n) sum rho(X_i - mu) for the 272 Old Faithful waits, each curve shifted
to have minimum 0; the squared loss is minimized at the mean 70.9, the
absolute loss at the median 76, Huber's loss (delta = 5 minutes) at 75.0."""
from _style import *
import csv, os

w = np.array([float(r["waiting"]) for r in csv.DictReader(open(os.path.join(os.path.dirname(HERE), "data", "old_faithful.csv")))])
def huber(r, d):
    a = np.abs(r)
    return np.where(a <= d, 0.5 * r ** 2, d * (a - 0.5 * d))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
r = np.linspace(-3, 3, 400)
ax1.plot(r, 0.5 * r ** 2, color=BLUE, lw=1.3)
ax1.plot(r, np.abs(r), color=ORANGE, lw=1.3, ls=DASHES[1])
ax1.plot(r, huber(r, 1.0), color=AQUA, lw=1.3, ls=DASHES[2])
ax1.set_xlim(-3, 3); ax1.set_ylim(0, 4.6)
ax1.set_xlabel(r"residual $x - \mu$"); ax1.set_ylabel(r"$\rho(x - \mu)$")
ax1.set_title("three losses")
ax1.text(0, 4.45, r"squared $\frac{1}{2}(x-\mu)^2$", color=BLUE, fontsize=7.5, va="top", ha="center")
ax1.text(0, 4.05, r"absolute $|x - \mu|$", color=ORANGE, fontsize=7.5, va="top", ha="center")
ax1.text(0, 3.65, r"Huber, $\delta = 1$", color=AQUA, fontsize=7.5, va="top", ha="center")

mu = np.linspace(60, 85, 500)
sq = np.array([np.mean(0.5 * (w - m) ** 2) for m in mu]); sq -= sq.min()
ab = np.array([np.mean(np.abs(w - m)) for m in mu]); ab -= ab.min()
hu = np.array([np.mean(huber(w - m, 5.0)) for m in mu]); hu -= hu.min()
ax2.plot(mu, sq, color=BLUE, lw=1.3)
ax2.plot(mu, ab, color=ORANGE, lw=1.3, ls=DASHES[1])
ax2.plot(mu, hu, color=AQUA, lw=1.3, ls=DASHES[2])
for m, c in [(w.mean(), BLUE), (np.median(w), ORANGE), (mu[np.argmin(hu)], AQUA)]:
    ax2.plot([m], [0], "o", ms=4, color=c, zorder=5, clip_on=False)
ax2.set_xlim(60, 85); ax2.set_ylim(0, 60)
ax2.set_xlabel(r"$\mu$ (minutes)"); ax2.set_ylabel("empirical loss, from its minimum")
ax2.set_title("Old Faithful: three minimizers")
ax2.text(72, 58, "minimizers (dots):\nmean $70.9$, blue\nmedian $76$, orange\nHuber $75.0$, aqua", fontsize=7.5, color=INK, va="top", ha="center")
save(fig, "fig_mestimation_losses")
print(w.mean(), np.median(w), mu[np.argmin(hu)])
