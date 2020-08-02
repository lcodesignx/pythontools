def fibonnacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonnacci(n - 1) + fibonnacci(n - 2)

for n in range(1, 101):
    print(n, ':', fibonnacci(n))
