# Model : DB

1. 사전 준비 : 사용자의 입력값을 POST로 보내고 그 값을 빼와 출력하는 방법
    - hello_world.html

    - views.py

2. DB에서 빼오기
    - new_hello_world 라는 새로운 객체를 만든다.
    - new_hello_world = HelloWorld()    # accountapp/models에 입력한 값

3. settings.py 보면 DATABASES 라는 값이 보인다. 기본적으로 엔진과 이름이 저장된다.
    - base_dir에 db 파일을 만들라는 명령 있음 (name에서 위치와 이름 지정)
    - hello_world.html 에서 models.py의 HelloWorld() 클래스를 호출하여 객체 생성 : new_hello_world
    - 1에서 만든 temp를 new_hello_world의 text에 할당
    - 갱신된 new_hello_world를 `.save()`

4. db.sqlite3 을 확인하면 db에 직접적으로 쿼리 명령어를 사용하지 않아도 새 행이 추가된 것을 확인 할 수 있음

5. db에 저장된 내용을 모두 읽어오는 list 생성 (in views.py)
    - 어떻게 가져오는가? : models.py/HelloWorld() class를 통해 접근 가능
    - objects로 접근한다. : 쿼리 가능해짐 (메소드 다양하니 확인 할 것)
        - 모든 데이터를 가져오는 쿼리 : all

    - hello_world_list = HelloWorld.objects.all()

    - context에 hello_world_list를 넘기기 위해 context 값 변경
        - hello_world_list의 key를 가진 hello_world_list의 객체를 넘긴다.
            - context={"hello_world_list": hello_world_list},
    
    - template도 변형
        - 여러개를 동시에 돌려야 하므로 템플릿 언어의 for문 사용

    - get 방식의 출력도 변경
        - 처음 주소창에 접근했을 때에도 db를 모두 확인할 수 있도록 변경
        - views.py/else 문에서 objects.all()로 객체를 불러오고 key와 valule 모두 hello_world_list로 변경하여 템플릿에서 for를 돌 수 있도록 한다.

6. 새로고침? : Redirect
    - **마지막에 보낸 작업**을 다시 보내는 것
    - 마지막에 보낸 데이터가 POST일 때 (Create Data) POST를 반복하게 된다.
    - 따라서 마지막 요청을 POST가 아닌 다른것으로 바꿀 필요가 있다 : redirect
        - 새로운 데이터를 생성하지 않도록 유도하기 위해 GET을 마지막 요청으로 바꾼다. (되돌린다.)

    - 주소를 일일이 칠 필요 없이 app name을 설정하고 views.py 에서 HttpResponseRedirect(위치) 를 설정한다.
        - appname : urls.py에서 지정
        - return HttpResponseRedirect
    - 원래 주소를 입력해야하는데 저 주소를 역추적해서 찾아가는 함수를 만들어야 한다. (reverse method)
        - 어떤 위치에서 어떤 앱으로 갈지 지정
        - return HttpResponseRedirect(reverse('accountapp:hello_world'))
    - 이제 다시 새로고침해도 반복된 결과가 전송된다는 경고창이 뜨지 않는다.