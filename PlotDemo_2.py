import numpy as np
#import matplotlib
from matplotlib import pyplot as plt
fig = plt.figure('Ishan')
plt.title("Ishan's Graph 2")
x = np.arange(0, 10, 0.5)
y1 = ((x**3)-1)
y2 = ((-x**3)-1)
plt.plot(x, y1,  'b', label='line one', linewidth=5)
plt.plot(x, y2,  'r', label='line two', linewidth=5)  
plt.ylabel('Y axis')  
plt.xlabel('X axis')  
plt.legend()  
plt.grid(True, color='k')  
plt.show()  

