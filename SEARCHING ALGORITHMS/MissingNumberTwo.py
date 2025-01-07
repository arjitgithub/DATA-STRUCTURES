# Python program to find the missing number

def missingNumber(arr):
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0

    # XOR all array elements
    for num in arr:
        xor2 ^= num

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor1 ^= i

    # Missing number is the XOR of xor1 and xor2
    return xor1 ^ xor2


arr = [1, 2, 3, 5]
res = missingNumber(arr)
print(res)