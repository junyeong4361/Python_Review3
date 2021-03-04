# while.py

'''
    [반복문]
        조건에 만족하면 수행한다. (조건문과 동일)
            >단, 조건에 만족하지 않을 때 까지

        1. while문
            - 조건식이 참이면 수행문 수행
            - if문과 기본 구조가 동일
                > if문 : 조건이 참이면 수행하고 끝
                > while문: 조건이 참이면 수행하고 다시 조건식을 비교

        [while문 기본 구조]
            while 조건식:
                수행문
                수행문

    [while문 수행 순서]
        1. 조건식 판별
        2. 수행문 수행 (True)
        3. 조건식 판별 부터 반복 (조건->수행->조건->수행->...)
        
'''

# while 문 사용

num = 0

while num < 3:
    print(f"num = {num}")
    num += 1 # num = num+1

print("while문 끝! num=", num)

'''
    (1) 무한반복
        num의 값을 수행문에서 증가시키지 않으면 조건식에서 비교 대상인 num의 값이
        계속 동일하기 때문에 항상 조건이 만족하여 반복문이 끝나지 않는다. -> 무한반복 현상
        ctrl +c : 강제 종료

    (2) 조건 변수
        num과 같이 조건식의 비교에 사용되는 변수를 '조건 변수'라고 한다.
        조건변수를 어떻게 다루었는지에 따라 반복 횟수가 정해진다.

    초기 값 (조건변수 생성)
    while 조건식: (조건변수 사용)
        수행문 (반복해서 수행하고 싶은 코드 + 조건변수의 변화식)
'''
'''

# 반복 횟수 지정
count = int(input("반복 횟수 입력: ")) # 조건변수 생성

while count > 0:
    print(f"count = {count}")
    count -= 1
'''

# 특정 조건 만족
# x를 입력하면 종료
input_str = 0

while input_str != "x":
    input_str = input("x를 입력하면 종료 :")

print("good")


'''
    반복문 공통사항
        1. break문 : 반복문을 끝낸다. (종료)

        2. continue문 : 수행을 끝낸다. (다음 식으로 이동)

'''

# break문 사용
'''
while True: # 무한 반복
    input_str = input("x를 입력하면 종료 : ")

    if input_str == "x":
        break # 반복문 안에서만 사용이 가능
'''
print()

# continue문 사용

num = 1
while num < 10: # num이 10보다 작을 떄 수행하겠다.
    if num % 2 == 0: # 짝수 일 때 수행하겠다.
        num += 1 # 
        continue # 수행문을 끝낸다.
    print("num = {}".format(num))
    num += 1

'''
    break, continue은 '반복문'안에서만 쓰인다.
    단, if문이 필요하다.
    if문 없는 break = 무조건 반복 종료
    if문 없는 continue = 무조건 조건식 이동
'''

# while문을 이용하여 1~10까지의 합계 구하기

# 1. 합계를 누적할 변수 필요
# 2. 1 ~ 10까지 증가할 변수 필요
# 3. while문에서 1~10까지 총 10회 반복
# 4. 1~10까지의 숫자들을 누적
# 5. 누적된 숫자를 출력

my_sum = 0
num = 1

while num < 11: # num <= 10
    my_sum = my_sum + num # my_sum += num
    num = num + 1# num += 1
    #print("1~10까지 합 :", my_sum)
    '''
    my_sum : 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
    num    : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    my_sum + num : 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
    '''
print("1~10까지 합 :", my_sum)





# while문 연습

'''
    1. 1부터 입력 받은 수까지 합 구하기
    [출력결과]
    숫자 입력 : 5
    1~5까지 합은 15입니다.
'''
"""
my_sum = 0
num = 1
num2 = int(input("숫자 입력: "))

while num <= num2:
    my_sum = my_sum + num
    num = num + 1

    '''
    my_sum       : 0, 1, 3, 6, 10, 15
    num          : 1, 2, 3, 4, 5,
    my_sum + num : 1, 3, 6, 10, 15,
    '''

print(f"1~{num2}까지 합은 {my_sum}입니다.")
"""
'''
    2. 구구단 7단 출력하기
        [출력결과]
        7 * 1 = 7
        ...
        7 * 9 = 63
'''
num1 = 7
num2 = 1

while num2 <= 9:
    print(f"{num1} * {num2} = {num1 * num2}")
    num2 += 1


'''
    3. 입력 받은 단 출력하기
        [출력결과]
        단을 입력하세요 : 5
        5 * 1 = 5
        ...
        5 * 9 = 45
'''
"""
dan = int(input("단을 입력하세요 : "))
num1 = 1

while num1 <= 9:
    print(f"{dan} * {num1} = {dan * num1}")
    num1 += 1
"""
'''
    4. * 찍기
        - 입력된 숫자만큼 아래와 같은 모양으로 별 찍기
        - 조건변수를 증가시키며 문자열 연산을 하면 매우 편하게 출력할 수 있다.

    [출력결과]
    숫자 입력 : 5
    *
    **
    ***
    ****
    *****
'''
"""
number = int(input("숫자 입력 :"))
hello = 1

while hello <= number:
    print("*"*hello)
    hello += 1
"""










