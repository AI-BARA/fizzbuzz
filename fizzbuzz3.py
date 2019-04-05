def fizzbuzz(count):
    while count % 15 == 0:
        return 'FizzBuzz'
    while count % 3 == 0:
        return 'Fizz'
    while count % 5 == 0:
        return 'Buzz'
    return count

for i in range(1, 101):
    print(fizzbuzz(i))