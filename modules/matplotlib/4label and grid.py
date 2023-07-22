import matplotlib.pyplot as plt
import numpy as np

rollnums = np.array([101,102,103,104,105,106,107,108])
marks = np.array([40,56,88,55,33,67,23,95])

plt.plot(rollnums,marks)

'''
loc='' for the position of the title 
fontdict= for the labelling style
'''
font1 = {'family':'serif','color':'blue','size':18}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("MARKER PLOT", loc="left",fontdict=font1)
plt.xlabel("Roll Nums",fontdict=font2)
plt.ylabel("Marks",fontdict=font2)

#grid denotion in graphs...
plt.grid(linestyle='-.', color='hotpink', linewidth='1')
#plt.grid(axis='x')
#plt.grid(axis='y')
plt.show()