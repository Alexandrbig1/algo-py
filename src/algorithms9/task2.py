import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Define the function to integrate
def f(x):
    return x**2

# Integration limits
a, b = 0, 2

# Number of random points for Monte Carlo integration
# N = 10000
# N = 1000000
N = 5000000

# Generate random points
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

# Check if points are under the curve
under_curve = y_rand < f(x_rand)

# Calculate the area using Monte Carlo method
area_mc = (b - a) * f(b) * np.sum(under_curve) / N

# Calculate the area using scipy's quad method
result_quad, error_quad = spi.quad(f, a, b)

# Print the results
print(f"Monte Carlo method: {area_mc}")
print(f"Quad method: {result_quad} (error {error_quad})")

# Plot the function and the random points
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(x, y, alpha=0.3, color='gray')
ax.scatter(x_rand, y_rand, c=under_curve, cmap='coolwarm', alpha=0.3, s=1)
ax.axvline(a, color='gray', linestyle='--')
ax.axvline(b, color='gray', linestyle='--')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Monte Carlo method for integral of f(x) = x^2 from {a} to {b}')
plt.grid()
plt.show()