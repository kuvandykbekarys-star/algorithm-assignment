dataset = [94, 41, 58, 12, 18, 68, 79, 97, 13, 65]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

result = quick_sort(dataset)

print("Original Dataset:")
print(dataset)

print("\nSorted Dataset:")
print(result)

print("\nComplexity:")
print("Best Case: O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case: O(n^2)")