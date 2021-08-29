## Cheat Sheet
- 최소단위 : Token
    - 보통 띄어쓰기를 기준으로 나눈다.
    - 한국어 vs 영어: 한국어가 더 까다롭다.
        - 한국어 띄어쓰기는 PyKoSpacing으로 교정
    - 주의 : 붙어야 하는 상황 / 떨어져야 하는 상황
    - 활용 : NLTK, SpaCy, KoNLPy
- 불용어 Stopwords 제거
    - 불용어 : 쓸데없는 단어
    - 이론적 배경 : Zipf's Law, Luhn's Cut
    - 예외 : 문장의 구조가 파괴되므로 문장단위 언어모델에서는 제거하지 않음 (e.g. BERT)
- 어간 Stem & 표제어 Lemmatize 추출
    - 어간은 단순한 규칙 기반 알고리즘으로 추출
    - 표제어는 '품사를 고려'해서 추출한다는 점이 다름
    - 장점

---

## Tokenization
> 말뭉치 corpus 를 의미를 가지고 있는 최소단위인 토큰 token 으로 분해하는 과정
### 기준 : 보통 띄어쓰기 whitespace 로 구분한다.
**한국어는 띄어쓰기를 기준으로 한 토큰화가 어렵다.** [참고](https://wikidocs.net/21698)
1. 영어는 굴절어로 단어가 띄어쓰기의 단위지만, 한국어는 어절이 단위인 교착어이므로 형태소 morpheme 분석이 필요하다.
    - 영어 : 단어 전체가 바뀌거나 어미가 바뀌어 문법적인 요소를 나타낸다. (e.g. eat-ate-eaten)
    - 한국어 : 어간에 문법적인 기능을 하는 요소가 붙어(교착)있다. (e.g. 먹다-먹었다-?)
2. 영어는 띄어쓰기가 필수지만 한국어는 띄어쓰기가 필수가 아니었다.
    - 한국어는 띄어쓰기가 잘 지켜지지 않는다. (모아쓰기)
    - 반면 영어는 띄어쓰지 않으면 의미를 이해하기 어렵다. (풀어쓰기)
3. 같은 단어라도 품사에 따라 다르게 사용되는 경우가 있다.
    - 한국어만의 특징은 아닌 것 같지만
4. <p font=yellow> 따라서, 한국어 토큰화를 위해서는 형태소를 기준으로 삼아야하고, 품사태깅을 해야한다.</p>

### 의미 : 토큰은 보통 '의미있는 단위'이지만 상황에 따라 다르다.
한국어에서 '형태소' : 뜻을 가진 가장 작은 말의 단위
- 형태소
    - 자립형태소 : 접사, 어미, 조사와 관계없이 그 자체로 단어가 되는 형태소
        - 체언 (명사, 대명사, 수사), 수식언 (관형사, 부사), 감탄사 등
    - 의존 형태소 : 다른 형태소와 결합하여 사용
        - 접사, 어미, 조사, 어간

### 주의 (영어 기준)
1. 붙어야 하는 상황
    - 여러 단어가 한 뜻을 의미하는 상황 non-compositional words : 관용구 idioms, 표현 phrases
    - 지명 
        - e.g. Los Angeles, New York
    - 구두점 또는 특수문자가 있는 경우 : 제대로 정제하지 않을 시 의미를 잃어버림
        - 정제 cleaning : 구두점이나 특수문자 제거
        - e.g. I received a Ph.D. I'm delighted! *Ph.D.*가 한 단어이므로 다음 예는 두 문장이 아닌 한 문장으로 취급해야 한다.
        - 따라서 마침표를 구분자로 토큰화하지 않는 것이 좋다. (nltk는 마침표를 구분자로 토큰화하지 않는다.)
2. 떨어져야 하는 상황
    - 줄임말 : 아포스트로피 apostrophe (*'*)로 압축된 단어가 있을 때
        - e.g. We're = We are이며 이 때 *'* 이후의 *re*를 '접었다 (clitic)'고 표현한다. 
        - 줄임말과 소유격은 또 다르게 취급해야하니 주의
    - 한국어의 경우 : 어간의 활용된 경우
        - e.g. *먹*다, *먹*고, *먹*어서, *먹*으니 ...
    

### 활용
> 주문제작 custom 이 가능한 라이브러리가 있고, 없는 라이브러리가 있다.
1. NLTK
    - 간단하지만 커스텀 불가
2. SpaCy
    - 좀 복잡해서 러닝 커브 learning curve 가 있지만 커스텀 가능
    - 그래도 익히면 빨리 배운다 : 러닝 커브가 가파르다. (아마도)
    - **SpaCy에서 토큰 커스텀하기**
        ```py
        import spacy
        from spacy import Language

        def main():
            # 토큰화 하고 싶은 문장
            sent = "That's a piece of cake!"       
            nlp: Language = spacy.load("en_core_web_sm")
            # 토큰화된 문장에서 토큰을 설정해 text로 변환
            tokens_before = [token.text for token in nlp(sent)]
            nlp.tokenizer.add_special_case("piece of cake", case)
            # tokens_before 와 동일한 작업
            tokens_after = [token.text for token in nlp(sent)]

        if __name__ == "__main__":
            main()
        ```
- 한국어 형태소 분석기 : 모든 형태소 분석기는 형태소분석, 품사태깅, 명사추출 기능을 제공함
    - KoNLPy : 규칙기반 형태소 분석
    - Hannanum (1999)
    - Kkma : A.K.A 꼬꼬마
    - Mecab : 일본어용 형태소 분석기를 한국어에 맞게 변형
    - Okt : 오픈소스 ((구)Twitter 형태소 분석기)


## 불용어 Stopwords 제거 : Dropping Common Terms
### 불용어란?
DTM을 만들 때 문장 구성에 필요하지만 큰 의미는 없는 단어 (e.g. be동사, 관사) 의 빈도가 높게 나오는 것을 확인했었다. 빈도와 중요도가 비례하는 Count-based Representation에서는 불용어를 제거하는 작업이 필요하다.

### 이론적 배경
1. Zipf's Law : 어떤 언어든 말뭉치 속 단어를 빈도수가 높은 순으로 역정렬하면 $f = \frac{C}{rank}$ 를 따른다.
    - 수학적 통계를 바탕으로 밝혀진 *경험적 법칙*으로, 물리 및 사회 과학 분야에서 연구된 많은 종류의 정보들이 지프 분포에 가까운 경향을 보인다는 것을 뜻한다. (wikipedia, 2021-10-20)
2. Luhn's Cut : 너무 많이 쓰이는 단어(Upper cut-off)는 쓸 데 없고 너무 많이 쓰이지도, 적게 쓰이지도 않는 단어가 중요하다. 불용어 찾기에서 기반이 되는 이론.

|zipf's law|luhn's cut|
|:-:|:-:|
|![zipf's law in nlp](https://www.ngcm.soton.ac.uk/wp-content/uploads/sites/362/2021/07/nlp_zipfs_law.png)|![luhn's cut in nlp](https://www.researchgate.net/profile/Carsten-Lanquillon/publication/45667197/figure/fig4/AS:669415251132434@1536612441901/Luhns-application-of-Zipfs-Law-following-Luhn-1958b-p-120.png)|

### 예외 : 불용어를 제거하면 어떤 문제가 생기나?

This is Apple 에서 This와 is를 없애면 문장이 아니라 단어가 된다. 즉, 불용어를 없애면 **문장의 문법적 구조가 파괴되고 의미가 훼손될 수 있다.** 따라서 문장 단위 *언어모델을 학습 시킬 때는 불용어를 제거하지 않는다. 또, 불용어는 단어의 빈도를 활용해야 하는 상황에서 문제가 되는 단어들이므로 count-based 방식이 아닌 언어모델에서는 불용어를 신경쓰지 않아도 된다. (일반적으로?) 
- *언어모델 : 규칙기반 모델이 아닌 확률/인공신경망을 활용하는 모델로, 문장 전체를 학습한다. 

**라이브러리마다 다르므로 불용어 목록을 미리 확인하고 필터링하는 작업이 필요하다.**
```py
# NLTK에서 확인
from nltk.corpus import stopwords
nltk_stopwords = stopwords.words('english')[:10]     # 영어의 불용어 10개 예시로
text = "Hello World!"   # 토큰화하고 싶은 문장을 text에 입력
# Stopwords 제거
tokens = [
    token   # tokens에 추가 (3)
    for token in word_tokenize(text)    # text의 토큰 중에서 (1)
    if token not in nltk_stopwords      # 불용어에 속하지 않으면 (2)
]
```
```py
# SpaCy에서 확인
import SpaCy
nlp = spacy.load("en_core_web_md")
text = "Hello World!"   # 토큰화하고 싶은 문장을 text에 입력
# Stopwords 제거
tokens = [
    token.text
    for token in nlp(text)
    if token.is_stop
]
```

## 어간, 표제어 추출
> 말뭉치의 단어 수를 줄이기 위해 사용한다. 말뭉치의 단어 개수가 줄어들면 단어의 **밀도**가 줄어들어 성능이 좋아진다!  
> 어간 추출과 표제어 추출의 차이는 품사를 고려했느냐 (표제어) 하지 않았느냐 (어간) 의 차이다.  

1. 어간 Stem : 규칙 기반으로 어간을 추출
    - 빠르다!
    - rule-based algorithm 이므로 어간 같지 않은게 추출되는 edge case가 나온다. 
        - 어떤 규칙? : 대강 뒤에 붙은 활용형 지우는 규칙
            - 활용형?
                - 영어에서는 접사 affix
                - 한국어, 인도유럽어 등에서는 어미 ending; 규칙활용, 불규칙 활용으로 구분됨
        - e.g. : organization -> organ
    - 문제 : 형태소 분석의 결과가 아니므로 일반화를 할 수 없다.
    - 활용 : 대표적인 stemming algorithm : Porter Stemmer
        - Porter Stemmer는 상당히 정밀하게 설계되어 있으므로 정확도가 높다!
2. 표제어 Lematize : 사전에 등록되어 있는 기본형
    - Lemma : 기본 사전형 단어
        - e.g. : is, are, were -> be
    - 활용 : 정규표현식을 사용하면 관용구도 검출할 수 있다.
- 보통 Count-based로 푸는 BoW (Bag of Words) 문제에서 사용한다. (단어의 밀도를 줄이는 것=더 낮은 차원의 벡터 이/가 목표이므로)

참고 : @eubinecto, [wikidocs / 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)