from dice import Dice
import pygal
dice = Dice()
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)
print(results)

frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 items."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')

