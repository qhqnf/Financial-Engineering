# %%
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import numpy as np
import scipy.stats as stat

# black scholes option formula


def europian_options(S, K, T, r, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        V = S * stat.norm.cdf(d1) - K * np.exp(-r * T) * stat.norm.cdf(d2)
    else:
        V = K * np.exp(-r * T) * stat.norm.cdf(-d2) - S * stat.norm.cdf(-d1)

    return V


print(europian_options(100, 100, 1, 0.02, 0.2, 'call'))

print(europian_options(100, 100, 1, 0.02, 0.2, 'put'))

# %%

# import library
init_notebook_mode(connected=True)

# parameter
K = 100
r = 0.01
sigma = 0.25

# variables
T = np.linspace(0, 1, 100)
S = np.linspace(0, 200, 100)
T, S = np.meshgrid(T, S)

# output
call_value = europian_options(S, K, T, r, sigma, 'call')
put_value = europian_options(S, K, T, r, sigma, 'put')

# call option price to 3D
trace = go.Surface(x=T, y=S, z=call_value)
data = [trace]
layout = go.Layout(title='Option Price',
                   scene={'xaxis': {'title': 'Maturity'}, 'yaxis': {'title': 'Spot Price'}, 'zaxis': {'title': 'Option Price'}})


fig = go.Figure(data=data, layout=layout)
iplot(fig)
# %%

# put option price to 3D
trace = go.Surface(x=T, y=S, z=put_value)
data = [trace]
layout = go.Layout(title='Option Price',
                   scene={'xaxis': {'title': 'Maturity'}, 'yaxis': {'title': 'Spot Price'}, 'zaxis': {'title': 'Option Price'}})


fig = go.Figure(data=data, layout=layout)
iplot(fig)


# %%
