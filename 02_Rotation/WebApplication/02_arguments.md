# Class & Arguments


## 위치기반 매개변수 Positional arguments
```python
def func1(argument1, argument2, argument3):
    print(f'위치기반 매개변수는 순서대로 매칭된다.\
    {argument1}, {argument2}, {argument3}')
```
일반적으로 사용하는 인자로, 함수에 인자를 넘기는 순서대로 인자가 할당된다.

## 키워드기반 매개변수 Keyword arguments
```python
def func2(name="이름", age="나이", status="배고프다"):
    print(f"저는 {name}이고 {age}세 이며 현재 {status}")
```
- 변수에 이름을 지정하여 함수에 인자를 넘긴다.
- 주의: 키워드 기반 매개변수는 위치기반 매개변수 다음에 위치해야 한다.



## 선택형 매개변수 Optional arguments
- 평소에 사용하지 않지만 가끔 필요할 때가 있는 경우에 사용한다.
- 관습적으로 args, kwargs를 이름으로 사용하지만 다른 이름을 사용해도 상관 없다. 

### `*args`
```python
def func3(name, price, `*args`):
    print(f'이 인자는 optional argument 입니다.: {args}')
    print(type(args))

func3('이름', '100')
# 이 인자는 optional argument 입니다.: ()
# <class 'tuple'>  

func3('이름2', '1000', '선택!')
# 이 인자는 optional argument 입니다.: ('선택')
# <class 'tuple'>  
```

- arguments의 약자
- `*args` 를 이용해 선택적으로 위치기반 인자를 넘길 수 있다. 
- tuple 안에 선택형 매개변수를 담을 수 있다.

### `**kwargs`
```python
def func3(name, price, `**kwargs`):
    print(f'이 인자는 optional argument 입니다.: {kwargs}')
    print(type(kwargs))

func3('이름', '100')
# 이 인자는 optional argument 입니다.: ()
# <class 'dict'>  

func3('이름2', '1000', keyword_1 = '선택!', keyword_2 = '선택2!')
# 이 인자는 optional argument 입니다.: {keyword_1 : '선택!', keyword_2 : '선택2!'}
# <class 'dict'>  
```

- keyword arguments의 약자
- `**kwargs`를 이용해 키워드 기반 인자를 넘길 수 있다.
- dict 안에 선택형 매개변수를 담을 수 있다. 접근하는 방식 역시 dict 데이터를 다룰때와 같다.

## 우선순위
1. 위치기반 매개변수
2. 키워드기반 매개변수
3. 선택적 매개변수 : 위치기반 매개변수 (`*args`)
4. 선택적 매개변수 : 키워드기반 매개변수 (`**kwargs`)