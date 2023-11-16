import numpy as np
import matplotlib.pyplot as plt

x_min = float(input("Введите минимальное значение x: "))
x_max = float(input("Введите максимальное значение x: "))
y_min = float(input("Введите минимальное значение y: "))
y_max = float(input("Введите максимальное значение y: "))

x = np.linspace(x_min, x_max, 100)
y = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x, y)

Z1 = (X**0.25) + (Y**0.25)
Z2 = (X**2) - (Y**2)
Z3 = 2*X + 3*Y
Z4 = (X**2) + (Y**2)
Z5 = 2 + 2*X + 2*Y - (X**2) - (Y**2)

plt.figure(figsize=(16, 12))

plt.subplot(231)
plt.contourf(X, Y, Z1, levels=20, cmap='coolwarm')
plt.title('z=(x**0.25) + (y**0.25)')

plt.subplot(232)
plt.contourf(X, Y, Z2, levels=20, cmap='coolwarm')
plt.title('z=(x**2) - (y**2)')

plt.subplot(233)
plt.contourf(X, Y, Z3, levels=20, cmap='coolwarm')
plt.title('z=2x + 3y')

plt.subplot(234)
plt.contourf(X, Y, Z4, levels=20, cmap='coolwarm')
plt.title('z=(x**2) + (y**2)')

plt.subplot(234)
plt.contourf(X, Y, Z5, levels=20, cmap='coolwarm')
plt.title('z=2 + 2x + 2y - (x**2) - (y**2)')

plt.tight_layout()
plt.show()