def get_two_elements(arr):
    n = len(arr)

    # Will hold xor of all elements
    # and numbers from 1 to n
    xor1 = 0

    x = 0
    y = 0

    # Get the xor of all array elements
    # and numbers from 1 to n
    for i in range(n):
        xor1 ^= arr[i]
        xor1 ^= (i + 1)  # 1 to n numbers

    # Get the rightmost set bit in xor1
    set_bit_no = xor1 & ~(xor1 - 1)

    # Now divide elements into two sets by
    # comparing rightmost set bit
    for i in range(n):

        # Decide whether arr[i] is in
        # first set or second
        if arr[i] & set_bit_no:
            x ^= arr[i]
        else:
            y ^= arr[i]

        # Decide whether (i+1) is
        # in first set or second
        if (i + 1) & set_bit_no:
            x ^= (i + 1)
        else:
            y ^= (i + 1)

    # Print the results
    print(f"Missing and Repeating (In any order): {x} {y}