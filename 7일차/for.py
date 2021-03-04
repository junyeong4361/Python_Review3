# for.py

'''
    2. for문
        > 리스트, 튜플, 문자열 등 요소가 나열된 형태의 값을
          첫 요소부터 마지막 요소까지 변수에 대입하며 반복
          

    [for문 기본 구조]
        for 변수 in 요소가 여러개인 값:
            수행문
            수행문

    in의 사용
        if : 포함 되어 있는지 확인하여 True/False
        for : 하나씩 대입
'''
'''

# for문 사용 - 범위 지정 반복문
for i in [1, 2, 3]:
    print("i =", i)
# 요소의 개수가 반복횟수를 나타낸다.

print("for문 끝난 뒤 i=", i)

for str1 in "대한민국":
    print(str1)

for i in [1, 2, 3, 4]:
    print("안녕~")
'''
#for i in [1,2,3,4,5,6,6,7,8,9,9,0,]

'''
    for문을 사용할 때 일반적인 사용법
    range() 함수 : 지정한 범위만큼의 숫자들을 반환

    range(10) : 0~9 (끝은 포함x)
    range(101) : 0~ 100

    range(5, 11) : 5~ 10
    range(1, 101) : 1~ 100

    range(100, 0, -1) :100 ~ 1, 1씩 감소
    range(1, 10, 2) : 1~ 9, 2씩 증가 -> 1, 3, 5, 7, 9
    
'''
'''
for i in range(1, 11):
    print(i)
'''

# for문으로 1~10까지의 합계 구하기
my_sum = 0 # 합계 누적용 변수
for i in range(1, 11):
    my_sum += i

print("1~10까지 합 :", my_sum)
print()

# 입력 횟수만큼 반복
'''
count = int(input("반복 횟수 입력 :"))
for i in range(count, 0, -1):
       print(i)
'''



'''
list1 = [["피카츄", "라이츄"], ["파이리", "리자몽"], ["꼬북이", "거북왕"]]

for str1 in list1:
    print("진화 전:", str1[0])
    print("진화 후:", str1[1])
    print()

print()

'''
#for문의 중첩 : 2중 for문, 3중 for문
'''
for i in range(1, 4):     # i : 1, 2, 3
    for j in range(1, 4): # j : 1, 2, 3
        print(i, j)


'''

'''
for i in range(2, 10): # i : 단 2 ~ 9
    for j in range(1, 10): # j: 곱해지는 숫자 1~9
        print(f"{i} * {j} = {i*j}")
    print()
'''
'''
# 3중 for문
for i in range(1, 4):           # i : 1 ~ 3
    for j in range(1, 4):       # j : 1 ~ 3
        for k in range(1, 4):   # k : 1 ~ 3
            print(i, j, k)
'''
        
# for문 연습
# n의 배수 : 어떤 숫자를 n으로 나눈 나머지가 0   --> num % n == 0 --> num은 n의배수
# 공배수 :    n1과 n2의 공배수 = 둘 다 만족!    num % n1 == 0 and num % n2 == 0
'''
    1. 1부터 입력 받은 수까지 '짝수'의 합 구하기

        [출력결과]
        숫자 입력 : 5
        1~5까지 짝수의 합은 6입니다.
'''
num = int(input("숫자 입력 : "))
my_sum = 0
for i in range(1, num+1):
    if i % 2 == 0:
        my_sum += i
print("1~{}까지 짝수의 합은 {}입니다.".format(num, my_sum))

'''
    2. 1부터 200까지 3과 4의 공배수를 하나의 변수에 '누적'
       누적된 수가 1000을 초과하면 반복문을 '탈출'
       이때, 누적된 수와 마지막에 더했던 공배수를 출력

        [출력결과]
        누적된 수 : 1092
        더한 수 : 156
'''
my_sum = 0
for i in range(1, 201):
    if i % 3 == 0 and i % 4 == 0:
        my_sum += i

    if my_sum > 1000:
        break
print(f"누적된 수 : {my_sum}")
print(f"더한 수 : {i}")

'''
    3. 1~100 사이 정수 중, 3의 배수와 5의 배수를 '역순'으로 출력
       단, 3과 5의 공배수는 <15> 처럼 출력

       [출력결과]
       100 99 96 95 93 <90> 87 ... 5 3

'''
for i in range(100, 0, -1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"<{i}> ", end="")
    elif i % 3 == 0 or i % 5 == 0:
        print(f"{i} ", end="")

print()


'''
    난이도 <상>
    4. 2중for문 구구단 예제를 for문 1개만 사용해서 만들어보기
        - 총 반복 횟수 = 72회
        - 처음 단은 2
        - 곱해지는 숫자는 처음이 1
        - 9회 수행마다, 단이 1 증가, 곱해지는 숫자는 1로 변경
'''

dan = 2
gob = 1

for i in range(72):
    print("{} * {} = {}".format(dan, gob, dan*gob))
    gob += 1

    if gob == 10:
        gob = 1
        dan += 1
        print()
        

