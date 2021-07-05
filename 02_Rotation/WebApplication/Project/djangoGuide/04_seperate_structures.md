# 페이지 구역 분리 : django template languages (extends, include)

0. div로 공간 분리
    ```html
    <!-- height : 높이 -->
    <!-- borer-radius : 원래 html 태그를 만들면 기본 모서리 형태가 직각이다. 모서리를 둥글게 해주는 속성이 border-radius -->
    <div style = "height : 20 rem; background-color:lgithslategrey; margin: 2rem; border-radius: 1rem;">    <!-- header -->
    <div style = "height : 40 rem; background-color:lgithslategrey; margin: 2rem; border-radius: 1rem;">    <!-- contents -->
    <div style = "height : 20 rem; background-color:lgithslategrey; margin: 2rem; border-radius: 1rem;">    <!-- footer -->
    ```

    <center>
    <img src=img/div.png width = 500 alt = "구역 분리 (div)">
    </center>

1. include :  header, footer 분리
    project/templates에 header, footer html 생성

2. include : head, footer 분리
    ```html
    <!--base.html-->
    {% include 'header.html% %}
    <div style = "height : 40 rem; background-color:lgithslategrey; margin: 2rem; border-radius: 1rem;">    <!-- contents -->
    {% include 'footer.html' %}
    ```

    3. exclude : contents 처리, accountapp/views.py에서 base.html을 만들었으므로 accountapp 만의 templates를 저장할 수 있는 template 폴더(`accountapp/templates/`)를 생성한다. accountapp의 template은 accountapp/templates에서 관리한다. (경로를 분리하기 위해)
        1. accountapp/templates 폴더 생성
        2. 1의 하위 위치에 accountapp 폴더 생성 (`accountapp/templates/accountapp`)
        3. 2 안에 html 생성 (`accountapp/templates/accountapp/hello_world.html`)
        4. hello_world.html에서 extends 구문으로 base.html을 불러온다.
        5. 무엇을 바꿔야 하는지 모르므로 구역을 설정해주고, 구역 안의 구간만 변경할 수 있도록 base.html에 구역을 지정한다. 
            ```html
            {% block content %}
            {% endblock %}
            ```
        <center>
        <img src=img/seperate_structures.png width = 500 alt = "contents 분리 완료">
        </center>

4. views.py에서 다시 뼈대였던 base.html을 가져오는게 아니라 accountapp/templates/accountapp/hello_world.html 을 불러오도록 view 파일을 변경한다.