# [AI Nation](https://www.aination.kr) DT Seminar : AI
21-06-29 최광철 실장님

### 컴퓨터와 뇌
- 컴퓨터 vs 뇌
    - 컴퓨터 : 입력 -> 프로그램 - > 출력
    - 뇌 : 입력 -> 신경망 연결 (점화패턴) -> 출력
- 뇌의 지능 구현 방법 : 입력 데이터에 대하여 예측 데이터를 구하는 미리 정해진 규칙을 컴퓨터가 단계를 나누어 순서대로 계산하여 결과 생성
- Rule-based Program : 사람의 지능을 흉내
    - 암기, 계산, 체스, 퀴즈까지
- Neural Network : 사람 두뇌의 작동방식을 프로그램으로 구현
    - Rule-based Program이 할 수 있는 일부터 예술까지

### 기업의 AI 혁신 기대효과
- 일반 기업 관점에서의 협업 : 예측 -> 결정 -> 행동 -> Feedback -> 학습
- 범용 AI와 산업 AI
    1. 범용 AI (Horiozntal AI) : 여러 AI 응용 분야에 보편적으로 활용되는 공통 기술 소프트웨어
        - B2C
        - 기업들이 초점을 맞추고 있는 부분
        - 이미지인식 AI, 자연어처리 AI, 음성인식 AI, 예측 AI
    2. 산업 AI (Vertical AI) : 범용 AI를 일부 활용하여 특정 용도로 개발된 딥러닝 응용 소프트 웨어
        - B2B
        - 스타트업에서 잘 하는 영역
        - TODO : industry domain knowledge

- [CBInsights | AI top 100](https://research-assets.cbinsights.com/2021/05/03185016/AI-100-export-min.png)

- 인터넷은 선점하는 기업이 독식하는 To Customer 구조라면 Industrial AI는 도메인 지식이 승패를 가르는 To Business 구조다.
    - 도메인 지식? 
        - [1_일반](https://subokim.wordpress.com/2013/03/31/technical-domain-knowledge/)
        - [2_데이터분석](https://medium.com/@unfinishedgod/%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D%EC%97%90-%EC%9E%88%EC%96%B4%EC%84%9C-%EB%8F%84%EB%A9%94%EC%9D%B8-%EC%A7%80%EC%8B%9D%EC%97%90-%EA%B4%80%ED%95%98%EC%97%AC-fe57cedde91d)
        - [3_개발](http://junil-hwang.com/blog/%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%84%A4%EC%9D%B4%ED%8B%B0%EB%B8%8C/)
- AI 경제에서 원유는 데이터다.


### 인터넷 분야의 AI 활용
- 플랫폼 허브 경제
    - 인터넷은 데이터가 많으므로 딥러닝을 자주 활용한다. 
    - 3대 요소 : Machine (AI), Platform, Crowd
        - 선순환 : 사용자가 더 많아지면 더 많은 데이터가 모이고 인공지능이 발전하며 더 좋은 제품을 만들어낼 수 있고 이는 더 많은 사용자를 끌어모은다.
- 금융 (AI First 금융기업, Ant Financial)
- 게임산업, 의료산업에서 사용되고 있다.

### 전통산업 분야의 AI활용
이전에는 규모가 중요했다면 이제는 속도가 중요해졌다.
> In the new world, it is not the big fish which eats the small fish, it's the fast fish which eats the slow fish. 
> Klaus Schwab. Favorite. 

- 제조업 AI
    - 스마트 제품 : 제품 OS, 로봇, 자율 주행차
    - 스마트 팩토리  : 자율운영, 생산최적화, 공정최적화, 예지보전, 디자인자동화
        - NIKE와 BMW가 인도네시아에 완전 자동화 공장을 만들었을 때 오히려 생산성이 떨어지는 현상 관측 -> 소수의 사람이 자동화 공장을 관리하는 체제 확립

- 소매업 AI
    - 수요 예측, 고객 서비스, 개인화 판매, 옴니채널, 물류, 무인매장
    - SEPHORA, amazon CO 등

- AI 물류 플랫폼 : 쿠팡에서 준비중이라고... 
- 교육 AI : 학습관리, 맞춤 학습, 평가, AI 튜터, 학사관리, 진로지도 등을 인공지능으로 관리. 몰입정도를 확인한다.

- 스마트 시티 : 싱가포르에서 주로 진행. 도시계획, 헬스케어, 에너지관리, 교통, 치안 등을 인공지능으로 관리한다.  
    - FEMS (공장에너지관리시스템) : [ex](http://www.idif.co.kr/solution/ems/) 전기 등의 에너지를 관리한다. 한국은 초기단계

### AI에 의한 미래 일자리 변화
- VUCA
    - 변동성 V
    - 불확실성 U
    - 복잡성 C
    - 모호함 A

- 인간과 AI 협업의 필요성 대두되고 있음.
    - Cobots Transforming Work and Learning
        - Work quality
        - Agile learning
        - Promising future

- 인간과 AI의 강점 비교
    - 인간 : 결정, 협업, 창조
    - AI : 예측, 기억, 실행


### 설명가능한 인공지능 XAI
- DARPA (Defense Advanced Research Projects Agency) 에서 제시
- 딥러닝의 블랙박스 문제를 해결하기 위해 머신러닝 방식을 함께 하며 원인을 추적한다.
- [Science On | 설명 가능한 인공지능(eXplainable AI, XAI) 동향](https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=KOSEN000000000001071)

### 딥러닝의 응용분야
1. Vision : up to 60%
2. Language
3. Audio    

### 신경계 척도 분석
눈/입 움직임을 이용해 신경계 척도를 진단한다. Glasgow Coma Scale을 기반으로 한다.
해당 이론은 이전까진 정성적으로 평가되었으나 인공지능이 도입되며 정량적으로 평가할 수 있게 되었다.

