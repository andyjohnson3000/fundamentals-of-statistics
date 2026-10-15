"""The maximum of n uniforms piles up at 1 (left); magnified by n, the gap 1 - max
has an Expo(1) limit (right)."""
from _style import *

n, reps = 50, 20000
r = rng(3)
U = r.uniform(size=(reps, n))
M = U.max(axis=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL)
ax1.hist(M, bins=60, range=(0.8, 1.0), density=True, color=BLUE, alpha=0.55, lw=0)
x = np.linspace(0.8, 1.0, 500)
ax1.plot(x, n * x ** (n - 1), color=INK, lw=1.0, label=r"exact density $n x^{n-1}$")
ax1.set_title(rf"$X_{{(n)}} = \max_i X_i$ for $n = {n}$")
ax1.set_xlabel(r"$X_{(n)}$")
ax1.set_ylabel("density")
ax1.legend(loc="upper left")

G = n * (1 - M)
ax2.hist(G, bins=60, range=(0, 6), density=True, color=BLUE, alpha=0.55, lw=0,
         label=rf"simulated, $n={n}$")
g = np.linspace(0, 6, 500)
ax2.plot(g, np.exp(-g), color=ORANGE, lw=1.4, label=r"Expo(1) density $e^{-x}$")
ax2.set_title(r"$n\,(1 - X_{(n)})$ and its limit")
ax2.set_xlabel(r"$n\,(1 - X_{(n)})$")
ax2.legend()
save(fig, "fig_max_uniform_expo")
