import matplotlib.pyplot as plt
squares = []
values = []
for value in range(0, 101):
    values.append(value)
    squares.append(value ** 2)
plt.plot(values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
