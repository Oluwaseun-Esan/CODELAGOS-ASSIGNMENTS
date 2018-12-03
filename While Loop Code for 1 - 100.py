x = float(input('Enter a value  '))
while (x<=100):
    print(x)
    x+=1
    if(x%3==0):
        print(x,' Fizz')
    elif(x%5==0):
            print(x,' Buzz')
    if(x%3==0 and x%5==0):
            print(x,' FizzBuzz')
