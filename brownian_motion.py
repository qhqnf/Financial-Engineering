import math
import numpy as np
import matplotlib.pyplot as plt

# Define dt and sqrt_dt
T = 1
N = 10000
dt = T / N
sqrt_dt = math.sqrt(dt)

# Generate Series of 1) Time, 2) White Noise 3) Brownian Motion
t = np.array([i for i in np.arange(0, T, T/N)])
dX = np.random.randn(N) * sqrt_dt
X = np.cumsum(dX)

# Print Graph
plt.subplot(2, 1, 1)
plt.plot(X, dX)
plt.subplot(2, 1, 2)
plt.plot(t, X)

plt.show()
