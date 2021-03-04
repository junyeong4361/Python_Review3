# global.py

'''
    [전역변수, 지역변수]

    전역변수 : 전체 영역에서 사용가능한 변수
        > 우리가 사용했던 변수

    지역변수 : 특정 지역에서만 사용가능한 변수 #특정지역: 들여쓰기 공간
'''

value = "전역변수" # 만들어진 뒤부터 어디서든 사용 가능

def fn1():
    print("fn1 호출!")
    print(value)

def fn2():
    print("fn2 호출!")
    value_fn2 = "fn2의 지역변수"
    print(value_fn2)
    value="지역변수로 변경!"
    print(value)
    # 지역에서 value에 값을 대입하게 되면 (전역변수 value가 있는데)
    # 전역변수 value의 값이 변경되는게 아니라 같은 이름으로
    # 이 지역의 value 지역변수가 생성
    
fn1()
fn2()
#print(value_fn2)
print(value)
print()

def fn3():
    print("fn3 호출!")
    global value_fn3 # 지역변수를 전역변수로 만드는 명령
    value_fn3 = "지역변수~~~"

fn3()
print(value_fn3)
# fn(3)이 호출되어야 value_fn3 이라는 변수가 생성
