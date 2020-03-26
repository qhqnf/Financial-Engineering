# %%
import numpy as np
import matplotlib.pyplot as plt

S0 = 100  # initial value
mu = 0.1  # drift(mean)
sigma = 0.23  # volatility(standard deviation)
T = 1  # time to maturity
N = 1  # number of trial

St = S0 * np.exp((mu - 1/2 * sigma ** 2) * T + sigma *
                 np.sqrt(T) * np.random.randn(N))
print(St)

N = 10000  # number of trial
St = S0 * np.exp((mu - 1/2 * sigma ** 2) * T + sigma *
                 np.sqrt(T) * np.random.randn(N))
# np.random.randn(N) give us array automatically

print(len(St))
plt.hist(St, bins=50)
plt.xlabel('price at maturity')
plt.ylabel('frequency')

plt.show()


# %%
