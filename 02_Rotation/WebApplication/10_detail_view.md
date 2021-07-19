### 어떻게 detail page에 접근할것인가?

> 로그인 한 사용자 : user  == client  
> 로그인 한 사용자의 것으로 추정되는 계정 정보 : account
>> user != account

1. pk 또는 primary key는 db에 데이터를 저장할 때 유일하게 저장되는 값이다. (ex 주민등록번호)
    - 따라서 db에서 정보를 불러올 때 pk라는 이름으로 데이터를 호출할 수 있다. 

2. 로그인한 *user*는 정보를 열람할 수 있게 로그인한 client를 말하며, 본인의 정보를 받기 위해 request를 보낸다.

3. 이 때, user는 자신이 가진 key (account) 를 통해 detail page를 요청하게 되는데, key를 가지고 정보를 가져오는 대상은 *account* 객체다.
    - 요청을 보내는 user와 account 객체는 분리되어있으니 헷갈리면 안된다.

4. detail.html에서도 *account* 객체가 정보를 불러오는데 이 때 해당 객체를 부르는 이름을 views.py에서 지정할 수 있다.
    - project에서는 AccountDetailView class에서 context_object_name으로 지정.
