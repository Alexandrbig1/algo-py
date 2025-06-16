def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound_index = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound_index = mid
            right = mid - 1

    return iterations, upper_bound_index

sorted_arr = [0.2, 1.1, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.5]

iterations, result = binary_search(sorted_arr, 6.5)
if result is not None:
    print(f"Target not found. Upper bound is at index {result}, value: {sorted_arr[result]}")
else:
    print("Target not found and no upper bound exists.")
print(f"Iterations: {iterations}")