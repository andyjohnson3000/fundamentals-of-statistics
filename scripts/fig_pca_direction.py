"""The sample variance of the projection u^T Z_i onto the unit vector
u = (cos t, sin t), as a function of the angle t, for the standardized Old
Faithful data: u^T S u = 1 + 0.90 sin 2t, largest (1.90) at 45 degrees and
smallest (0.10) at 135 degrees."""
from _style import *
from _faithful import faithful

x, y = faithful(); X = np.column_stack([x, y]); Z = (X - X.mean(0)) / X.std(0); S = Z.T @ Z / len(x)
t = np.linspace(0, 180, 361); u = np.column_stack([np.cos(np.radians(t)), np.sin(np.radians(t))])
v = np.einsum("ij,jk,ik->i", u, S, u)
fig, ax = plt.subplots(figsize=(4.6, 2.9), layout="constrained")
ax.plot(t, v, color=BLUE, lw=1.4)
ax.axhline(1.0, color=GRAY, lw=0.6, ls=":")
ax.plot([45], [v.max()], "o", color=ORANGE, ms=4); ax.plot([135], [v.min()], "o", color=AQUA, ms=4)
ax.text(45, 2.0, r"$45^\circ$: $\lambda_1 = 1.90$", color=ORANGE, fontsize=8, ha="center")
ax.text(135, 0.42, r"$135^\circ$: $\lambda_2 = 0.10$", color=AQUA, fontsize=8, ha="center")
ax.text(176, 1.06, "average over directions: 1", color=GRAY, fontsize=7.5, ha="right")
ax.set_xticks([0, 45, 90, 135, 180]); ax.set_xlabel("direction $u$ (degrees from the duration axis)")
ax.set_ylabel(r"sample variance of $u^\top Z_i$"); ax.set_ylim(0, 2.2)
ax.set_title("how spread depends on direction")
save(fig, "fig_pca_direction")
