#funkcja zwraca listę x kolejnych wyrazów ciągu Fibonacci'ego
def fibonacci_string(x):
    if x == 0:
        string = []

    elif x == 1:
        string = [1]
    else:
        x = x-2
        string = [1, 1]
        y = 0
        while y < x:
            n = string[y] + string [y+1]
            string.append(n)
            y += 1
    print(string)

print('Podaj ile wyrazów ciągu Fibonacciego chcesz uzyskać:')
n = input()
n = int(n)
fibonacci_string(n)