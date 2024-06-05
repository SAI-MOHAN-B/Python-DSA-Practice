def search_string(str,ch):
   for i in range(len(str)):
    if len(str) == 0:
        return False
    if str[i] == ch:
        return True
    return False
data = search_string("mohan","s")
print(data)