import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi,15)
sine_plot = np.sin(x)   #list of sine values..
cos_plot = np.cos(x)    #list of cosine values..

# 'bs:' mentions blue color, square 
# marker with dotted line
plt.plot(x,sine_plot, 'bs:' ,label='sine_plot')

#'ro-' mentions red color, circle 
# marker with solid line.
plt.plot(x,cos_plot, 'r-.o' ,label='cos_plot')

plt.title("Trigonometric Functions", size=20,color='green')

#plt.legend(labels = ('Cosine Function', 'Sine Function'), loc = 'upper left')
plt.legend(loc='best')
plt.show()