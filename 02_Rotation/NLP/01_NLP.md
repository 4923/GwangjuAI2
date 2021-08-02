# NLP

> NLP refers to a set of techniques to understand text (i.x. natural language) for the sake of solving real world task

## 목표
1. 단어나 문서의 의미를 나타낼 수 있는 "표현"을 찾는다.
2. "표현"은 기호, 벡터, 이미지를 포함한 무엇이든 될 수 있다.
3. "표현"의 의미를 조금이라도 구체화 하는것이 목표다.
    - 이런 구체화 과정이 하나의 논문이 되기도 한다.
    - BERT
        - Google에서 발표한 언어 이해 알고리즘 (Open Source Software)
        - 방대한 양의 Corpus(위키피디아, 책 등)를 pre-training한 결과다.
            - Corpus : 말뭉치, 대량의 텍스트 데이터
        - 즉, BERT는 사전훈련을 통해 가장 유용한 표현을 찾는 방법이다.

## 방법 (1) : One Hot Vector / One Hot Encoding

> 각 단어가 가지는 고유 index를 기준으로 단어의 의미를 표현

- 분류에서 가장 간단하게 사용할 수 있는 방법이나 단어의 의미가 담겨있지 않기 때문에 **유사도를 정량적으로 구할 수 없다.** 
- one hot vector는 직교하므로 유사도라는 개념이 없다.
- 또한 단어의 종류가 많아질수록 0의 개수가 커져 행렬이 희소해진다.
    - 희소행렬 Sparse Matrix
        - 값이 대부분 0으로 이루어진 행렬.
        - 데이터가 공간에 밀집되지 않고 넓게 분산된 표현방식이다.
        - 반) 밀집 행렬 Dense Matrix
        - 야기하는 문제
            1. 불필요한 0으로 인한 메모리 낭비
            2. 행렬의 크기로 인한 연산 시간 증가
            => 같은 메모리를 가지고 담을 수 있는 의미의 양이 적어진다.
            - 해결 : 예측 기반 접근방법 (rule-based XXX)


## 방법 (2) : Distributional semantics
> 벡터에 단어의 의미를 담는 방법  

**단어의 의미는 문장 곳곳에 분배되어 있다**
 
NLP의 기본 가정 중 하나인 distributional hypothesis (비슷한 맥락에 등장하는 단어들은 유사한 의미를 지니는 경향이 있다.)와 관계가 있다.

1. Count-based
    - 말뭉치 corpus로부터 DTM (Document Term MAtrix)을 구축하여 단어벡터, 문서 벡터를 추출한다.
        - DTM : 유사도를 정량적으로 측정할 수 있다.
            - 코사인 유사도?
    
2. Prediction-based (Language Models, 예측 기반의 모델을 통틀어 '언어모델'이라고 한다.)
    - 모델이 단어의 의미를 스스로 학습하여 벡터에 담도록 하자.
    - 최근의 흐름 
    - 목적 : Dense Vector
    - 목표 : $P(next|context)$ 를 최대화 하는 방향으로 딥러닝 모델의 가중치 최적화
        - 맥락이 주어졌을 때 맥락 다음의 단어가 올 조건부 확률
    - 예시 : GPT3, BERT, Word2Vec
        - GPT3 : 코드 자동완성 서비스의 기반 모델 (Github Copilot)
            - $P(next|context=past)$
        - BERT : 미래의 맥락까지 고려한다.
            - $P(next|context=past & future)$
        - GPT3 vs BERT
            - GPT3 : a robot must (exterminate? obey?)
            - BERT : a robot must () *human*