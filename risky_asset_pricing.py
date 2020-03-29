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

S0 = 100  # Initial price
mu = 0.1  # Drift
sigma = 0.23  # Volatility
T = 1.0  # Time to maturity
D = 252  # Trading days in 1 year
dt = T / D  # Annualized Measure of 1 day
N = 10000  # Number of trials

# Create zero array
S = np.zeros((D+1, N))
S[0] = S0  # fill first row into initial value

# simulation
for t in range(1, D+1):
    S[t] = S[t-1] * np.exp((mu - 0.5 * sigma ** 2) *
                           dt + sigma * np.sqrt(dt) * np.random.randn(N))

# plot graph
plt.plot(S[:10000])
plt.xlabel('day')
plt.ylabel('price')
plt.grid(True)


# %%
