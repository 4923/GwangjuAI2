# Word2Vec
1. 언어 모델로 비유문제를 풀 수 있다. 자연어처리의 전제 중 하나인 `Distributional Semantics` 를 따르며 비슷한 단어의 벡터표현이 유사하다는데 착안한다.
2. Word2Vec는 의미를 이해하는데 이는 곧 cosine similarity가 크다는 뜻과 일맥상통한다. 사용자가 입력한 쿼리를 확장할 수 있고 맥락이 비슷한 단어와 동의어를 추출할 수 있으므로 (단순한 수준의) 검색엔진에서 주로 사용된다. : 동의어 확장 Synonym expansion
3. 방식
    - CBOW (Contiinuous Bag of Words)
        - BoW에서 발전된 방식?
        - 주변의 단어를 가지고 **중간의 center word** 단어를 예측
    - Skip-Gram
        - 중간의 단어로 **주변 단어 context word**들을 예측
    
    - 앞 뒤로 몇개의 단어를 볼지 : window (이 때 선택을 바꿔가며 데이터셋을 생성하는 방법은 sliding window라고 한다.)
        - 아니 이걸 window 말고 뭐라고 했는데 gram이 아닌거같고 뭐더라


# Word Embeddings
구축하고, 기반을 둔다는 뜻인 Embedding을 사용하는 Word Embedding은 단어의 의미를 단어를 표현한 벡터에 두는 기법이다.


- 


# ref
- [빈도수 세기의 놀라운 마법 Word2Vec, Glove, Fasttext](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/11/embedding/)
-