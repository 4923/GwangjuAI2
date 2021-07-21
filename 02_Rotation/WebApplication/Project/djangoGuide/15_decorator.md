# decorator
decorator를 함수를 인자로 받는다.
python은 웬만한 모든 자료형을 인자로 받을 수 있는데 그 안에 func도 포함된다.

decorator는 함수를 인자로 받고, 인자로 받은 함수의 앞 뒤를 꾸며준 후 다시 반환한다.

- 인자로 받은 함수를 감싼 새로운 함수를 선언한다. : `decorated`
- 감싸진 함수를 다시 리턴한다.

반복되는 구문을 decorator로 꾸며 중복을 막을 수 있다.

> 실습 
- hello_world 함수 작성 (함수 내용 자유)
- 함수의 시작, 종료를 출력하는 decorator 생성
`decorators.py`


> 실습 2
- 함수 작성
    - 삼각형의 넓이 계산 함수
    - 사각형의 넓이 계산 함수
- decorator 작성
    - 입력값이 양수인지 확인
    - 아닐경우 Error 발생
- `decorators2.py`


> 실습 3
- User 클래스 작성
    - User 클래스 내 is_authenticated 변수 작성
- User 객체를 넓이 함수 인자로 전달
- is_authenticated 변수를 확인하고 True가 아닐 경우 Error 발생
- `decorators3.py`