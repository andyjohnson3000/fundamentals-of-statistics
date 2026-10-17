"""Power of four tests of H0: the data are Gauss(0, 1), with n = 50, each
at exact level 5% (thresholds from 40,000 samples under the null). The tests:
Kolmogorov-Smirnov (blue, solid), Anderson-Darling (orange, dashed), and
Pearson's chi-squared test on the counts in 4 (aqua, dash-dot) or 10
(yellow, dotted) cells that are equally likely under the null. Left: data
from Gauss(delta, 1), against the shift delta. Right: data from
Gauss(0, s^2), against the standard deviation s. Each point is the
rejection rate in 10,000 samples."""
from _style import *

g = rng(1952)  # the year of Anderson and Darling's paper
n = 50
i = np.arange(1, n + 1)
erf = np.frompyfunc(math.erf, 1, 1)


def Phi(x):
    return 0.5 * (1 + erf(np.asarray(x) / math.sqrt(2)).astype(float))


def statistics(U):
    U = np.sort(U, axis=1)
    ks = np.maximum((i / n - U).max(1), (U - (i - 1) / n).max(1))
    Uc = np.clip(U, 1e-12, 1 - 1e-12)
    ad = -n - ((2 * i - 1) * (np.log(Uc) + np.log(1 - Uc[:, ::-1]))).sum(1) / n
    out = {"KS": ks, "AD": ad}
    for K in (4, 10):
        C = np.stack([((U >= k / K) & (U < (k + 1) / K)).sum(1) for k in range(K)], 1)
        out["chi%d" % K] = ((C - n / K) ** 2 / (n / K)).sum(1)
    return out


null = statistics(g.random((40000, n)))
crit = {k: np.quantile(v, 0.95) for k, v in null.items()}
style = {"KS": (BLUE, DASHES[0]), "AD": (ORANGE, DASHES[1]), "chi4": (AQUA, DASHES[2]), "chi10": (YELLOW, DASHES[3])}
deltas = np.linspace(0, 0.8, 17)
sds = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.35, 1.5, 1.65, 1.8, 2.0])
M = 10000
pw_shift = {k: [] for k in crit}
pw_scale = {k: [] for k in crit}
for d in deltas:
    s = statistics(Phi(g.standard_normal((M, n)) + d))
    for k in crit:
        pw_shift[k].append((s[k] > crit[k]).mean())
for sd in sds:
    s = statistics(Phi(sd * g.standard_normal((M, n))))
    for k in crit:
        pw_scale[k].append((s[k] > crit[k]).mean())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
names = {"KS": "Kolmogorov--Smirnov".replace("--", "\u2013"), "AD": "Anderson\u2013Darling",
         "chi4": "chi-squared, 4 cells", "chi10": "chi-squared, 10 cells"}
handles = []
for k, (c, ls) in style.items():
    h, = ax1.plot(deltas, pw_shift[k], color=c, ls=ls, lw=1.3, label=names[k])
    ax2.plot(sds, pw_scale[k], color=c, ls=ls, lw=1.3)
    handles.append(h)
for ax in (ax1, ax2):
    ax.axhline(0.05, color=GRAY, lw=0.6, ls=DASHES[3])
    ax.set_ylim(0, 1.0)
ax1.set_xlim(0, 0.8)
ax1.set_xlabel(r"shift $\delta$"); ax1.set_ylabel("rejection rate")
ax1.set_title("the mean moves")
ax2.set_xlim(0.5, 2.0)
ax2.set_xlabel(r"standard deviation $s$")
ax2.set_title("the spread changes")
fig.legend(handles=handles, loc="outside lower center", ncol=4, fontsize=7.5, frameon=False)
save(fig, "fig_edf_power")
for k in crit:
    print(k, "crit", round(crit[k], 4), "shift 0.4:", round(pw_shift[k][8], 3), "sd 1.5:", round(pw_scale[k][9], 3), "sd 0.7:", round(pw_scale[k][2], 3))
print("label check, shift curves at 0.3:", {k: round(pw_shift[k][6], 3) for k in crit})
print("scale curves at 1.8:", {k: round(pw_scale[k][11], 3) for k in crit}, "at 0.6:", {k: round(pw_scale[k][1], 3) for k in crit})
