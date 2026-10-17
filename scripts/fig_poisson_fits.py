"""Testing a Poisson model with lambda estimated. Left: von Bortkiewicz's
deaths by horse kick in 10 Prussian army corps over 20 years (200
corps-years): the number of corps-years with 0, 1, 2, 3 and 4 or more
deaths (blue bars: 109, 65, 22, 3, 1) and the counts expected under
Pois(0.61), 0.61 being the mean number of deaths (black ticks). Right: the
siblings data, n = 24 students, the number of siblings minus one (blue
bars: 8, 9, 6, 1 for 0, 1, 2, 3 or more) and the counts expected under
Pois(1.0), 1.0 being the sample mean (black ticks)."""
from _style import *


def pois_pmf(k, lam):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def expected(n, lam, kmax):
    p = [pois_pmf(k, lam) for k in range(kmax)]
    p.append(1 - sum(p))  # the last cell is "kmax or more"
    return n * np.array(p)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
for ax, obs, lam, labels, ylab, title, top in [
        (ax1, np.array([109, 65, 22, 3, 1]), 0.61, ["0", "1", "2", "3", "4+"],
         "number of corps-years", "horse kicks, 200 corps-years", 125),
        (ax2, np.array([8, 9, 6, 1]), 1.0, ["0", "1", "2", "3+"],
         "number of students", "siblings minus one, 24 students", 11.5)]:
    e = expected(obs.sum(), lam, len(obs) - 1)
    x = np.arange(len(obs))
    ax.bar(x, obs, width=0.6, color=BLUE, alpha=0.75, edgecolor="none")
    for xi, ei in zip(x, e):
        ax.plot([xi - 0.36, xi + 0.36], [ei, ei], color=INK, lw=1.6, solid_capstyle="butt")
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylim(0, top)
    ax.set_ylabel(ylab); ax.set_title(title)
    print(title, "observed", obs, "expected", np.round(e, 2))
ax1.set_xlabel("deaths in a corps-year")
ax2.set_xlabel("siblings minus one")
note(ax1, r"expected under $\mathrm{Pois}(0.61)$", (1.36, 66.3), (1.9, 95), ha="left")
note(ax2, r"expected under $\mathrm{Pois}(1.0)$", (3.36, 1.93), (1.75, 10.6), ha="left")
save(fig, "fig_poisson_fits")
