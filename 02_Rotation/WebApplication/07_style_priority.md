# 스타일 객체의 우선순위

CSS의 스타일 태그는 다음 세 종류로 나뉜다.

1. inline style
    - <div style="~">
2. internal style sheet
    - base.css
3. external style sheet
    - 외부에서 불러온 google font 등

우선순위는 inline > internal > external 순서다.



<details>
<summary>순서가 달라지는 이유</summary>
렌더링엔진이 가장 먼저 읽어들이는 문서는 HTML문서로 CSS파일의 우선순위는 그 다음이다.

원칙적으로 css를 포함한 스타일 시트는 DOM트리를 변경하지 않는 '규칙'이다. HTML 안의 스타일 (inline) 은 처음 해석될 때 html로 읽히기 때문에 가장 먼저 렌더링되고 internal 인 스타일 시트는 html 문서가 요구하는 바에 따라 불러와진다. external은 외부 소스이므로 기본적인 처리가 완료된 후에 덧씌워진다.  

<li><a href="https://d2.naver.com/helloworld/59361">Naver D2 : "브라우저는 어떻게 동작하는가?"</a></li>
</details>


display attribute

block : 부모 크기를 전부 가져간다.

inline : 글자크기

inline : 원하는대로 높이 넓이 나눌 수 있다.