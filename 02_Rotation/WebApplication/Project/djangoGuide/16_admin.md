# Django administration

1. create superuser
- server 안에서 superuser를 생성한다.
- `python manage.py createsuperuser`
- 비밀번호는 보이지 않을 뿐 제대로 입력된다.
- DB에서 계정 관련 테이블 auth_user 에서 확인할 수 있다.
    - is_superuser. is_staff가 True인 1로 지정되어 있음을 볼 수 있다.
    ```
    Username (leave blank to use 'ek'): admin
    Email address: _____@likelion.org
    Password: 
    Password (again):
    Superuser created successfully.
    (base) 
    ```
2. http://127.0.0.1:8000/admin 에서 관리자 계정 접근 가능