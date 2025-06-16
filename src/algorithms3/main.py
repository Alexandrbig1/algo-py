import timeit
import random

def insertion_sort(arr):
    """Sorts an array using the insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Merges two sorted arrays."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort(arr):
    """Sorts an array using Python's built-in Timsort algorithm."""
    return sorted(arr)

def generate_data(size_data):
    """Generates random, sorted, and reverse sorted data."""
    random_data = [random.randint(0, 10000) for _ in range(size_data)]
    sorted_data = sorted(random_data)
    reversed_data = sorted_data[::-1]
    return random_data, sorted_data, reversed_data

def benchmark_sorting(algorithm, data, name):
    """Benchmarks a sorting algorithm."""
    time_taken = timeit.timeit(lambda: algorithm(data.copy()), number=5)
    print(f"{name}: {time_taken:.5f} sec")
    return time_taken

def main():
    sizes = [1000, 2000]
    results = {}

    for size in sizes:
        print(f"\nTest in arr of size {size}:")
        random_data, sorted_data, reversed_data = generate_data(size)

        results[size] = {
            "Insertion Sort": benchmark_sorting(insertion_sort, random_data, "Insertion sort"),
            "Merge Sort": benchmark_sorting(merge_sort, random_data, "Merge sort"),
            "Timsort": benchmark_sorting(timsort, random_data, "Timsort"),
        }

        print("\nSorted data:")
        benchmark_sorting(insertion_sort, sorted_data, "Insertion sort")
        benchmark_sorting(merge_sort, sorted_data, "Merge sort")
        benchmark_sorting(timsort, sorted_data, "Timsort")

        print("\nReverse sorted data:")
        benchmark_sorting(insertion_sort, reversed_data, "Insertion sort")
        benchmark_sorting(merge_sort, reversed_data, "Merge sort")
        benchmark_sorting(timsort, reversed_data, "Timsort")

    readme_content = """
## Testing results (sec)

| Array size | Insertion Sort | Merge Sort | Timsort |
|------------|----------------|------------|---------|
"""

    for size, times in results.items():
        readme_content += f"| {size} | {times['Insertion Sort']:.5f} | {times['Merge Sort']:.5f} | {times['Timsort']:.5f} |\n"

    readme_content += """
## Results: Timsort is faster than Insertion Sort. Merge Sort is a little slower than Timsort but still faster than Insertion Sort because it combines both algorithms.
"""

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

    print("\033[92m---Results are ready!---\033[00m")

if __name__ == "__main__":
    main()