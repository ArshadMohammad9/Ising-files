import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

from functions import lattice
from functions import view
from functions import m
from functions import MCC
from functions import equi
from functions import E

'''start = time.time()
A = lattice((16,16))
T = np.linspace(1, 4, 40)
Equi = equi((A, 2, 1, 10000 ))
end = time.time()
print(f"The time for 1 T to equil{end-start}= 1167.196")'''


from multiprocessing import Pool

if __name__ == "__main__" :
    start = time.time()
    A = lattice((16,16))
    T = np.linspace(1,4,8)
    J = 1
    with Pool(processes=8) as pool:
        input_values = [(A,T[i], J, 10000) for i in range (len(T))]
        results = pool.map(equi, input_values)

    end = time.time()

print(f"Time taken:{end-start}")
print(results)
np.savetxt('data.csv', results, delimiter=',')

#7:08
print(results)