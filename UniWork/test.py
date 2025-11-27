n = len(tr_y)
deg_list, redchi2, bic = [], [], []
for deg in range(1, 10):
    p = np.polyfit(Xtr, tr_y, deg)
    fit = np.polyval(p, Xtr)
    rss = np.sum((tr_y - fit)**2)
    rss = max(rss, 1e-12)              # guard for exact fit
    p_params = deg + 1                  # coefficients incl. intercept
    dof = max(n - p_params, 1)          # avoid zero/negative dof for high deg
    redchi2.append(rss / dof)
    bic.append(n * np.log(rss / n) + p_params * np.log(n))
    deg_list.append(deg)

print("\nModel testing (training set):")
for d, rc2, b in zip(deg_list, redchi2, bic):
    print(f"deg={d}: reduced chi^2={rc2:.3f}, BIC={b:.3f}")
best_bic_deg = deg_list[int(np.argmin(bic))]
best_rc2_deg = deg_list[int(np.argmin(redchi2))]
print(f"Best by BIC: degree {best_bic_deg}")
print(f"Best by reduced chi^2: degree {best_rc2_deg}")

plt.figure(figsize=(9,4))
plt.plot(deg_list, redchi2, 'o-', label='reduced chi^2')
plt.plot(deg_list, bic, 'o-', label='BIC')
plt.xlabel('Polynomial degree'); plt.grid(True, alpha=0.3)
plt.title('Model testing metrics (training fit)')
plt.legend(); plt.tight_layout(); plt.show()