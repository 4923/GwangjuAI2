# Python 3강 : function, Class

### 함수 function
필요한 전달 값을 받아, 특정 작업을 수행한 후 결과값을 반환(return)하는 코드블록
- 장점
    + 쉬운 사용 : 함수의 내부 구조를 몰라도 함수를 실행했을 때 어떤 결과가 나오는지만 알면 사용할 수 있다.
    + 반복 가용 : 함수를 여러 번 호출함으로써 반복되는 작업을 줄일 수 있다.

```python
# 함수 생성
def print_hello():  # 함수 선언
    print('Hello World!') # 일반 출력
    return # 반환
```

1. 기본 틀
함수를 생성할 때 사용하는 **예약어** `def`는 define의 약자다.  
기본 틀은 ` def 함수이름(전달값의 변수):`를 따른다.

2. 반환 return
함수가 종료될 때 넘겨주는 결과값  
코드블럭 안의 코드와는 다르게 변수 또는 값만을 할당한다.

3. 내장함수 built-in function
자체적으로 함수를 제작할 수도 있지만 이미 제작된 함수도 있다. 이를 내장 함수라고 한다.  
외부 모듈과는 다르게 `import`가 필요하지 않다.

```python
# example
a = [1, 2, 3, 4, 5]
len(a)  # 길이 반환
# >> 5

a = input('your input : ')  # 입력
# >> your input : 

list(range(0, 3, 1))  # 순회
# [1, 3, 5, 7, 9]
```

### 클래스 Class
```python
class Class_name:
    variable = 1
    variable2 = 2
    def func_name(self, parameter1, ...):
        print('this is method : funcion of class')
        print('self called class itself', self.variable)
```

1. 기본 틀  
클래스를 생성할 때 사용하는 **예약어** `class`다.  
기본 틀은 ` class 클래스이름:`를 따른다.
- 클래스는 __init__에서 생성자를 생성했을 때에만 인자를 받는다.
- 인자가 없더라도 클래스를 선언할 때에는 `클래스이름()` 형식을 따른다.

2. 인스턴스  
클래스를 변수로 지정할 때 이 변수를 인스턴스라고 한다.  
인스턴스는 클래스에 속한 변수와 함수를 모두 사용할 수 있다.  
클래스 안에 속한 변수나 함수에 접근할 때 `.` 을 사용한다.

3. 다른 파이썬 파일의 클래스 활용하기  
from과 import를 활용한다.
```python
# if 'python_file_name.py' has 'class_name'
from python_file_name import class_name
```
