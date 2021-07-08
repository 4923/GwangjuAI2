0. 모델 생성
    - 앱폴더의 models.py에서 DB 객체 생성
    - 상속받아온다 (models.Model)

    ```py
    # class name은 camel case로
    class HelloWorld(models.Model):
        text = models.CharField(max_length=250, null=False)
    # text라는 객체에 최대 길이가 250인 문자열을 받는데 빈값은 허용하지 않는다.
    ```
1. `$ python manage.py makemigrations` 
    ```plain
    Migrations for 'accountapp':
    accountapp\migrations\0001_initial.py
        - Create model HelloWorld
    ```
    - DB의 변화사항을 migrations에 0001_initial.py로 저장된다.
2. `$ python manage.py migrate`
    - 생성한건 HelloWorld 객체 하나인데 왜 여러가지가 변경된다고 뜨나? : settings.py에 이미 INSTALLED_APPS 된 객체들이 있는데 그 중 이미 DB를 사용하는 객체가 있을 수 있기 때문
