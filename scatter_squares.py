import matplotlib.pyplot as plt
# x_values = list(range(1, 101))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, s=50, edgecolor='none', c=y_values, cmap=plt.cm.Blues)
# # Цвет можно задавать и в виде строки: 'red' ...
# #Градиент цвета пример :cmap=plt.cm.Blues
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.axis([0, 110, 0, 11000])
# # plt.savefig() - автоматически сохраняет диаграмы.

x2_values = list(range(1, 101))
y2_values = [x**3 for x in x2_values]
plt.scatter(x2_values, y2_values, s=50, edgecolor='none', c=x2_values, cmap=plt.cm.Reds)
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 110, 0, 1100000])
plt.show()
