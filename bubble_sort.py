dataset = [94, 41, 58, 12, 18, 68, 79, 97, 13, 65]

arr = dataset.copy()

n = len(arr)

for i in range(n):
    swapped = False

    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    print(f"Pass {i + 1}: {arr}")

    if not swapped:
        break

print("\nFinal Sorted Array:")
print(arr)

print("\nComplexity:")
print("Best Case: O(n)")
print("Average Case: O(n^2)")
print("Worst Case: O(n^2)")
