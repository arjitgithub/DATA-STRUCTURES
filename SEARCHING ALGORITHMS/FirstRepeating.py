# Python program to find first repeating element
# using Naive approach in O(n^2) Time and O(1) Space

# Function to find the index of first repeating element in an array
def firstRepeatingElement(arr, n):

    # Nested loop to check for repeating elements
    for i in range(n):
        for j in range(i+1, n):

            # If a repeating element is found, return its index
            if arr[i] == arr[j]:
                return i

    # If no repeating element is found, return -1
    return -1

# Driver code
if __name__ == '__main__':

    # Initializing an array and its size
    arr = [10, 5, 3, 4, 3, 5, 6]
    n = len(arr)

    # Finding the index of first repeating element
    index = firstRepeatingElement(arr, n)

    # Checking if any repeating element is found or not
    if index == -1:
        print("No repeating element found!")
    else:
        print("First repeating element is", arr[index])