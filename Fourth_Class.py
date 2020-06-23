print('출생연도를 입력하세요 : ')
year = input()
길이 = len(year)
if (길이 == 4):
    if (year[-1]=='0' or year[-1]=='5') :
        print('금요일에 구매하세요')
    elif (year[-1]=='1' or year[-1]=='6') :
        print('월요일에 구매하세요')
    elif (year[-1]=='2' or year[-1]=='7') :
        print('화요일에 구매하세요')
    elif (year[-1]=='3' or year[-1]=='8') :
        print('수요일에 구매하세요')
    elif (year[-1]=='4' or year[-1]=='9') :
        print('목요일에 구매하세요')
    else:
        print('주말에 구매하세요')
else :
    print('출생연도를 잘못 입력하였습니다.')
    
for f in [1,2,3,4,5] :
    print('f의 값은 ',f)
for fr in range(6) :
    print('fr의 값은 ',fr)
text = '안녕하세요'
for txt in range( len(text)) :
    print('text의 값은 ',txt)
w = 0
while w < 5:
    print('w의 값은 ',w)
    w = w+1

def forfunction(a):
    for i in range(a) :
        print(a)

forfunction(5)
print("*" * 100)
forfunction(10)

def hellofunction(hello) :
    for i in range(hello) :
        print('hello')

hellofunction(10)

def sumfunction(o,p):
    q = o+p
    return q  # 리턴 명령어를 만나면 디파인 함수는 종료된다 / 밑에 무슨 함수를 넣어도 동작 안함

print(sumfunction(1,2))

for br in range(10):
    if (br==8):
        break # break는 조건을 만족하는 순간 가장 가까운 반복문(for, while)을 깨부수고 나옴
    print(br)

for con in range(5):
    if (con==2):
        continue # continue는 조건을 만족하는 순간 아래의 명령어를 수행하지 않고 다시 반복문 처음으로 돌아와서 다음 동작을 수행
    print(con)


# 강제종료 하고 싶을때는 컨트롤C 누르면 종료