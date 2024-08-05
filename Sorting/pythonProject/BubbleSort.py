def bubble_sort(arr):
    # run the steps n times
    for i in range(len(arr)):
        swapped = False
        # for each step,max element comes at the last index of the array
        for j in range(1, len(arr) - i):
            # swap if it is smaller than the previous elements
            if arr[j] < arr[j - 1]:
                # temp
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                swapped = True
        # if you did not swapped for a particular value of i
        # it means that the array is sorted
        # hence stop the program
        if not swapped:
            break
    return arr


res = bubble_sort([1,2,3,4,5])
print(res)
