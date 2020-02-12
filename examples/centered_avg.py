# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.


# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

# Assume at least 3 items in the array
# If there are repeats of largest/smallest, ignore only one


5, 5, 8, 7
25 // 4 = 6

1, 5, 5, 8, 7
26 // 5 = 5

-4, -2, -4, -2
-12 // 4 = -3


def centered_average(arr):
    arr.sort()
    arr = arr[1:-1]
    return sum(arr) // len(arr)


centered_average([1, 2, 3, 4, 100])
centered_average([1, 1, 5, 5, 10, 8, 7])
centered_average([-10, -4, -2, -4, -2, 0])



def centered_average(arr):
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr) // len(arr)

centered_average([1, 2, 3, 4, 100])
centered_average([1, 1, 5, 5, 10, 8, 7])
centered_average([-10, -4, -2, -4, -2, 0])



def centered_average(arr):
    # Walk through the array and sum each value,
    # keeping track of low and high values
    total = 0
    low = float("inf")
    high = -float("inf")
    for i in arr:
        if i < low:
            low = i
        if i > high:
            high = i
        total += i
    # subtract low and high from sum and divde by length - 2
    return (total - low - high) // (len(arr) - 2)

centered_average([1, 2, 3, 4, 100])
centered_average([1, 1, 5, 5, 10, 8, 7])
centered_average([-10, -4, -2, -4, -2, 0])



