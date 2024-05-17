import numpy as np
import matplotlib.pyplot

# Load data
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
# Make Figure
fig = matplotlib.pyplot.figure(figsize=(5.0, 7.0))

# Create subplots in 3 rows and 1 column
axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

# Plot and label the average, max, and min of the data
axes1.set_ylabel('average')
axes1.plot(data.mean(axis=0))

axes2.set_ylabel('max')
axes2.plot(data.max(axis=0))

axes3.set_ylabel('min')
axes3.plot(data.min(axis=0))

fig.tight_layout()

matplotlib.pyplot.savefig("plot.png")

# Code adapted from Software Carpentry. Check out the full lesson here:
# http://swcarpentry.github.io/python-novice-inflammation/01-numpy.html