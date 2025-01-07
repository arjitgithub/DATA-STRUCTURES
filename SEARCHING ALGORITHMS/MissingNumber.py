# Python program to find the missing number

def missingNumber(arr):
    n = len(arr) + 1

    # Create hash array of size n+1
    hashArr = [0] * (n + 1)

    # Store frequencies of elements
    for num in arr:
        hashArr[num] += 1

    # Find the missing number
    for i in range(1, n + 1):
        if hashArr[i] == 0:
            return i

    return -1


arr = [1, 2, 3, 5]
result = missingNumber(arr)
print(result)