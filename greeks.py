# %%
# import module
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import numpy as np
import scipy.stats as stat
init_notebook_mode(connected=True)

# %%
# calculate delta


def delta(option_type, S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option_type == 1:
        return stat.norm.cdf(d1)
    else:
        return stat.norm.cdf(d1) - 1


call = 1
put = -1

K = 100
r = 0.01
sigma = 0.25

n1 = 100  # number of steps for x-axis
n2 = 50  # number of contour line
start_t = 0.00001  # start value of maturity
end_t = 1  # end value of maturity
start_s = 0.00001  # start value of underlying asset price
end_s = 200  # end value of underlying asset price

T = np.linspace(start_t, end_t, n1)
S = np.linspace(start_s, end_s, n2)
T, S = np.meshgrid(T, S)

call_delta = delta(call, S, K, T, r, sigma)
put_delta = delta(put, S, K, T, r, sigma)


# %%

trace = go.Surface(x=T, y=S, z=call_delta, colorscale='Jet', opacity=0.8,
                   contours_x=dict(show=True, color='black', start=start_t, end=end_t,
                                   size=(end_t - start_t) / n1, project_x=True),
                   contours_y=dict(show=True, color='black', start=start_s, end=end_s, size=(end_s - start_s) / n2, project_y=True))


data = [trace]
layout = go.Layout(title='Delta Surface',
                   scene={'xaxis': {'title': 'maturity'}, 'yaxis': {
                       'title': 'Spot price'}, 'zaxis': {'title': 'Delta'}},
                   width=400, height=400, autosize=True)

fig = go.Figure(data=data, layout=layout)
iplot(fig)

# %%
