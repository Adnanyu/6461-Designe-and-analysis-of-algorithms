import numpy as np
import time
import matplotlib.pyplot as plt

# Sample arrays 'a' and 'b'
def generate_arrays(n):
    a = np.random.randint(1, 10, size=n)
    b = np.random.randint(1, 10, size=n)
    return a, b

def algorithm(n, a, b):
    Sum = 0
    j = 2
    while j < n:
        k = j
        while k < n:
            Sum += a[k] * b[k]
            k += int(n**(1/3) * np.log(n))
        j = 2 * j
    return Sum

# This function is calculating the time taken to run every value of n
def measure_time(n):
    a, b = generate_arrays(n)
    start_time = time.time()
    algorithm(n, a, b)
    end_time = time.time()
    print(f'Time Takes for {n} is {end_time - start_time}')
    return end_time - start_time

n_values = [1, 10, 100, 10000, 100000, 1000000, 100000000]

#am storing the time taken for n in this array
times = [measure_time(n) for n in n_values]

plt.plot(n_values, times, label="Experimental Time", marker='o')

# Here am calculating the value of the constanstant C and getting the time taken for 10^6 from the times array
C = times[-2] / (1000000 ** (2/3))

n_values_fine = np.linspace(min(n_values), max(n_values), 100)
# time_theoretical = [C * (n ** (2/3)) for n in n_values]
theoretical_times =  [C * (n ** (2/3)) for n in n_values]

print('theory table')
for i in range(len(theoretical_times)):
    print(f'time for {n_values[i]} is {theoretical_times[i]} ')
    
    
plt.plot(n_values, theoretical_times, label=r"$n^{2/3}$", linestyle="--")

plt.xscale('log')
plt.yscale('log')
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()



