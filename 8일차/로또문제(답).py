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












