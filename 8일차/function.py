# function.py

'''
    [함수] - method
        - 특정 작업을 수행하는 일련의 문장들을 하나로 묶은 것

        - 함수의 장점
            1. 한 번 만들어 놓으면 언제든지 재사용 가능
            2. 중복된 코드 제거
            3. 프로그램의 구조화
                > 작업 단위로 묶어서 구조화 시킨다.


        [함수의 기본 구조]
        def 함수이름(매개변수1, 매개변수2, ...):
            수행문
            return 반환 값


    1. 매개변수 (parameter)
        - 함수가 호출될 때 값을 받을 '변수'
        - 개수 제한이 없고, 필요 없으면 생략도 가능
        - 우리가 함수를 호출할 때 전달하는 '값'을 인수라고 한다.
            > argument

    2. 반환 값
        - return 뒤에 오는 값은 함수의 수행이 완료되고 되돌려주는 값
        - return 을 사용하면 함수의 수행이 끝난다.
            >마치 반복문의 break와 같은 효과

    3. 매개변수와 반환 값의 유/무에 따른 함수 형태 (4가지)
        1. 매개변수와 반환 값 둘 다 있다.
        2. 매개변수와 반환 값 둘 다 없다.
        3. 매개변수만 있다.
        4. 반환 값만 있다.
            > 만드는 목적에 따라 알아서 사용

    > 함수는 define(정의) 하기만 하면 프로그램 수행에 영향이 없다.
    > 함수를 호출하면, 코드의 흐름이 내가 호출한 함수의 수행문으로 '점프'
      함수의 수행문이 끝나면, '함수를 호출했던 원래 위치'로 되돌아온다.
      단, return 반환 값이 있다면 그 값을 들고 온다.



'''
# 함수 4가지 형태
# 1. 매개변수, 반환 값

def add(a, b):
    return a + b

# 호출 -> 함수명(인자값1, 인자값2, ...)
# add함수는 매개변수가 2개 -> 사용하려면 값을 2개 전달해줘야 한다.

result=add(10, 3) # 변수에 대입 용도
print("result =", result)

print("3 + 5 = ", add(3,5)) # print()안에서 사용
# 함수의 호출코드는 return 뒤에 있는 값으로 바뀐다.
print()

# 2. 매개변수, 반환 값 없다.

def print_hi():
    print("hi~~!hi~~!")
    print("안녕~ 안녕~")

# 반환 값이 없을 때는 호출만 한다.
print_hi()

# 매개변수에 따라 함수를 호출할 때는 그 규칙을 맞춰줘야 한다.
# 매개변수의 개수에 맞게 인자값을 전달!

result = print_hi()
print("result =", result)
# None은 아무것도 들어 있지 않을때의 값
print(print_hi())
# 변수에 대입하거나 어딘가에 사용하면 None이라는 값이 된다.

# 3. 매개변수만 있다.
def say(talk):
    print(talk)

say("파이썬~~")
say([1, 2, 3])

# 4. 반환 값만 있다.
def get_data():
    return "문자열~~~!"

print(get_data())
data= get_data()
print(data)
# return 뒤에 오는 값의 자료형에 따라 반환된 결과도 그 자료형이 된다.
# 1개 또는 0개


'''
    입력한 숫자가 짝수인지 홀수인지 0인지 판별하는 함수를 작성
    2가지 형태로 작성 (반환 값이 있는 형태, 없는 형태)

    [출력결과]
    숫자 입력 : 20
    함수1 : 짝수입니다.
    함수2 : 짝수입니다.
'''

def Even_Number1(num):
    if num % 2 == 0 and num != 0:
        return "짝수"
    elif num % 2 == 1:
        return "홀수"
    return "0"

def Even_Number2(num):
    result = 0
    if num % 2 == 0 and num != 0:
        result = "짝수"
    elif num % 2 == 1:
        result = "홀수"
    else:
        restul = "0"
    print("함수2 : {}입니다.".format(result))

input_num = int(input("숫자 입력 : "))
print(f"함수1 : {Even_Number1(input_num)}입니다.")
Even_Number2(input_num)



