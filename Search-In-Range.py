def search_range(arr,target,start,end):
    if len(arr) == 0:
        return -1
    for index in range(start,end):
        element = arr[index]
        if target == element:
            return index
    return -1
test = search_range([12,13,14,15],19,1,3)
if test > 0:
    print(f"element found at {test}")
else:
    print(f"element doesn't found")
