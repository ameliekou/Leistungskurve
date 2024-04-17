from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt
import numpy as np

data = load_data("activity.csv")
power_W = data['PowerOriginal']
#Sort
sorted_power_W = bubble_sort(power_W)


print(data)
print(sorted_power_W)
