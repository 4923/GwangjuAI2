## Word Embedding
> 구축하고 기반을 둔다는 뜻인 Embedding을 사용하는 Word Embedding은 단어의 의미를 단어를 표현한 벡터에 두는 기법이다. 

### vs One-Hot Vector
|구분| One-Hot Vector |	임베딩 벡터 |
|:-:|:-:|:-:|
|차원 |	고차원(단어 집합의 크기)  |	저차원  |
|다른 표현|	희소 벡터의 일종  |	밀집 벡터의 일종 |
|표현 방법|	수동(index)	| 훈련 데이터로부터 학습함 |
|값의 타입|	1과 0	| 실수 |

- One-Hot Vector는 각 단어간 유사성을 표현할 수 없다는 한계가 있었다.
    - 단어의 **인덱스**만 표현하기 때문
    - 희소 표현 sparse representation (0과 1로 표현하기 때문)
- One-Hot Vector의 한계를 해결하기 위해 단어 사이의 유사도를 벡터화하는 방법을 고안했는데 이를 **분산표현**이라고 한다.

### Embedding Vector
- 분산표현 distributed representation
    - 단어 사이의 **유사도**를 다차원 공간에 벡터화 -> 단어의 **의미**를 담는다.
    - 유사도와 의미가 무슨상관인가?
        - 분산 표현은 분포 가설을 기반으로 하는데, 분포 가설은 "비슷한 위치에서 등장하는 단어들은 비슷한 의미를 가진다" 는 가설이다. 특정 단어의 위치에 유의어를 입력해도 문장 전체의 의미는 달라지지 않기 때문이다.
            - e.g. 강아지는 귀엽다 / 강아지는 사랑스럽다 / 강아지는 깜찍하다 에서 귀엽다, 사랑스럽다, 깜찍하다는 의미적으로 유사하다고 말할 수 있다.
    - 이렇게 **분산 표현**으로 표현된 벡터를 **임베딩 벡터 Embedding Vector** 라고 한다.
    - 그 차원이 상대적으로 낮으므로 밀집 벡터 dense vector 라고 할 수도 있다.


## Language Model : 무엇인가?
> 언어모델은 규칙을 스스로 만든다!  
- Count-based model의 문제인 희소행렬의 문제를 해결하기 위해 벡터에 의미를 담는 과정을 모델에 맡긴다. 
    - 장점 : dense한 vector 생성 가능
    - 단점 : 해석이 불가능함
- 비유하자면 : 제대로 답하지 않은, 원하는 문항만 답변한 성격유형검사 결과가 DTM이었다면 Language Model의 Embedding Vector는 대상들을 관찰하고 의미를 담은 (기준은 알 수 없음) 결과 보고서. 무엇으로 채워져있든 일단 어지간한 항목은 다 채워져있다.
    - 추정 : 비슷한 맥락에서 쓰이는 단어는 각 차원의 값이 유사하다 : 단어의 유사성 파악 가능
- 현재 쓰는 예측기반 모델은 차원 개수가 천개까지 간다. (그래도 dense하다.)

    
## Word2Vec
> 1. CBOW, Skip-Gram 두 가지 방식이 있다. (모두 양방향이다!)  
> 2. Word2Vec에서 입력은! 반드시 One-Hot Vector! 이어야 한다!  
> 3. P(context|pivot) 을 최대화 하는 것이 목표다

### 무엇인가?
언어 모델의 일종으로 비유문제를 풀 수 있다. 자연어처리의 전제 중 하나인 <u>**Distributional Semantics**</u> 를 따르며 비슷한 단어의 벡터표현이 유사하다는데 착안한다.

### 용어
- window : 한 번에 몇 개의 단어를 볼 것인가?
- sliding (window) : 집중하는 단어인 window를 한 칸씩 이동하는 방법; 주변 단어와 중심 단어를 바꿔가며 학습을 위한 데이터 셋을 만든다.
- center word : 중간단어
- context word : 주변단어
- pivot word : 중심이 되는 단어, 보통 output이 해당하며 CBOW냐 Skip-Gram이냐에 따라 달라진다.

