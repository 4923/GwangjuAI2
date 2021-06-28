# Class

## 왜 클래스를 사용하는가?
> 프로그램 순서와 자료구조를 분리할 수 있다.

프로그램에 접근하는 방식이 달라진다. 기능에 따라 클래스를 만들고 세부 기능을 메소드로 만들기 때문에 흐름을 정하기에 쉽다.

## 클래스란?
### 프로그램 언어의 종류
1. 절차 지향 Procedure Programming
2. 객체 지향 Object oriented Programming

- 지향이라는 것이지 강제하는것이 아니다. 프로그래밍 방식에 따라 다양한 지향성을 가질 수 있다.
- 지향으로 언어를 나누는 기준 : 언어가 가지는 특성을 반영
- 두 방식을 나누는 가장 큰 개념은 `Class`다.
- 객체지향과 절차지향은 반대되는 개념이 **아니다.**

### 클래스?
클래스라는 것은 실제로 존재하지 않는 **추상체**다. 이를 실체로 만든 것이 **객체**, 즉 **인스턴스**다.
```python
class Car():
    pass

santafe = Car()

# Car : 객체
# santafe : 인스턴스
```

### 객체변수
```python
class Car:
    def __init__(self):
        self.number = '12가3456'    # 객체 변수
        self.company = '현대'
        self.model_name = 'Santafe'

santafe = Car()     # initializer의 self는 객체 자신을 말한다.
```
[velog | self 이해하기](https://velog.io/@magnoliarfsit/RePython-1.-self-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)

### `super()`
부모 클래스에 접근하여 __init__메서드, 초기화 제서드를 재사용할 수 있다.  
[Github @4923 | 참고 TIL](https://github.com/4923/TIL/blob/master/Python/Basic/1_Syntax/Class.md)