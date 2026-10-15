"""Where the square root of n comes from. Every formula in the book divides
by sqrt(n), and the reason is cancellation. Left: twenty random walks, each
a running sum of n steps of +1 or -1 with equal probability, with the band
+/- sqrt(n) drawn over them. If the steps all pointed the same way the sum
would reach n (the dotted line); because they cancel, the sum typically
reaches only about sqrt(n). Right: the root-mean-square distance from zero, measured over 20,000
simulated walks, against sqrt(n) and against n on the same axes. The
simulation sits on sqrt(n) exactly (E[S_n^2] = n, since the cross terms
have expectation zero) and is nowhere near n."""
from _style import *

r = rng(11)
n_max = 400
steps = np.arange(1, n_max + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

# ---- left: twenty walks inside the sqrt(n) band
walks = r.choice([-1.0, 1.0], size=(20, n_max)).cumsum(1)
for w in walks:
    ax1.plot(steps, w, color=BLUE, lw=0.6, alpha=0.45)
ax1.plot(steps, np.sqrt(steps), color=ORANGE, lw=1.4)
ax1.plot(steps, -np.sqrt(steps), color=ORANGE, lw=1.4)
ax1.axhline(0, color=INK, lw=0.6)
ax1.set_xlim(0, n_max)
ax1.set_ylim(-70, 70)
ax1.set_xlabel(r"number of steps $n$")
ax1.set_ylabel(r"sum of the steps $S_n$")
ax1.set_title("Twenty walks, and the band $\\pm\\sqrt{n}$")
note(ax1, r"$\pm\sqrt{n}$", (300, math.sqrt(300)), (250, 48), ha="left", fontsize=8)
ax1.text(14, -62, "if the steps never cancelled,\n$S_n$ would reach $n$: off this plot\nby step 70", fontsize=7.5, color=INK, ha="left", va="bottom")

# ---- right: mean |S_n| against sqrt(n) and against n
reps = 20000
sub = np.array([1, 2, 3, 5, 8, 12, 20, 30, 50, 75, 110, 160, 220, 300, 400])
rms = []
for m in sub:
    w = r.choice([-1.0, 1.0], size=(reps, m)).sum(1)
    rms.append(math.sqrt((w ** 2).mean()))
rms = np.array(rms)
ax2.plot(steps, steps, color=GRAY, ls=DASHES[3], lw=1.0)
ax2.plot(steps, np.sqrt(steps), color=ORANGE, lw=1.4)
ax2.plot(sub, rms, "o", ms=3.5, color=BLUE, mec="white", mew=0.4, zorder=5)
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlim(1, n_max * 1.1)
ax2.set_ylim(0.7, n_max * 1.3)
ax2.set_xlabel(r"$n$ (log scale)")
ax2.set_ylabel("root-mean-square distance from $0$")
ax2.set_title("What the simulation actually does")
note(ax2, "no cancellation: $n$", (90, 90), (1.6, 190), ha="left", fontsize=7.5)
note(ax2, r"$\sqrt{n}$", (220, math.sqrt(220)), (300, 5.0), ha="right", fontsize=7.5)
ax2.text(1.4, 1.6, "simulated walks,\n20,000 each", fontsize=7.5, color=INK, ha="left", va="bottom")
save(fig, "fig_why_root_n")
print("rms at n = 400:", round(rms[-1], 3), " sqrt(400) = 20.0",
      " ratio:", round(rms[-1] / 20.0, 4))