### CBOW (Contiinuous Bag of Words)
- BoW에서 발전된 방식
- 맥락으로 단어를 예측 : 주변의 단어를 가지고 **중간의 단어 center word**를 예측


1. idea of CBOW: One-Hot Vector를 input layer에 할당

    |도식화|매커니즘|
    |:-:|:-:|
    |![ANN](https://wikidocs.net/images/page/22660/word2vec_renew_1.PNG)|![layer](https://wikidocs.net/images/page/22660/word2vec_renew_2.PNG)|
    - 은닉층이 하나이므로 DNN이 아니라 Shallow Neural Network 얕은 신경망이다.
    - Word2Vec의 은닉층은 독특하게 활성화 함수가 없고, **lookup table**이라는 연산을 담당하는 층이므로 특별히 이름을 붙여 부른다; projection layer, 투사층
    - M : 임베딩 벡터의 차원
    - V : 단어 집합의 크기
    - 학습 전 W와 W'는 작은 랜덤 값

2. i번째 단어의 One-Hot Vector에 (초기: 랜덤값) 가중치 행렬의 i번째 행을 곱해 lookup
3. projection layer에서 lookup한 결과가 모여 평균을 낸다.

    |lookup table|훈련|
    |:-:|:-:|
    |![lookup](https://wikidocs.net/images/page/22660/word2vec_renew_3.PNG)|![train](https://wikidocs.net/images/page/22660/word2vec_renew_4.PNG)|

    - lookup table? : i번째 인덱스가 1인 One-Hot Vector ($x$) 에 가중치 $W_{W * M}$ 행렬을 곱하는 과정은 W행렬의 i행을 그대로 읽어오는 (*lookup*) 과정과 동일
        - 일반적인 행렬과 벡터의 곱
        - W의 i번째 행벡터 == Word2Vec를 수행한 후 i번째 단어에서 M차원의 크기를 갖는 임베딩 백터
    - 이 때 Projection Layer : **주변 단어의 One-Hot Vector에 가중치를 곱해 생긴 벡터들이 만나는 장소**로, 가중치를 곱해 생긴 벡터들의 **평균**을 구한다.

4. 손실함수 cross entropy 적용하여 score vector (output) 생성

    ![cross entropy](https://wikidocs.net/images/page/22660/word2vec_renew_5.PNG)
    - 평균을 구한 벡터인 projection layer는 두번째 가중치 행렬인 W'와 곱한다. -> 결과값: 마찬가지로 벡터
    - 확률분포를 구할 것이므로 손실 함수로 softmax 함수를 취한다.
        - softmax 함수 출력값의 합은 1이기 때문
    - 그 결과를 **score vector** 라고 한다.

5. 역전파하며 가중치 갱신


### Skip-Gram
- 단어로 맥락을 예측 : 중간의 단어로 **주변 단어 context word**를 예측

![ANN](https://wikidocs.net/images/page/22660/word2vec_renew_6.PNG)
idea of Skip-Gram: CBOW와 달리 Projection Layer에서 Vector들의 평균을 구하지는 않는다.
- PPT 보고 보충

### 한계
- Bag of Words 를 가정하므로 앞뒤를 구분하지 않는다.
    - 해당 문제를 해결하기 위해서는 문장 단위 모델 (RNN, transformer, BERT) 을 사용해야 한다.
- 다음 단어를 예측하는게 확률 분포의 목적이라면, '다음 단어 후보'는 사전의 모든 단어가 아닌 문장 안의 단어면 되는게 아닐까?


## 참고
- [빈도수 세기의 놀라운 마법 Word2Vec, Glove, Fasttext](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/11/embedding/)
- [딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/22660)