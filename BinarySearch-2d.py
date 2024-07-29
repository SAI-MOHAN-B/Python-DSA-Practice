def search(arr,target):
    row = 0;
    col = len(arr) -1
    while(row<len(arr) and col >=0):
        if target == arr[row][col]:
            return [row,col]
        if target > arr[row][col]:
            row+=1
        else:
            col-=1
    return [-1,-1]
arr = [[10,20,30,40],[15,25,35,45],[28,29,37,49],[33,34,38,50]]
res = search(arr,11)
print(f"the index of the target is",res)
