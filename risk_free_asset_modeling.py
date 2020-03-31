# %%
import numpy as np
import matplotlib.pyplot as plt


def risk_free_value(init_val, r, t):
    result = init_val * np.exp(r*t)
    return result


# Input as Value
init_val = 100  # Initial Investment
r = 0.02  # Risk-free interest
t = 10  # Time to investment (year)

# Output as Value
v = risk_free_value(init_val, r, t)

print(round(v, 2))

# Input array
t = np.array([x for x in np.arange(0, 100, 0.1)])


#  Output array
v = risk_free_value(init_val, r, t)

plt.plot(t, v)
plt.show()

# %%


