x = float(input('Enter a value '))
while (x<=100):
    if(x%3==0 and x%5==0):
        print('FizzBuzz')
    if(x%3==0):
        print('Fizz')
    elif(x%5==0):
        print('Buzz')
    else:
        print(x)
    x+=1
