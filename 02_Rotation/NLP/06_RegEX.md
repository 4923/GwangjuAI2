> 필요할 때마다 꺼내보기 위한 정규표현식 정리

### 파싱 parsing
- 어떤 문서에서 **원하는 데이터**를 특정 패턴이나 순서로 **추출**하여 정보를 **가공**하는 과정
- 보통 웹 문서 (HTML, JSON, XML) 를 requests, beautiful soup, selenium 등으로 파싱하여 string 형태로 남긴다.
    - Lateral Thinking! 하나하나 접근하지 말고 (스크레이핑) 범용적으로 사용할 수 있는 코드를 짜자

# REGular EXpression

> 왜 "정규" 표현식인가?

일반적인 (regular) 패턴을 *Meta문자를 통해 문장 (expression) 으로 표현한 것이 정규표현식이다.
- *Meta문자 : 정규표현식에서 사용하는 문자, 정규표현식의 알파벳

![python regex cheatsheet](https://t1.daumcdn.net/tistoryfile/fs13/31_tistory_2009_07_02_13_58_4a4c3e88c279f?x-content-disposition=inline)
<p align=center>Python RegExp cheatsheet</p>

<br>

![regular expression e-mail matching example](https://www.computerhope.com/jargon/r/regular-expression.gif)
<p align=center>Email matching example</p>



### 참고 
- [정규표현식 (Regex) 정리](https://hamait.tistory.com/342)
- [정규 표현식(RegEx)을 이해 해보자!](https://justkode.kr/data-science/regex-1)