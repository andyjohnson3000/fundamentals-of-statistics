"""The kiss data's log-likelihood (124 couples, 80 right turns), measured
from its maximum, on two scales. Left: against p, with the maximum at
p-hat = 0.645. Right: against the canonical parameter theta = log-odds,
with the maximum at theta-hat = 0.598 and the quadratic approximation
-n p-hat(1 - p-hat)(theta - theta-hat)^2/2 (orange, dashed) that the
curvature b''(theta-hat) = 0.229 gives."""
from _style import *

n, s = 124, 80
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
p = np.linspace(0.35, 0.9, 400)
ll = s * np.log(p) + (n - s) * np.log(1 - p); ll -= ll.max()
ax1.plot(p, ll, color=BLUE, lw=1.4)
ax1.plot(p, -n / ((s / n) * (1 - s / n)) * (p - s / n) ** 2 / 2, color=ORANGE, lw=1.1, ls=DASHES[1])
ax1.axvline(s / n, color=GRAY, lw=0.8, ls=":")
ax1.set_ylim(-14, 1); ax1.set_xlabel("$p$"); ax1.set_ylabel("log-likelihood, from its maximum")
ax1.set_title("on the scale of $p$")
th = np.linspace(-1.0, 2.2, 400); ph = s / n; th0 = np.log(ph / (1 - ph))
ll2 = s * th - n * np.log1p(np.exp(th)); ll2 -= ll2.max()
ax2.plot(th, ll2, color=BLUE, lw=1.4)
ax2.plot(th, -n * ph * (1 - ph) * (th - th0) ** 2 / 2, color=ORANGE, lw=1.1, ls=DASHES[1])
ax2.axvline(th0, color=GRAY, lw=0.8, ls=":")
ax2.set_ylim(-14, 1); ax2.set_xlabel(r"$\theta$ (log-odds)")
ax2.set_title(r"on the scale of $\theta$")
save(fig, "fig_ef_kiss_loglik")
print("theta hat", th0, "n p(1-p)", n * ph * (1 - ph), "se", 1 / np.sqrt(n * ph * (1 - ph)))
