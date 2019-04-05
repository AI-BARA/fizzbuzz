for i in range(1,101):
    fizzbuzz_list = ['FizzBuzz', i, i, 'Fizz', i, 'Buzz', 'Fizz', i, i, 'Fizz', 'Buzz', i, 'Fizz', i, i]
    print(fizzbuzz_list[i%15])