def fizzBuzz1(n):
    # Write your code here
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ('FizzBuzz')
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print ('Buzz')
        else:
            print (str(i))




def fizzBuzz2(n):
    numberRange = range(1, n+1)
    for i in numberRange:
        if i % 3 == 0 and i % 5 == 0:
          print ('FizzBuzz')
        elif i % 3 == 0:
          print ('Fizz')
        elif i % 5 == 0:
          print ('Buzz')
        else:  
          print (i)
