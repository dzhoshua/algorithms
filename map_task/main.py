from sys import getsizeof
import time

file = open('out-py.txt', 'w', encoding='UTF-8')
for i in range(8):
    t1 = time.perf_counter_ns()
    dict = {}
    n = 10**i
    for j in range(1, n+1):
        dict[j] = j
    t2 = time.perf_counter_ns()
    ns = t2 - t1

    print(n, int(ns), getsizeof(dict))
    file.write(str(n) + ' ' + str(int(ns)) + ' '+str(getsizeof(dict))+'\n')
file.close()