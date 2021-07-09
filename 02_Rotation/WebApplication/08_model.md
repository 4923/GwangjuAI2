# model

## Migration
> Migrations are **Django's way of Propagating** changes you make to your models (Adding a field, deleting a model, etc)**into your database schema** (document)

1. 변화를 반응하는 방법이다. (Django's way of Propagating)
2. 어디에? **into your database schema**

### 과정
> django에서는 DB에서 변화를 감지하는 과정(1, 2)에 개입을 한다.

0. /models.py
- django의 models.py에서 model 객체를 생성한다.

1. `$ ~makemigrations`
동일하게 DB Schema에 변화를 **감지**
: 000x.auto_2021xx.py

2. `$ ~migrate`
실제 DB에 000x.auto_2021xx.py에 실제로 반영

## HTTP Protocol
반영하기 위해 통신해야한다.

client가 sever에 request
server가 client가 response

이 과정에서 GET과 POST가 어떤 역할을 하는가?
- client가 server에게 **무엇**을 요청하여 server가 client에 **무엇**을 넘겨야 하는지
- GET과 POST는 넘기는 방식이 다르다.

1. GET inquiry
    - Read : 어떤 데이터를 조회하기만 할 때
    - 추가 데이터를 어떻게 보내느냐?
        - 주소의 끝에 key value 쌍으로 값을 넘긴다 : 쿼리데이터
            ```
            https://onion.haus/?param1=value1
            # ?param1=value1
            ```
2. POST inquiry
    - Create, Update : 만들거나, 수정할 때
    - 추가 데이터를 어떻게 보내느냐?
        - post body에 데이터를 싣는다.
        - ex) 게시글을 작성할 때 게시글 내용을 모두 주소에 작성할 수 없음 (보안, 길이제한 등의 이유로)
        - 방법
            1. `views.py`에서 `request.method`를 POST로 지정한다.
                - 이것만 설정하면 올바른 http response가 아니라는 에러가 발생하므로 else문으로 GET방식으로 접근했을 시 반환할 값도 지정한다.
            2. render 함수에 context값을 넣어준다.

