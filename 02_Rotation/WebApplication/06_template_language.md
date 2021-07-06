# Django Template Language

웹 페이지의 구역을

1. header
2. contents
3. footer

세개로 나눈다고 할 때

header와 footer는 대부분의 페이지가 공유하는 부분이고, (include)  
contents는 실질적으로 변경되는 부분이다. (extends)

따라서, 재사용 할 수 있는 부분은 재사용 하는 것이 경제적이며 이를 위해 django는 template language를 제공한다.

## `extends`
재활용 되는 부분은 재사용하자. (header, footer)
바탕이 되는 html을 가져와서 `extends` 구문을 사용한다.

## `include`
틀이 있다고 할 때 틀에 값을 채우는 작업

틀에서 extend, 값을 include



- Template Language [(공식문서 kor)](https://django-doc-test-kor.readthedocs.io/en/old_master/topics/templates.html#template-inheritance) / [(참고 velog)](https://velog.io/@hidaehyunlee/Django-%ED%85%9C%ED%94%8C%EB%A6%BF-%EC%96%B8%EC%96%B4)  
    또, Django에서는 Template 언어를 사용할 수 있는데 사용방법은 다음과 같다.
    - 템플릿 변수 : 뷰에서 템플릿으로 객체를 전달한다. 
        - `{{ 변수 }}`
    - 템플릿 필터 : 변수의 값을 특정 언어로 변환할 때 사용한다.
        - `|` 파이프를 사용한다. 
        - [Django의 내장 필터](https://django-doc-test-kor.readthedocs.io/en/old_master/ref/templates/builtins.html#ref-templates-builtins-filters)
        - 처음 보는 부분이라 공부가 좀 더 필요하다.
    - 템플릿 태그 : python의 문법을 사용할 수 있게 한다.
        - 반복문 for 에서의 활용
            ```django
            {% for template in templates %} 
            {% template %} 
            {% end for %}
            ```
            반복문 종료시 반드시 `{% end for %}` 라고 적어주어야 한다.
        - 분기문 if 에서의 활용
            ```django
            {% if student_list %}
                총 학생 수 : {{ student_list|length }}
            {% else %}
                학생이 없어요!
            {% endif %}
            ```
            마찬가지로 분기문 종료시 `{% endif %}`를 적어야 한다.
    
    템플릿 언어는 익숙해질 때 까지 많이 사용해보는 것이 좋겠다.
