def find_min(arr):
    min  = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min
test = find_min([18,3,4,-7,5,6])
print(f"Minimum Element {test}")