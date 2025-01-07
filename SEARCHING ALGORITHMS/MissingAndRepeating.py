def print_two_elements(arr):
    n = len(arr)

    # Creating visited vector of size n+1 with
    # initial values as false. Note that array
    # values will go upto n, that is why we
    # have taken the size as n+1
    visited = [False] * (n + 1)
    repeating = -1
    missing = -1

    for i in range(n):
        if visited[arr[i]]:
            repeating = arr[i]
        else:
            visited[arr[i]] = True

    for i in range(1, n + 1):
        if not visited[i]:
            missing = i
            break

    print(f"Repeating : {repeating}")
    print(f"Missing : {missing}")

arr = [7, 3, 4, 5, 5, 6, 2]
print_two_elements(arr)