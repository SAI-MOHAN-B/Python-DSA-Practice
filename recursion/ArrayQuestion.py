def sorted(arr,index):
    if index == len(arr) - 1:
        return True
    return arr[index] < arr[index+1] and sorted(arr,index+1)
    
res = sorted([1,2,32,4,5,6,7],0)
print(res)

# reverse Linear Search
def searching(arr,target,index):
    if index == len(arr)-1 and arr[index] == target:
        return index
    return searching(arr,target,index+1)

test_data = searching([1,2,32,4,5,6,7],32,0)
print(test_data)

# reversing the index
def findIndex(arr,target,index):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    else:
        return findIndex(arr,target,index+1)
# finding the index which is repetative
def findIndexoccur(arr, target, index):
    if index == len(arr) - 1:
        return;
    if arr[index] == target:
        temp.append(index)
    findIndexoccur(arr, target, index + 1)


res = findIndexoccur([12, 13, 14, 15, 15, 16], 15, 0)
print(temp)
