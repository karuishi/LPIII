import numpy as np
import matplotlib.pyplot as plt

mes = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
mes_sin = np.sin((mes-1)*(2.*np.pi/12))
mes_cos = np.cos((mes-1)*(2.*np.pi/12))

x = np.linspace(0, 16) 
plt.plot(x, np.sin(x))
plt.show()