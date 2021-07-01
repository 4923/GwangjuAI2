# Secret Key 분리

1. 최상위 폴더에 `.env` 파일 생성
2. settings.py 에서 SECRET_KEY = "~~" 생성
3. 원본 settings.py에서 .env의 SECRET_KEY를 읽어오는 작업
    ```python
    import os       # for local_env

    # BASE_DIR = Path(__file__).resolve().parent.parent
    # Path(__file__) : settings.py가 있는 경로
    # parent.parent : 해당 경로의 부모 경로를 두개 찾겠다.  
        # settings.py의 parent : 앱폴더
        # 앱폴더의 parent : project 폴더

    # BASE_DIR 하단에 작성 : 불러오기
    env_list = {}
    local_env = open(os.path.join(BASE_DIR, '.env'))    # import os

    # 읽기
    while True:
        line = local_env.readline()
        if not line: break
        line = line.replace('\n' , '')
        start = line.find("=")  # "=" 이라는 대입 연산자를 기준으로 왼쪽을 key, 오른쪽을 value로 지정
        key = line[:start]
        value = line[start+1:]
        env_list[key] = value
    ```

    - overflow에서는 environ을 사용했는데, 해당 모듈에서는 `.read_env` 를 사용할 수 있는 것 같다.
    - `os.path.join`
        - `os`란?
            - 운영체제의 기능을 사용할 수 있게 하는 모듈
            - `os.path`는 운영체제 안의 경로를 말한다.
            - `os.path`에 base dir를 합쳐서 돌려준다.
4. .gitignore에 `.env` 추가