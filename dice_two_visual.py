from dice import Dice
import pygal
dice_1 = Dice(6)
dice_2 = Dice(10)
results = []
step = 0
amount = 1000000
for rol_num in range(amount):
    step += 1
    result = dice_1.roll() + dice_2.roll()
    results.append(result)
    print(round((step/amount) * 100, 2), '%')

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
hist = pygal.Bar()
hist.title = f"Results of rolling two D6 dice {amount} times."
# hist.x_labels = [str(x) for x in range(2, 17)]
x_labels = []
for x in range(2, 17):
    x_labels.append(str(x))

hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual_2.svg')
