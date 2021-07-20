# decorators


# # without decorator
# def hello_world(input_text):
#     print("start!")
#     print("\t", input_text)
#     print("end!")


# hello_world("hello_world")

"""decorator 선언"""


def decorator(func):  # function을 parameter로 받는다.
    # 함수 안에 새로움 함수를 또 선언한다 : decorated, decorated의 인자는 func의 인자 (hello_world의 인자 input_text)
    def decorated(input_text):
        print("start!")
        # 인자로 받은 함수 : func을 호출한다.
        func(input_text)
        print("end!")

    return decorated  # 꾸며진 함수를 반환한다. (func X hello_World X **decorsated O**)


"""decorator 사용"""


@decorator  # 1. @로 decorator를 불러와서
def hello_world(input_text):
    print(input_text)


# 2. 함수 실행
hello_world("hello_world")

# 3. 실행 결과
# start!
# hello_world
# end!

# 원래 hello_world는 input_text를 출력하는 기능만 설정되어있는데
# decorator를 사용하면 앞 뒤에 꾸며주는 문구도 추가된다.
