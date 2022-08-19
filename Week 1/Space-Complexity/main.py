import random
import memory_profiler
from memory_profiler import profile
import time
import matplotlib.pyplot as plt


#Implement a basic measure of tracking the space  taken to run an algorithm.

#def sorted_lst1():
  #lst = []
  #for i in range(2, 102):
    #  lst.append(i)
    #  lst.sort()
    
   
def sorted_list2(n):
    x = []
    for i in range(100):
        x.append(random.randrange(2, 100, 2))

    x.sort()

    #print("list", x, "&", "List Sorted: " +str(x))


my_lst = []
test_lst = [i for i in range(100)]


for i in range(2, 102):
    start = time.perf_counter()
    sorted_list2(test_lst[0:i])
    end = time.perf_counter()
    final = end - start
    x = memory_profiler.memory_usage()

    my_lst.append(x[0])
    print(my_lst)


plt.plot(test_lst, my_lst)
plt.xlabel('List Length')
plt.ylabel('Space')
plt.title("Space Complexity Graph")
plt.show()
