# Secret Key 분리

1. 최상위 폴더에 `.env` 파일 생성
2. settings.py 에서 SECRET_KEY = "~~" 생성
    - 이 때 **띄어쓰기나 따옴표는 삭제**한다.
3. 원본 settings.py에서 `.env`의 `SECRET_KEY`를 읽어오는 작업
    ```python
    import os       # for local_env

    # BASE_DIR = Path(__file__).resolve().parent.parent
    # Path(__file__) : settings.py가 있는 경로
    # parent.parent : 해당 경로의 부모 경로를 두개 찾겠다.  
        # settings.py의 parent : 앱폴더
        # 앱폴더의 parent : project 폴더

    # BASE_DIR 하단에 작성 : 불러오기
    env_list = {}
    local_env = open(os.path.join(BASE_DIR, '.env'))    # load contents of .env file

    # 읽기
    while True:
        line = local_env.readline()     # read contents of .env file by line
        if not line: break              # break condition
        line = line.replace('\n', '')   # 보이지 않는 줄개행 문자를 지우는 작업 (readline()을 사용하게 되면 줄개행 문자도 함께 읽어들이게 됨)
        start = line.find('=')          # key, value는 '='을 기준으로 나눈다.
        key = line[:start] 
        value = line[start+1:]
        env_list[key] = value           # env_list는 dictionary type이므로 key, value를 할당
    ```

    - overflow에서는 environ을 사용했는데, 해당 모듈에서는 `.read_env` 를 사용할 수 있는 것 같다.
    - `os.path.join`
        - `os`란?
            - 운영체제의 기능을 사용할 수 있게 하는 모듈
            - `os.path`는 운영체제 안의 경로를 말한다.
            - `os.path`에 base dir를 합쳐서 돌려준다.
4. .gitignore에 `.env` 추가