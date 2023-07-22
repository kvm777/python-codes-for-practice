import numpy as np
import matplotlib.pyplot as plt
 
# create data
x=np.array([1, 2, 3, 4, 5])
 
# making subplots
fig, ax = plt.subplots(2, 2)

'''
# set data with subplots and plot
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x*2)
ax[1, 0].plot(x, x*x)
ax[1, 1].plot(x, x*x*x)
 
# set the title to subplots
ax[0, 0].set_title("Linear")
ax[0, 1].set_title("Double")
ax[1, 0].set_title("Square")
ax[1, 1].set_title("Cube")
 '''

title = ["linear","double","square","cube"]
y = [x, x*2, x*x, x*x*x]

for i in range(4):

    plt.subplot(2, 2, i+1)
     
    # plotting (x,y)
    plt.plot(x, y[i])
     
    # set the title to subplot
    #plt.gca().title.set_text(title[i])
    plt.gca().set_title(title[i])
 




#this is for main title..
fig.suptitle("function graphs",size=20,color='green')

#tight_layout must use before showng...
fig.tight_layout(pad=2)     #pad= for spacing around the graphs..
#fig.subplots_adjust()      this is used for individual adugestments..
plt.show()