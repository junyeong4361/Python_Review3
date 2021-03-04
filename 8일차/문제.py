'''
    1 ~ 10 사이의 두 수를 입력 받기
    1 ~ 100까지 전달된 두 수의 공배수를 출력하는 함수 만들기 (반환x)
        > 매개변수 2개, 변환 값 없음

        [출력결과]
        두 수 입력 : 3 5
        결과 : 15 30 45 60 75 90
'''

def hi(num1, num2):
    result = 0
    for i in range(1, 101):
        if i % num1 == 0 and i % num2 == 0:
            result = i
            print(f"{result} ", end = "")

num1, num2 = map(int, input("두 수 입력: ").split())
hi(num1, num2)


'''
    로또 번호 만들기 (함수로 구현 - 매개변수, 반환 값 자유)

    숫자를 입력받아 입력한 숫자만큼 로또 숫자 생성 (5를 입력하면 6개의 숫자를 5번 만든다.)
    1 ~ 45까지 숫자들 리스트로 생성
    랜덤한 숫자로 6개의 숫자를 가져온다.(중복 되면 안됨)
    가져온 숫자들을 오름차순으로 정렬하여 출력 
    (리스트 관련 함수 이용하여 로또 번호 만들기)

    [출력결과]
    로또 번호 횟수 입력 : 3
    [3, 6, 11, 16, 19, 33]
    [7, 13, 14, 15, 19, 22]
    [9, 10, 20, 22, 23, 24]
'''

import random

def Lotto_init(): # 1 ~ 45숫자 만들기 
    lotto = []
    choicelotto = []
    for i in range(1, 46):
        lotto.append(i)
    return [lotto, choicelotto]

def Lotto_Game(num):
    lotto, choicelotto = Lotto_init()
    i = 0
    while i < num:
        for j in range(6): # 6회 반복 (6개 숫자) 
            index = random.randint(0, 44-j) # 인덱스로 사용할 랜덤한 숫자생성
            choicelotto.append(lotto.pop(index)) # 랜덤한 숫자 하나씩 추가 
        choicelotto.sort() # 만들어진 로또 번호 정렬
        print(choicelotto) # 로또 출력 
        i += 1
        lotto, choicelotto = Lotto_init()

input_num = int(input("로또 횟수 입력 : "))
Lotto_Game(input_num)

