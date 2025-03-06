

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi , 2 * np.pi, 1000 )
plt.plot(x, np.sin(x), label='seno')
plt.plot(x, np.cos(x), label='coseno')
plt.legend()
plt.show()