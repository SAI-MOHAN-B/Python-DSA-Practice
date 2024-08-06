def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        # here we are checking whether correct index = arr[i] - 1 
        # here arr[i] represents the current element
        # index = value - 1 
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            swap(arr,i,correct)
        else:
            i+=1
    return arr    
res = cyclic_sort([5,4,3,2,1])
print(res)
