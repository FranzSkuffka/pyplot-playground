import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.stats

YLABEL = 'μV/m²'
XLABEL = 'Time (ms)'

# In milliseconds
START = -200
END = 1200
# hzRESOLUTION = 256
hzRESOLUTION = 500

MSPERSECOND = 1000
# how many milliseconds per x-step
RESOLUTION = round(MSPERSECOND / 256)
STEPS = round(
    (END - START)
    / RESOLUTION
  )

# Data for plotting
x = np.arange(START, END, RESOLUTION)
# fake curves
y1 = 0.00025 + 0.001 * np.exp(-x/130.) + scipy.stats.gamma(15).rvs(len(x))*(1-np.exp(-x/100))*2e-5 * 1000 * 3 + 6
y2 = 0.00025 + 0.001 * np.exp(-x/150.) + scipy.stats.gamma(30).rvs(len(x))*(1-np.exp(-x/100))*2e-5 * 1000 * 3 + 6
y3 = 0.00025 + 0.001 * np.exp(-x/130.) + scipy.stats.gamma(15).rvs(len(x))*(1-np.exp(-x/100))*2e-5 * 1000 * 3 + 5
y4 = 0.00025 + 0.001 * np.exp(-x/150.) + scipy.stats.gamma(30).rvs(len(x))*(1-np.exp(-x/100))*2e-5 * 1000 * 3.5 + 4


fig, ax = plt.subplots()

# Axis configuration
# Draw one plot

ax.plot(x, y1, label='NOGO cathodal')
ax.plot(x, y2, label='NOGO sham')
ax.plot(x, y3, label='GO cathodal')
ax.plot(x, y4, label='GO sham')
ax.set(
    xlabel=XLABEL
  , ylabel=YLABEL)
  # , title=TITLE)



# set axis positions to zero
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Hide frame
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# set specific range axes
plt.ylim(top=10, bottom=-8)
plt.xlim(left=START, right=END)

plt.legend(loc='best')

# make spines thicker
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)



# set labels
xlabel = ax.set_xlabel(XLABEL, fontWeight = "bold")
ax.xaxis.set_label_coords(1, 0.5)

# adjust label positions
ylabel = ax.set_ylabel(YLABEL, fontWeight = "bold", rotation = 0)
ax.yaxis.set_label_coords(0.2, 0.98)

# for readability - hide zero on X
yticks = ax.yaxis.get_major_ticks()
yticks[4].label1.set_visible(False)

# move zero on y
xticks = ax.xaxis.get_major_ticks()
# TODO - MOVE ZERO ON Y
xticks[1].label1.set_visible(False)



fig.savefig("test.png")
