# CSS Cheatsheet

> CSS 태그를 정리한다.


### 길이 단위
- [w3schools](https://www.w3schools.com/cssref/css_units.asp)
- 기준에 따라
    1. 상대적 크기
        - `em`
            - 상위 요소 크기를 기준으로 삼는다. 기준이 되는 요소가 매번 달라진다.
            - ex) 2em : 바로 상위 요소의 크기보다 2배 큰 크기
        - `rem`
            - html 요소 크기를 기준으로 몇 배인지를 결정한다.
            - html 요소 크기의 기본 값은 보통 16px이다.
            - ex) 2rem: 기본값이 16px으로 그대로라고 할 때 16/2px == 32px
    2. 절대적 크기
        - `px`