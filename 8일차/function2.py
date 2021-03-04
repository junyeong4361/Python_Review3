# function2.py

def calc(a, b):
    return a+b, a-b, a*b, a/b # 여러 개처럼 보이지만 튜플 

result = calc(10, 5)
print(result) 
print()

# 매개변수에 초기 값 사용
'''
def print_info(name, age, phone="010-xxxx-xxxx"):
    print("이름 :", name)
    print("나이 :", age)
    print("전화번호 :", phone)

print_info("아이유", 20, "112")
print_info("유재석", 40)
# 초기 값이 지정된 매개변수에 값을 주면 내가 준 값으로 변경
# 값을 주지 않으면 초기 값을 그대로 사용
# 초기 값이 들어가는 매개변수는 맨 뒤에 위치해야 한다.
'''

# 키워드 인수 : 함수의 매개변수명을 키워드로 사용
def print_info(name, age, phone):
    print("이름 :", name)
    print("나이 :", age)
    print("전화번호 :", phone)

print_info(phone="119", name="김종국", age=33)
print()

# 가변인수 : 전달하는 값의 개수가 변할 수 있다.
# 어떤 것이든 다 받아준다.
# 없어도 동작한다.
# 사용할때 *을 떼면 튜플로 동작한다.

def add(*args):
    print(args) # *떼면 튜플
    my_sum = 0
    for i in args:
        my_sum += i
    return my_sum


print(add(1, 2, 3, 4))
print()

# 일반 매개변수, 가변인수를 혼용할 때는 가변인수는 마지막에 위치
'''
def f(*args, a, b):
    return a+b

f(1, 2, 3, 4, 5, a=10, b=20)
'''


