import matplotlib.pyplot as plt
from Random_walk import RandomWalk


# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()
colors = ['red', 'blue', 'green', 'black', 'yellow']
while True:
    rw = RandomWalk(50000)
    plt.figure(dpi=128, figsize=(10, 6))
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor=None, s=1)
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input('Make another walk? y/n: ')
    if keep_running == 'n':
        break


