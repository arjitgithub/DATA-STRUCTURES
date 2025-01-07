# Python program to find the missing number

def missingNumber(arr):
    n = len(arr) + 1

    # Calculate the sum of array elements
    totalSum = sum(arr)

    # Calculate the expected sum
    expectedSum = (n * (n + 1)) // 2

    # Return the missing number
    return expectedSum - totalSum


arr = [1, 2, 3, 5]
print(missingNumber(arr))