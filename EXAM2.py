def Calc(arr, n):
    # Initialize maximum element
    max = arr[0]
    min = arr[0]
    # buy day
    bd = 0
    # sell day
    sd = 0

    # Traverse array elements from second
    # and compare every element with
    # current max and min
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
            sd = i
        if arr[i] < min:
            min = arr[i]
            bd = i
    print("Buy on - Day ", bd + 1, " - sell on - Day ", sd + 1, " - profit = ", max - min)


# Driver Code
arr = [100, 180, 260, 310, 40, 535, 695]
n = len(arr)
Calc(arr, n)