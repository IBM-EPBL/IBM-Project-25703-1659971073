#Program to display odd numbers from m to n
m, n = map(int, input("Enter m and n values: ").split())
while m < n:
    if m % 2 != 0:
        print(m)
    m += 1