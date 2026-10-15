"""Why the MLE is asymptotically normal: the score is an average. Left: the
log-likelihood of one couple's turn, two curves (R = 1 and R = 0), and the
slope of each at p* = 0.645, which is the score: +1.55 for a right turn,
-2.82 for a left turn. Under p* the score averages to 0 and has variance
I(p*) = 4.37. Middle: the average score (1/n) l_n'(p*) over 20,000 simulated
studies of 124 couples, with the Gaussian N(0, I(p*)/n) the CLT predicts
(sd 0.188). Right: the same 20,000 studies' p-hat, with the Gaussian
N(p*, 1/(n I(p*))) the theorem predicts (sd 0.043). The two panels are the
same histogram under a change of scale: p-hat - p* is approximately the
average score divided by I(p*)."""
from _style import *

ps, n = 0.645, 124
r = rng(5)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6.0, 2.5), layout="constrained")
p = np.linspace(0.3, 0.95, 400)
ax1.plot(p, np.log(p), color=BLUE, lw=1.2)
ax1.plot(p, np.log(1 - p), color=ORANGE, lw=1.2, ls=DASHES[1])
for f, df, c in [(np.log(ps), 1 / ps, BLUE), (np.log(1 - ps), -1 / (1 - ps), ORANGE)]:
    t = np.linspace(ps - 0.12, ps + 0.12, 20)
    ax1.plot(t, f + df * (t - ps), color=INK, lw=1.0)
ax1.plot([ps, ps], [np.log(ps), np.log(1 - ps)], "o", ms=3.5, color=INK, zorder=5)
ax1.axvline(ps, color=INK, lw=0.5, ls=":")
ax1.set_xlim(0.3, 0.95); ax1.set_ylim(-2.6, 0.45)
ax1.set_xlabel(r"$p$"); ax1.set_title(r"slopes at $p^*$: the score")
ax1.text(0.32, 0.42, r"$R = 1$: slope $+1.55$", color=BLUE, fontsize=7.5, va="top")
ax1.text(0.32, -2.5, r"$R = 0$: slope $-2.82$", color=ORANGE, fontsize=7.5, va="bottom", ha="left")

sims = r.binomial(n, ps, 20000) / n
score = sims / ps - (1 - sims) / (1 - ps)
I = 1 / (ps * (1 - ps))
edges = (np.arange(0, n + 2) - 0.5) / n; edges = edges / ps - (1 - edges) / (1 - ps)
ax2.hist(score, bins=edges, density=True, color=AQUA, alpha=0.5, edgecolor="none")
x = np.linspace(-0.9, 0.9, 300)
ax2.plot(x, norm_pdf(x, 0, np.sqrt(I / n)), color=INK, lw=1.2)
ax2.set_yticks([]); ax2.set_xlim(-0.9, 0.9)
ax2.set_xlabel(r"average score at $p^*$, $n = 124$")
ax2.set_title(r"CLT: $\mathrm{Gauss}(0, I(p^*)/n)$")

ax3.hist(sims, bins=np.arange(0.45, 0.85, 0.008), density=True, color=BLUE, alpha=0.5, edgecolor="none")
x = np.linspace(0.45, 0.85, 300)
ax3.plot(x, norm_pdf(x, ps, 1 / np.sqrt(n * I)), color=INK, lw=1.2)
ax3.set_yticks([]); ax3.set_xlim(0.45, 0.85)
ax3.set_xlabel(r"$\hat p$, $n = 124$")
ax3.set_title(r"MLE: $\mathrm{Gauss}(p^*, 1/(nI(p^*)))$")
save(fig, "fig_score_clt")
print(score.std(), np.sqrt(I / n), sims.std(), 1 / np.sqrt(n * I))
