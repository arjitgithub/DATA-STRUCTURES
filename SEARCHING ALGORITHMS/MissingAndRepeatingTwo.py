def print_two_elements(arr):
    n = len(arr)
    s = (n * (n + 1)) // 2
    ssq = (n * (n + 1) * (2 * n + 1)) // 6

    missing = 0
    repeating = 0

    for i in range(n):
        s -= arr[i]
        ssq -= arr[i] * arr[i]

    missing = (s + ssq // s) // 2
    repeating = missing - s

    print("Repeating:", repeating)
    print("Missing:", missing)

arr = [4, 3, 6, 2, 1, 6, 7]
print_two_elements(arr)