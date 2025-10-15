import math
import timeit

def find_max(nums):
    max_val = nums[0]
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2 
        max_val = max(max_val, nums[m])
        print('max value here is: ', max_val)
        if nums[m] >= nums[l]:
            max_val = max(max_val, nums[l])
            l = m + 1
        else:
            r = m - 1
    return max_val

# print(findMax([15, 27, 29, 35, 42, 5, 15]))


def create_rotated_array(size, rotation_point=None):
    #Creates a rotated sorted array of the given size.
    arr = list(range(size))
    if rotation_point is None:
        rotation_point = size // 2  # Default: rotate in the middle
    return arr[rotation_point:] + arr[:rotation_point]


import time
import matplotlib.pyplot as plt

def measure_accurate_binary_search_time():
    input_sizes = [10**i for i in range(1, 8)]  # 10 to 10 million
    times = []

    for size in input_sizes:
        arr = create_rotated_array(size)

        # Use a lambda to bind the current arr to the timed function
        elapsed_time = timeit.timeit(lambda: find_max(arr), number=10) / 10
        times.append(elapsed_time)

        print(f"Input size: {size}, Avg time: {elapsed_time:.10f} seconds")


    log_times = [math.log2(n) for n in input_sizes]
    
    # normalizing the data for the graph using average of experimental/average of theoritical
    average_of_theory = sum(log_times) / len(log_times)
    average_of_experimental = sum(times) / len(times)
    normalization_scale =  average_of_experimental / average_of_theory
    normalized_log_times = [t * normalization_scale for t in log_times]
    
    print('normalized log time:', normalized_log_times)

    
    print("times are: ", times)
    print(" normalized log times are: ", normalized_log_times)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, marker='o', label='find_Max Time')
    plt.plot(input_sizes, normalized_log_times, linestyle='--', label='O(log n) Theoretical')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input Size (log scale)')
    plt.ylabel('Avg Time (seconds, log scale)')
    plt.title('Accurate Timing: findMax in Rotated Sorted Array')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

measure_accurate_binary_search_time()
