
def linear_search(arr,key):
    if len(arr) == 0:
        return False
    for i in range(len(arr)):
        element = arr[i]
        if element ==  key:
            return True
    return False
arr = [12,13,14,15]
data = linear_search(arr,14)
print(data)
    