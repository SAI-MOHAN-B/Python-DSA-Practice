# Find the Prime Numbers in the array
temp = []
def isprime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i = i+1
    return True

n = 50
for i in range(1,n+1):
    if isprime(i):
        temp.append(i)
print(",".join([str(s) for s in temp]))
