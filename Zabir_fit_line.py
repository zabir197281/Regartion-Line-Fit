import matplotlib.pyplot as plt
import numpy as np

def list_sum(x, y):
    return np.dot(x, y)

def square_sum(x):
    return np.dot(x, x)

def my_linfit(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = square_sum(x)
    sum_xy = list_sum(x, y)

    b = (sum_y / n - (sum_x * sum_xy) / (n * sum_x_squared)) / (1 - (sum_x ** 2 / (n * sum_x_squared)))
    a = (sum_x * -b + sum_xy) / sum_x_squared

    return a, b

x_coords = []
y_coords = []

def on_click(event):
    if event.button == 1:
        x_coords.append(event.xdata)
        y_coords.append(event.ydata)
        ax1.clear()
        ax1.scatter(x_coords, y_coords, c='b', marker='o', label='Points')
        ax1.set_xticks([-2, -1, 0, 1, 2, 3, 4, 5])
        ax1.set_yticks([-2, -1, 0, 1, 2, 3, 4, 5])
        ax1.set_xlabel('X-axis')
        ax1.set_ylabel('Y-axis')
        ax1.legend()
        plt.draw()
    elif event.button == 3:
        plt.close()

fig, ax1 = plt.subplots()
ax1.set_xticks([-2, -1, 0, 1, 2, 3, 4, 5])
ax1.set_yticks([-2, -1, 0, 1, 2, 3, 4, 5])
ax1.scatter(x_coords, y_coords, c='b', marker='o', label='Points')
fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()

fig, ax2 = plt.subplots()
a, b = my_linfit(x_coords, y_coords)
xp = np.arange(-2, 5, 0.1)
ax2.plot(xp, a * xp + b, '-r')
ax2.scatter(x_coords, y_coords, c='b', marker='o', label='Points')

print ( f"My fit : a={b} and b={b}" )

plt.show()
