from multiprocessing import Pool     

# importing Pool
# Pool divides the whole input dataset into provided procesess and runs them paralelly in your CPU cores.
# Say if the size of your input is 40.
# when procesess = 10 provided
# The dataset of size 40 will be divided into 10 chunks, with each chunk having 4 units of data. Each process will be assigned one of these chunks.
# Each process will work on its independently assigned chunk
# I have cores as 4. So I can work on 4 tasks simultaneously
# Each process will assign 4 units of data to 4 Cores and runs them


def multi(args):
    lattice, T_start, T_end, steps, N, J = args 
    if __name__ == "__main__" :  
        start = time.time()
        T = np.linspace(T_start, T_end, steps) 
        with Pool(processes=10) as pool:   
            input_values = [(lattice, N, T[i], J) for i in range (len(T))]  # Creating input as args
            results = pool.map(data, input_values) #pool.map requires func and input values as args. It maps the results as array.
        end = time.time()
        print(f"Time taken to multi is {end-start}\n")
    return results
