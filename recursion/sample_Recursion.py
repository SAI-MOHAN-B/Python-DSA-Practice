def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n-1)
print_num(6)


def print_data(n):
    if n > 50:
        return
    print(n)
    print_data(n+5)
print_data(5)

def print_numbers(n):
    if n > 10:
        return
    print(n)
    print_numbers(n+1)
print_numbers(1)

def funrev(n):
    if n == 0:
        return
    funrev(n-1)
    print(n)
funrev(5)
    
