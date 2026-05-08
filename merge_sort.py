dataset = [94, 41, 58, 12, 18, 68, 79, 97, 13, 65]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = 0
    j = 0

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

sorted_array = merge_sort(dataset)

print("Original Dataset:")
print(dataset)

print("\nSorted Dataset:")
print(sorted_array)

print("\nComplexity:")
print("Best Case: O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case: O(n log n)")
