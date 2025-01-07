def largest(arr, n):
    mx = arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] > mx:
            mx = arr[i]

    return mx

if __name__ == '__main__':
    arr = [10, 324, 45, 90, 9808]
    n = len(arr)

    ans = largest(arr, n)

    print(ans)