for i in range(1, 101):
    p = i
    if i % 3 == 0:
        p = 'Fizz'
        if i % 5 == 0:
            p = 'FizzBuzz'
    elif i % 5 == 0:
        p = 'Buzz'
    print(p)