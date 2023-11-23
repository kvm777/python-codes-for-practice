import matplotlib.pyplot as plt
import numpy as np

''' 
marker notations...
'o'	    Circle 
'*'	    Star	
'.'	    Point	
','	    Pixel	
'x'	    X	
'X'	    X (filled)	
'+'	    Plus	
'P'	    Plus (filled)	
's'	    Square	
'D'	    Diamond	
'd'	    Diamond (thin)	
'p'	    Pentagon	
'H'	    Hexagon	
'h'	    Hexagon	
'v'	    Triangle Down	
'^'	    Triangle Up	
'<'	    Triangle Left	
'>'	    Triangle Right	
'1'	    Tri Down	
'2'	    Tri Up	
'3'	    Tri Left	
'4'	    Tri Right	
'|'	    Vline	
'_'	    Hline
''' 



ypoints = np.array([3, 5, 6, 1, 8])
plt.plot(ypoints, marker = 'o', ms=10, mec='k', mfc='m')      
#ms = num detoes for markerSize
#mec= 'k' k for black and edge of marker point  color
#mfc = 'm' k for Magenta which is marker face color
#u can use the color codes like #000000

y1points = np.array([1, 4, 2, 7, 2])
plt.plot(y1points, marker = '*' )


'''
marker lines indication..
'-'	    Solid line	
':'	    Dotted line	
'--'    Dashed line	
'-.'	Dashed/dotted line
'''

'''
marker colors as
'r'    	Red	
'g'    	Green	
'b'    	Blue	
'c'    	Cyan	
'm'    	Magenta	
'y'    	Yellow	
'k'    	Black	
'w'    	White
'''
y2points = np.array([8,4,2,6,1])

plt.plot(y2points, '*-.m')   #marker|line|color  as '*:b' it is string format fmt

plt.show()