# for number1 in range(2,10) :
#     for number2 in range(2,10) :
#         print(number1,"*",number2,"=",number1*number2)
        
import random
    
chance = 1

def gugudan ():
    a=random.randrange(2,10)
    b=random.randrange(2,10)
    
    answer = a * b
    
    print(str(chance)+"번째 문제입니다.")
    
    input_value = int(input( str(a) + "*" + str(b) + "=" ))
    
    if (answer==input_value):
        print("정답입니다.")
    else :
        print("오답입니다.")
        return False
    
while True :
    gogo = gugudan()
    if gogo == False:
        chance = chance-1
        print(str(chance) + "회 맞추었습니다.")
        break
    else :
        chance = chance+1