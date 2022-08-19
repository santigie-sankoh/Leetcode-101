from line_profiler import LineProfiler
import random
import matplotlib.pyplot as plt
import numpy as np

#Implement a basic measure of tracking the time taken to run an algorithm.


def time_algo(items):
    for item in range(100):
        return item


items = [random.randint(1, 100)]
lp = LineProfiler()
lp_wrapper = lp(time_algo)
lp_wrapper(items)
lp.print_stats()

#Question 4 (a)

#ploting some len of int(x) over string(y)
x = [1, 2, 3, 4]
y = ["Boy", "story", "fax", "trying"]
arr1 = []
arr2 = []

for i in range(len(x)):
    arr1.append(i)
for j in range(len(y)):
    arr2.append(j)

plt.plot(arr1, arr2, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Time Complexity')
plt.show()

#Question 5 (time taken when the sixe is 1000,000)


def algo_two(inputs):
    for input in inputs:
        print(input)


inputs = [random.randint(1, 1000000)]
lp = LineProfiler()
lp_wrapper = lp(algo_two)
lp_wrapper(inputs)
lp.print_stats()
