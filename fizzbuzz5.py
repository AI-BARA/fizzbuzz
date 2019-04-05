a = ''
for i in range(100):
    a += str(i %3//2*"Fizz"+ i %5//4*"Buzz" or i+1) + '\n'
print(a)