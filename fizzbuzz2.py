for i in range(0,91,15):
    print(i+1,i+2,'Fizz', i+4,'Buzz','Fizz', i+7,i+8,'Fizz','Buzz', sep='\n')
    if i + 10 == 100:
        break
    print(i+11,'Fizz',i+13,i+14,'FizzBuzz', sep='\n')