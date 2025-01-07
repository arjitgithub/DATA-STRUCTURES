# Python program to find first repeating element
# using Hash Set in O(n) Time and O(n) Space
import sys

def firstRepeatingElement(arr):
    s = set()

    # If an element is already present, return it
    # else insert it
    minEle = sys.maxsize
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in s:
            minEle = min(minEle, i)
        s.add(arr[i])

    # If no element repeats
    return -1 if minEle == sys.maxsize else minEle

arr = [10, 5, 3, 4, 3, 5, 6]
index = firstRepeatingElement(arr)
if index == -1:
    print("No repeating found!")
else:
    print("First repeating is", arr[index])