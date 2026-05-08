dataset = [94, 41, 58, 12, 18, 68, 79, 97, 13, 65]

hash_table = [None] * 7

for value in dataset:
    index = value % 7

    original_index = index

    while hash_table[index] is not None:
        index = (index + 1) % 7

        if index == original_index:
            break

    hash_table[index] = value

print("Hash Table:")

for i in range(len(hash_table)):
    print(i, ":", hash_table[i])

print("\nComplexity:")
print("Best Case: O(1)")
print("Average Case: O(1)")
print("Worst Case: O(n)")
