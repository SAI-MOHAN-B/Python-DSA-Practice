def search_2d(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return [i,j]
    return [-1,-1]
arr = [[23,3,1],[18,12,3,9],[78,99,34,56],[18,12]]
res_arr = search_2d(arr,35)
print(res_arr)

        
   
