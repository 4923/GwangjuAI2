# Teachable machine Deploy (with Netlify)

0. 프로젝트 폴더를 만든다.
1. model을 다운로드 받고, 폴더이름을 `my_model`로 변경한다.
2. `my_model`이 위치한 폴더에 `index.html`을 생성한다.
3. `index.html`에 '모델에서 사용할 코드 스니펫' 이라고 적힌 `js` 코드를 입력한다.
    - 로컬서버를 돌리면 'Teachable Machine Image Model' 이라는 글씨와 함께 start버튼이 생성된 것을 확인할 수 있다. 이 상태에서는 모델이 동작하지 않는다.
4. Netlify에 배포한다. 배포 과정은 학교멋사에서 제작한 강의자료로 대신한다. 
    - 나만의 웹 사이트 배포하기 : [notion](https://www.notion.so/4923i/d15d6c2a42704f4796354d5f27afa818), [velog](https://velog.io/@hufsglobal09/Session-4-Deploy)
5. [완성된 배포 페이지](https://teachable-machine-mask.netlify.app)

---
<br>

<details>
<summary>확인 필요</summary>
- https가 붙어야 모델을 사용할 수 있음
    - 왜? js라 그렇다고 하는데 모르겠음... native tf는 cpu를 엔진으로 사용하는것으로 아는데 tf.js는 뭔가 다른건가? 아니면 표현 방법만 다른건가? 배포해야만 볼수 있다면... 모델은 이미 있고 볼 수 있는 방법만 다르다는건가?
</details>