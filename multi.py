from multiprocessing import Pool
import time
import numpy as np

def func(args):
    x, a = args
    sum = 0
    for i in range (a):
        sum += x**i
    
    return sum

start = time.time()
a = 15
A=[]
input_values = [(i,a) for i in range(1000000)]
for args in input_values:
    A.append(func(args))
end = time.time()
print(f"The time taken sequential : {end-start}")


if __name__ == "__main__":
    start = time.time()
    # Create a Pool with 8 processes
    with Pool(processes=8) as pool:
        # Input values
        a=15
        input_values = [(i,a) for i in range(1000000)]

# Apply the function to the input values in parallel as touples only
        results = pool.map(func, input_values)

    end = time.time()
print(f"The time taken multiprocessing :{end-start}")
