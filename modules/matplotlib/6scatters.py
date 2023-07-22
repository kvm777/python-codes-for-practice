import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,6,2,4,8,1,9,7,3])
y = np.array([50,40,88,35,22,95,10,35,70])

#colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige"])
colors = np.array([10,20,30,40,50,60,70,80,90])
plt.scatter(x,y,c=colors, cmap='viridis')
plt.colorbar()
#plt.plot(x,y)
plt.show()

plt.scatter(x,y, s=colors, alpha=0.7) #here we use colors as sizes 
    #aplha= gives the transparency..
plt.show()
