## 숫자 자료형, 정수와 실수가 있다.
# a = 10
# c = 3
# print(a)
# print("########")
# print(a+c) #더하기
# print(a/c) #나눗셈
# print(a//c) #나눗셈의 몫
# print(a*c) #곱하기
# print(a-c) #빼기
# print(a%c) #나머지
# print("################")

# print(type(a//c))
# print(type(a/c))


# 문자 자료형

# a = "hello"
# b = 'good'
# print(a)
# print(b)
# print(a+b)
# # print(a-b) #에러가 뜨는데 에러뜨는것을 읽어봅시다.
# print(a * 10)
# print(a[1])
# print("a의 slicing : ", a[1])
# print(a[1:3])
# print(a.replace("h","g"))
# print(a)


# # 쉬어가는 부분

# myvar = input()
# # myvar = input("입력해주세요")
# print(myvar)
# print(type(myvar))


# #리스트 자료형
# mylist = list()
# mylist2 = []

# b = [1, 2, 3]    #숫자로 이루어진 List
# c = ['a','b','c','d']  #문자로 이루어진 List
# d = [1, 2, 'Life', 'is'] #숫자와 문자로 이루어진 List
# e = [1, 2, ['Life', 'is']] #숫자와 List로 이루어진 List

# b[2] = 100
# #list의 method

# mylist.append("첫째")
# mylist.append("둘째")
# mylist.append("셋째")
# print(mylist)
# mylist.remove("둘째")
# print(mylist)
# mylist.pop()
# print(mylist)
# tmp_list = [1,5,7,4,7,22] 
# tmp_list.reverse()     #역순
# print(tmp_list)
# tmp_list.sort()        #오름차순
# print(tmp_list)

# print(tmp_list.count(7))

# print(tmp_list[3])
# print(tmp_list[3:6])
# print(tmp_list[:4])
# print(tmp_list[1:])

# tmp_str = "+".join(c)
# print(tmp_str)

# return_list = tmp_str.split("+")
# print(return_list)



# #튜플 자료형
# tuple1 = ()
# tuple2 = (1,)
# tuple3 = (1,2,3)
# tuple4 = 1,2,3
# tuple5 = ('a','b',('ab','cd'))
# print(tuple5)

# #변경이불가능하다는것 말고는 list와 비슷한 속성을 가진다


#딕셔너리 자료형
#key-value로 이루어진 자료형
mydict = {1:'hello'}
mydict2=dict()
mydict22={}
mydict3 = {'이름':'장치훈','나이':12,'특징':['하나','둘']}
mydict3['추가']='내용'
print("*"*50,type(mydict2),type(mydict22))
print(mydict)
print(mydict[1])
print(mydict3)
print(mydict3.keys())
print(mydict3.values())
print(mydict3.items())
print(mydict3['이름'])
print(mydict3.get('이름'))
print(mydict3.get('성별'))
print(mydict3.get('성별','입력을 안했습니다'))

print("키가 딕셔너리 안에 있나?", '이름' in mydict3)
print("키가 딕셔너리 안에 있나?", '장치훈' in mydict3)
print("키가 딕셔너리 안에 있나?", '성별' in mydict3)
