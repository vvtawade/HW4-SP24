import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Define the functions
def equation1(x):
    return x - 3 * np.cos(x)

def equation2(x):
    return np.cos(2 * x) * x**3

# Find roots
root_eq1 = fsolve(equation1, 0)
root_eq2 = fsolve(equation2, [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])

# Check if functions intersect
intersection_points = fsolve(lambda x: equation1(x) - equation2(x), [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])

# Plot the functions
x_values = np.linspace(-2*np.pi, 2*np.pi, 1000)
plt.plot(x_values, equation1(x_values), label='x - 3cos(x)')
plt.plot(x_values, equation2(x_values), label='cos(2x) * x^3')
plt.scatter(root_eq1, [0] * len(root_eq1), color='red', label='Root of x - 3cos(x)')
plt.scatter(root_eq2, [0] * len(root_eq2), color='blue', label='Roots of cos(2x) * x^3')
plt.scatter(intersection_points, equation1(intersection_points), color='green', label='Intersection points')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersection of Functions')
plt.grid(True)
plt.show()

# Print the results
print("Roots of x - 3cos(x):", root_eq1)
print("Roots of cos(2x) * x^3:", root_eq2)
print("Intersection points:", intersection_points)

