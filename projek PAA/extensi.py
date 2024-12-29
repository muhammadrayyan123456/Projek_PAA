import random
import time
import matplotlib.pyplot as plt

# Parameters
max_val = 250 - 76

# Function to generate a random array
def generate_array(n, max_val):
    return [random.randint(1, max_val) for _ in range(n)]

# Function to check uniqueness of array elements
def check_uniqueness(array):
    return len(array) == len(set(array))

# Main function to measure execution time
def measure_time(n_values, repeats=5):
    worst_case_times = []
    average_case_times = []

    random.seed(12345)  # Seed for consistency

    for n in n_values:
        # Worst case: Array with duplicates (to ensure there are duplicates)
        array_worst_case = generate_array(n, max_val)
        while check_uniqueness(array_worst_case):
            array_worst_case = generate_array(n, max_val)  # Ensure duplicates

        # Measure time for worst case
        worst_case_duration = 0
        for _ in range(repeats):
            start_time = time.perf_counter()
            check_uniqueness(array_worst_case)
            end_time = time.perf_counter()
            worst_case_duration += (end_time - start_time)
        worst_case_times.append(worst_case_duration / repeats)

        # Average case: Random array
        array_average_case = generate_array(n, max_val)

        # Measure time for average case
        average_case_duration = 0
        for _ in range(repeats):
            start_time = time.perf_counter()
            check_uniqueness(array_average_case)
            end_time = time.perf_counter()
            average_case_duration += (end_time - start_time)
        average_case_times.append(average_case_duration / repeats)

    return worst_case_times, average_case_times

# Array sizes
n_values = [100, 150, 200, 250, 300, 350, 400, 500]

# Measure execution times for worst case and average case
worst_case_times, average_case_times = measure_time(n_values)

# Plotting the graph
plt.plot(n_values, worst_case_times, label='Worst Case', marker='o')
plt.plot(n_values, average_case_times, label='Average Case', marker='x')

plt.xlabel('Size of Array (n)')
plt.ylabel('Time (seconds)')
plt.title('Worst Case vs Average Case Time Complexity')
plt.legend()
plt.grid(True)
plt.show()