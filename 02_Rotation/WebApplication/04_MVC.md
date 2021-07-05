## MVC & Django : MTV
> Web Framework인 Django는 MVC패턴을 기반으로 한 MTV 패턴을 따른다.

<center>

|MVC|MTV|
|-|-|
|Model|Model|
|View|Template|
|Controller|View|

</center>

### MVC?
> 모델-뷰-컨트롤러(model–view–controller, MVC)는 소프트웨어 공학에서 사용되는 소프트웨어 디자인 패턴이다. 이 패턴을 성공적으로 사용하면, 사용자 인터페이스로부터 비즈니스 로직을 분리하여 애플리케이션의 시각적 요소나 그 이면에서 실행되는 비즈니스 로직을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있다. [(wiki)](https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%8D%B8-%EB%B7%B0-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC)

- **소프트웨어 디자인 패턴?** : 당연히 UIUX와는 관계가 없다. [소프트웨어를 설계할 때 특정 맥락에서 자주 발생하는 고질적인 문제들이 또 발생했을 때 재사용할 수 있는 해결책](https://gmlwjd9405.github.io/2018/07/06/design-pattern.html)으로, 프로젝트를 효율적으로 개발 및 관리하기 위해 사용하는 일종의 템플릿, 형식이다.
- **MVC** : 개발에 필요한 부분을 Model, View, Controller 세가지 요소로 나누어 개발하는 방법이다. 복잡한 파일들을 폴더에 나누어 정리하는 방법과 비슷하다고 이해했다. MVC에서의 분류 기준은 '기능'이라는 것이 중요하다.


- Model, View, Controller [(참고)](https://medium.com/@jang.wangsu/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4-mvc-%ED%8C%A8%ED%84%B4%EC%9D%B4%EB%9E%80-1d74fac6e256)
    1. Model : **무엇을** 보여줄 것인가?
        - DB에 접근할 필요 없이 데이터에 접근
        - 데이터 구조를 나타낸다. DB와 상호작용하며 행(row), 열(column) 형태로 저장된 item, attributes를 불러오는 역할을 담당한다.
    2. View : **어떤 파일을** 보여줄 것인가?
        - user의 모든 요청을 처리하고 처리된 결과를 user에게 되돌려준다.
        - 눈으로 보이는 부분을 담당한다. HTML, CSS, JS 파일이 포함된다.
        - Controller에 종속되어 Model에서 결정한 것을 시각화한다.
    3. Controller : **어떻게** 보여줄 것인가?
        - Model에서 선택된 데이터를 어떻게 View로 넘겨줄 것인지 결정하는 로직 처리 구간이다.
        - request (user to server)와 rendering (server to user), response도 이 구간에서 담당한다.


### MTV / MVT
MTV 또는 MVT로 부르지만 본 문서에서는 기능별로 열을 맞춘 MTV로 용어를 통일하겠다.  
Django는 Model, Template, View로 구성된 소프트웨어 디자인 패턴을 사용하며, 이 때 Template는 MVC의 View를, View는 MVC의 Controller를 담당한다.  
View라는 용어가 동일해서 헷갈릴 수 있으나 Template 이 조금 더 시각적인 느낌에 가깝다는 생각을 하면 적응하기 쉽다. (ppt template 등)  

- [django template의 특징 : template language](https://github.com/4923/GwangjuAI2/blob/master/02_Rotation/WebApplication/Project/djangoGuide/06_template_language.md)