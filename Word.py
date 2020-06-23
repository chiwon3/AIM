print("끝말잇기 시작")


word = input()

if (len(word)==0) :
    print("글자를 입력하지 않았습니다.")
else :
    while True :
        word_last = word[-1]
        word = input()
        if (len(word)!=0 and word[0] == word_last):
            continue
        elif (len(word)==0) :
            print("글자를 입력하지 않았습니다.")
            break
        else:
            print("틀렸습니다. 게임이 종료됩니다.")
            break
