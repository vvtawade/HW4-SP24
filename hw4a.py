from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


mu_1 = 0  # Mean 1
sigma_1 = 1  # Variance 1
dist_1 = stats.norm(mu_1, sigma_1)  # Produces a normal continuous distribution with the given parameters

x_values1 = np.linspace(-5, 5, 1000)  # Assigns evenly spaced x values
pdf_1 = dist_1.pdf(x_values1)  # Produces probability density function for 1
cdf_1 = dist_1.cdf(x_values1)  # Produces cumulative distribution function for 1

mu_2 = 175  # Mean 2
sigma_2 = 3  # Variance 2
dist_2 = stats.norm(mu_2, sigma_2)  # Produces a normal continuous distribution with the given parameters

x_values2 = np.linspace(160, 190, 1000)  # Assigns evenly spaced x values
pdf_2 = dist_2.pdf(x_values2)  # Produces probability density function for 2
cdf_2 = dist_2.cdf(x_values2)  # Produces cumulative distribution function for 2

# PLOTS SECTION

fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # Assigns subplots to plot

# Plots pdf for 1
axes[0, 0].plot(x_values1, pdf_1, label='PDF')
axes[0, 0].fill_between(x_values1, pdf_1, where=(x_values1 < 1), color='skyblue', alpha=0.4, label='P(x < 1)')
axes[0, 0].axvline(1, color='red', linestyle='dashed', label='x = 1')
axes[0, 0].set_title('PDF for P(x < 1 | N(0, 1))')
axes[0, 0].legend()

# Plots cdf for 1
axes[1, 0].plot(x_values1, cdf_1, label='CDF')
axes[1, 0].axvline(1, color='red', linestyle='dashed', label='x = 1')
axes[1, 0].axhline(dist_1.cdf(1), color='green', linestyle='dashed', label='y = P(x < 1)')
axes[1, 0].set_title('CDF for P(x < 1 | N(0, 1))')
axes[1, 0].legend()

# Plots pdf for 2
axes[0, 1].plot(x_values2, pdf_2, label='PDF')
axes[0, 1].fill_between(x_values2, pdf_2, where=(x_values2 > (mu_2 + 2 * sigma_2)), color='lightcoral', alpha=0.4,
                        label='P(x > μ + 2σ)')
axes[0, 1].axvline(mu_2 + 2 * sigma_2, color='blue', linestyle='dashed', label='μ + 2σ')
axes[0, 1].set_title('PDF for P(x > μ + 2σ | N(175, 3))')
axes[0, 1].legend()

# Plots cdf for 2
axes[1, 1].plot(x_values2, cdf_2, label='CDF')
axes[1, 1].axvline(mu_2 + 2 * sigma_2, color='blue', linestyle='dashed', label='μ + 2σ')
axes[1, 1].axhline(dist_2.cdf(mu_2 + 2 * sigma_2), color='green', linestyle='dashed', label='y = P(x > μ + 2σ)')
axes[1, 1].set_title('CDF for P(x > μ + 2σ | N(175, 3))')
axes[1, 1].legend()

plt.xlabel('x')  # Labels x axis
plt.tight_layout()
plt.show()  # Show plot
