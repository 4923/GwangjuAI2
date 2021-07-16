# Django CRUD의 중요성
우리는 왜 장고를 쓰는걸까? 장고는 C R U D를 아주 잘 만들기로 유명하다.과정이 잘 구현되어 있기에 개발자는 해당 패턴을 쉽게 만들 수 있다.

> CRUD는 Create REad Update Delete다.

### **왜 장고가 CRUD를 잘/쉽게 만들 수 있을까?**  
C R U D에 대응되는 View (MTV에서 View는 Logic임) 를 기본적으로 제공하기 때문이다. 개발자는 이 패턴을 이걸 그냥 가져다쓰면 되니 전반적인 생산성이 향상된다.

### **어떻게 제공하나?**  
- **CBV(Class Based View)**
    - 반대개념 :  FBV (Function Based View)
        - FBV? : 지금까지 만든게 FBV다. instagramlike project에서 구현한 hello_World 함수가 FBV다.

- 굳이 CBV를 써야 하는 이유?
    > 길이를 단축하고 가독성을 높여 생산성을 높이기 위함
    - Account를 만든다고 생각해 보자. 하는 일은 똑같다.
        - Get Data
        - Assign Data
        - Save Data

    그런데 이걸... 30개씩 한다고 하면...? 함수를 30개나 만들어야 한다. 속성이 한 두개가 아니기 때문.   
    그리고 각각 다르게 검증해야 한다고 하면 작업 공수가 늘어난다. django로 만들고 있는건 서버고 서버는 클라이언트를 100% 신뢰하면 안 되기 때문이다. 모든 경우의 수를 적용해줘야 한다.  
    당연히 추가 프로세스도 있을 것이고 그것까지 추가한다면 코드가 너무 길어지고 유지보수도 고통스러워진다.

=> 따라서 복잡도를 제어할 필요가 생긴다. 그래서 이 패턴들을 View에 다 담아두게 된 것이다.

### **View의 패턴을 한번 보자.**

1. Create View?
    - 받고 할당하고 저장하고
2. Read View?
    - 데이터를 키와 함께 받고 읽는다. (뭘 읽을지 알아야 하므로 Key가 필요)
3. Update View
    - Key에 따라 데이터 변경하고 저장하고
4. Delete View
    - 마찬가지로 key에 따라 데이터를 골라 지우고 저장한다.

이렇게 CRUD 라는 라이프 스타일에 대부분의 기능을 담을 수 있다. Django가 편리한 이유다.