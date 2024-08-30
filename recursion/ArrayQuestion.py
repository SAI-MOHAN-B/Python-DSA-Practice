def sorted(arr,index):
    if index == len(arr) - 1:
        return True
    return arr[index] < arr[index+1] and sorted(arr,index+1)
    
res = sorted([1,2,32,4,5,6,7],0)
print(res)
