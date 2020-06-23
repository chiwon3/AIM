import random

"바위"=="묵"
"가위"=="찌"
"보"=="빠"

list = ["가위", "바위", "보"]

com_decision = random.choice(list)

input_Value = input("가위바위보 중 하나를 입력하세요.  ")

if input_Value == '가위' :
    if com_decision == '가위':
        print("비겼습니다.")
    elif com_decision == '바위':
        print("졌습니다.")
    else :
        print("이겼습니다.")
elif input_Value == '바위' :
    if com_decision == '가위':
        print("이겼습니다.")
    elif com_decision == '바위':
        print("비겼습니다.")
    else :
        print("졌습니다.")
else :
    if com_decision == '가위':
        print("졌습니다.")
    elif com_decision == '바위':
        print("이겼습니다.")
    else :
        print("비겼습니다.")