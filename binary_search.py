dataset = [94, 41, 58, 12, 18, 68, 79, 97, 13, 65]

sorted_dataset = sorted(dataset)

target = 68

low = 0
high = len(sorted_dataset) - 1

while low <= high:
    mid = (low + high) // 2

    print(f"Low={low}, High={high}, Mid={mid}")

    if sorted_dataset[mid] == target:
        print("\nTarget Found")
        print("Index:", mid)
        break

    elif sorted_dataset[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

print("\nSorted Dataset:")
print(sorted_dataset)

print("\nComplexity:")
print("Best Case: O(1)")
print("Average Case: O(log n)")
print("Worst Case: O(log n)")