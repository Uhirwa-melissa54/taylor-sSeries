import numpy as np
import matplotlib.pyplot as plt
import math

# Define x range
x = np.linspace(-2*np.pi, 2*np.pi, 400)

# Original function
y_sin = np.sin(x)

# Taylor polynomial of sin(x) around 0 up to degree 9
# sin(x) ≈ x - x^3/3! + x^5/5! - x^7/7! + x^9/9!
y_taylor = (
    x
    - x**3 / math.factorial(3)
    + x**5 / math.factorial(5)
    - x**7 / math.factorial(7)
    + x**9 / math.factorial(9)
)

# Plot both functions on the same graph
plt.figure(figsize=(10,6))
plt.plot(x, y_sin, label="sin(x)", color="blue")
plt.plot(x, y_taylor, label="Taylor Polynomial (degree 9)", color="red", linestyle="--")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin(x) and its Taylor Polynomial Approximation around 0")
plt.grid(True)
plt.show()
