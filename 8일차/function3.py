# function3.py

def func3(num):
    print("func3() 시작, num =", num)
    print("func3() 끝, num =", num)

def func2(num):
    print("func2() 시작, num =", num)
    func3(num - 1)
    print("func2() 끝, num =", num)
    
def func1(num):
    print("func1() 시작, num =", num) 
    func2(num - 1)
    print("func1() 끝, num =", num)

func1(3)

'''
    재귀 함수
        - 함수의 수행문 안에서 나 자기 자신 함수를 다시 호출하는 함수
        - 수행문이 반복되기 때문에 반복문과 유사한 성격
        - 너무 많이 반복 수행하다보면 프로그램 오류 발생
        - 함수 호출 시 'stack'이라는 구조의 메모리를 사용
        Queue : First In, First Out (FIFO) - 입구/출구 따로 # 1등먼저 나감
        Stack : First In, Last Out (FILO) - 출입구 하나 # 꼴등먼저 나감
            > Stack 용량이 초과될 정도로 많이 호출하면 오류
            > StackOverFlow 오류라고 한다.
            > 함수 호출 시 Stack을 사용하는 이유는
              함수 수행이 끝난 후 돌아갈 위치를 저장

        - 재귀함수도 반복문 처럼 반복 호출이 끝날 수 있는 조건이 필요
        
'''

def fn(num):
    print("fn() 시작, num =", num)
    if num == 1:
        print("fn() 끝, num =", num)
        return # 함수에서 반환 값 없이 return만 쓰면 함수 종료
    fn(num - 1) # 재귀호출 (자기 자신 함수 다시 호출)
    print("fn() 끝, num =", num)


fn(3)



