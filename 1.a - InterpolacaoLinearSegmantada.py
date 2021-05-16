import numpy as np
import matplotlib.pyplot as plt

x = [1.03, 1.43, 1.76, 2.20, 2.78, 3.15, 3.55, 4.12]
y = [2.37, 1.53, 1.02, 0.60, 0.26, 0.17, 0.13, 0.08]

plt.scatter(x, y); plt.plot(x, y); plt.xlabel('X'); plt.ylabel('Y'); plt.title('Y(X)'); plt.tight_layout()
plt.show()

y_interpolado = np.interp(2.0, x, y)
novoY = round(y_interpolado, 2)
print(novoY)