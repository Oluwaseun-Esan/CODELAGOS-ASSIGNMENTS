#STUDENT'S GRADE CALCULATOR

x = float(input('Enter Student\'s Final_Score: '))

if (x>100):
    print ('Student\'s Grade = A')
if (70<=x<=100):
    print ('Student\'s Grade = A') 
elif (60<=x<=69):
    print ('Student\'s Grade = B') 
elif (50<=x<=59):
    print ('Student\'s Grade = C') 
elif (45<=x<=49):
    print ('Student\'s Grade = D') 
elif (40<=x<=44):
    print ('Student\'s Grade = E') 
elif (0<=x<=39):
    print ('Student\'s Grade = F') 
elif (x < 0):
    print ('Student\'s Grade = F')
