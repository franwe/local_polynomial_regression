import numpy as np
from matplotlib import pyplot as plt

from local_polynomial_regression.base import LocalPolynomialRegressionCV

np.random.seed(1)
X = np.linspace(-np.pi, np.pi, num=150)
y_real = np.sin(X)
y = np.random.normal(0, 0.5, len(X)) + y_real

# Bandwidth selection for local polynomial regression
model_cv = LocalPolynomialRegressionCV(
    X=X,
    y=y,
    h=0.75,
    kernel="gaussian",
    n_sections=15,
    loss="MSE",
    sampling="slicing",
)

results = model_cv.bandwidth_cv_sampling(np.linspace(0.4, 1.5, 10))

print(f"Optimal bandwidth: {results['h']}")
plt.plot(results["bandwidths"], results["MSE"])
plt.show()

results = model_cv.bandwidth_cv(np.linspace(0.4, 1.5, 10))
plt.plot(results["coarse results"]["bandwidths"], results["coarse results"]["MSE"])
plt.plot(results["fine results"]["bandwidths"], results["fine results"]["MSE"])
plt.show()
a = 1
