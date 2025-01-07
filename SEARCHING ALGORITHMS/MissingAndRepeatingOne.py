def print_two_elements(arr):
    n = len(arr)
    missing = (n * (n + 1)) // 2
    print("Repeating", end=" ")

    for i in range(n):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
            missing -= abs(arr[i])  # subtract unique elements
        else:
            print(abs(arr[i]))

    print("Missing", missing)

# Driver code
arr = [7, 3, 4, 5, 5, 6, 2]
print_two_elements(arr)