# Introduction of Web Application

### 왜 WEB인가?
서비스를 제공하는 방법은 WEB이다. 

### 개요
1. 무엇을 사용할 것인가? : Django Web Framework
2. 무엇을 할 것인가? : Pinterest 디자인을 본따 커뮤니티 제작
3. 무엇을 배울 것인가?
    1. Django부터 (개발)
        - 카드형 레이아웃
        - 반응형 디자인 : 기기의 크기에 상관없이 어떤 환경 (웹, 모바일, 태블릿 등)에서든 사용할 수 있게 한다.
        - 계정 시스템
        - 게시판 시스템
        - 구독 시스템
        - 좋아요 시스템
        - ...
    2. Docker까지 (배포)
4. 진행방식 : 라이브 코딩으로 함께 개발하고, 혼자서 프로젝트를 따로 진행한다.

### HOW?
- Front-End : html, css, js
- Back-End
    - MariaDB (DB)
    - NGiNX (Server)
    - **Django (Web Framework)**
    - **Docker (Deploy)**

### RoadMap
1. Django : 각각의 기능을 APP으로 분리하고 하나의 프로젝트로 엮는다.
2. 1에서 만든 Django Container를 Docker에 적용한다.
3. 2에서 적용한 Docker, DB, Server, Django container를 AWS를 통해 배포한다.

