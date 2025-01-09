import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,7,100)
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,label='sin(x)')
plt.plot(x,z,label='cos(x)')
plt.xlabel('X------>')
plt.ylabel('Y------>')
plt.grid()
plt.legend()
plt.title('first plot')
plt.show()
