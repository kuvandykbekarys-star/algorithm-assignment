dataset = [94, 41, 58, 12, 18, 68, 79, 97, 13, 65]

target = 58

comparisons = 0

for i in range(len(dataset)):
    comparisons += 1

    if dataset[i] == target:
        print("Target Found")
        print("Index:", i)
        print("Comparisons:", comparisons)
        break

print("\nComplexity:")
print("Best Case: O(1)")
print("Average Case: O(n)")
print("Worst Case: O(n)")