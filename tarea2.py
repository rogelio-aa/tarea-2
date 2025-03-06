
  



#      ejercicio 1


palabra = input("Ingresa una palabra: ").lower()
print(f"La letra 'h' se encuentra en la posición: {palabra.find('h')}" if 'h' in palabra else "La letra 'h' no se encuentra en la palabra.")



#     ejercicio 2
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
plt.plot(x, np.sin(x), color='yellow', label='Seno')
plt.plot(x, np.cos(x), color='blue', linewidth=2, label='Coseno')
plt.legend()
plt.show()
