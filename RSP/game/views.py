from django.shortcuts import render
import random

# Create your views here.

list = ["가위","바위","보"]

win = 0
lose = 0

def index(request) :
    
    
    if request.GET.get("user_decision") :
        com_decision = random.choice(list)
        user_decision = request.GET.get("user_decision")
        
        if com_decision == user_decision :
            print("비겼습니다.")
            continue
        elif com_decision == "가위" && user_decision == "바위" :
            print("이겼습니다.")
            win += 1
            continue
        elif com_decision == "가위" && user_decision == "보" :
            print("졌습니다.")
            lose += 1
            continue
        elif com_decision == "바위" && user_decision == "보" :
            print("이겼습니다.")
            win += 1
            continue
        elif com_decision == "바위" && user_decision == "가위" :
            print("졌습니다.")
            lose += 1
            continue
        elif com_decision == "보" && user_decision == "가위" :
            print("이겼습니다.")
            win += 1
            continue
        elif com_decision == "보" && user_decision == "바위" :
            print("졌습니다.")
            lose += 
            continue
        elif user_decision == "그만" :
            print(win,"W ",lose,"L")
            break
    