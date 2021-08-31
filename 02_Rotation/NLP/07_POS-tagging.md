## POS tagging - 무엇인가?
- 문장으로부터 품사 Part-of-Speech 를 파싱한다.
- 품사란? : 품사의 정의는 Penn Tree bank를 기반으로 한다. (모르겠을 때 확인 할 것)
- 품사 태깅이란
    1. 토큰화 된 문장의 토큰에 Penn Tree bank에서 구분한 태그를 알맞게 일대일 대응 시키는 과정이다. 
    2. 문맥이 다양하므로 규칙보다는 **확률**로 접근하는 편이 좋다.
    3. 어떤 확률? : 단어와 태그 사이의 모든 관계를 고려할 수 있는 **결합 확률 joint probability**
        - 결합 확률은 연쇄 규칙 chain rule로 분해된다. (조건부확률과 확률의 곱)
    4. 이러저러해서 조건부 확률을 구하는 것이 최종 과제로 남는다.
    5. 경우의 수가 굉장히 많으므로 공학적으로 접근 : 근사적으로 푼다.
        - 베이즈 정리
        - 마르코프 연쇄
        - 독립


## POS tagging - 방법론
1. 규칙기반 / rule-based
    - e.g. nltk의 pos tagger
    - 오류가 많다.
2. 예측기반 / Deep Learning or Hidden markov Model
    - 맥락을 읽는다! (동음이의어 구분 가능!)
    - e.g. SpaCy의 pos tagger (Deep Learning)
    - Markov는 데이터가 많이 필요하지 않다는 장점이 있다.
    - 더 효과적인 모델은 딥러닝 모델

## Hidden Markov Model; HMM, 은닉 마르코프 모델
![markov model diagram](https://bygritmind.files.wordpress.com/2020/08/image-5.png?w=1024)
**바로 직전에만 영향을 받는 시퀀스 데이터의 확률**을 계산한다. 증명은 따로 주피터에 정리해야 할 듯


### 참고
[Hidden Markov 모델 (feat. 품사태깅)](https://gritmind.blog/2020/07/14/hidden-markov-model-pos/)

