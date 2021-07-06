# Design
> bootstrap과 google font를 활용한다.
> 현대 사회에서 디자인은 상품/서비스의 모든 것

### 카테고리 만들기
1. 제목 생성
    1. header를 div 태그를 이중으로 두개 생성
        - 위 div 태그에는 이름
        - 아래 태그에는 메뉴 (span으로 nav 4개)

    2. 중앙정렬
        - 개발자도구 f12에서 요소 별 코드 확인하고 변경사항 테스트 할 수 있다.  
            <img alt="변경사항 테스트" src=img/element_style_test.png>
        - 최상위 태그에 css의 `text-align=center;`를 적용한다.
    
    3. 같은 과정을 footer에도 적용한다.

### bootstrap
1. bootstrap?
    - twitter가 발표한 front-end library 
    - css를 일일이 만지지 않아도, class만 지정하면 디자인을 사용할 수 있다.
    - 버튼, 알림 팝업, 카드 레이아웃, 내비게이션 바 등 다양한 **디자인 요소**들을 긁어올 수 있다.
    - 소스를 사용하여 페이지 디자인을 개선시킬 수 있다.

2. 적용방법
    1. bootstrap 검색
        - 공식페이지 [link](https://getbootstrap.com)
        - 공식문서 [documnets](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    2. 공식 문서의 css 복사
        ```css
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        ```
    3. 프로젝트에 적용
        - 외부 소스를 가져오는 위치는 head이므로 head에 불러온다.
            ```html
            <!-- templates/head.html -->
            <head>
                <meta charset="UTF-8">
                <meta name="viewport"
                    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Document</title>

                {% comment %} bootstrap link {% endcomment %}
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
                    rel="stylesheet"
                    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
                    crossorigin="anonymous">
            </head>
            ```
    4. 변경사항 확인
        - 레이아웃이 소소하게 변경되었다.
            <table>
            <tr>
                <td><img alt="적용 전" src=img/footer_header_style_applied.png></td>
                <td><img alt="적용 후" src=img/bootstrap_1.png witdh=400px></td>
            <tr>
            </table>


### [Google Font](https://fonts.google.com)

1. google font 에서 코드를 복사해온다.
    - type something에 원하는 문구를 작성하면 공개된 폰트로 작성된 문구를 확인할 수 있다.
    - 이 때 License를 잘 확인 할 것
    - 원하는 타입에서 Select this style을 누르면 link를 복사할 수 있게 된다.
2. `head.html`에 `class` 추가
    - ```html
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Merienda&display=swap" rel="stylesheet">
        ```
    - 왜 폰트가 여러개인가? : 첫번째 폰트가 열리지 않을 경우 다음 순위의 폰트를 출력하기 위해

3. 원하는 위치의 div에서 `font-family:` 속성 추가. 보통 css rules라는 항목으로 google font 하단에 적혀있다.
    - ```html
        font-family: 'Merienda', cursive;
        ```

4. 완성  
    <img alt="apply font" src=img/apply_font.png>