# 회원 탈퇴 기능 구현 (cruD)
1. logic 이므로 views.py에서 delete 기능 구현
    ```py
    class AccountDeleteView(DeleteView):
        model = User
        context_object_name = "target_user"
        success_url = reverse_lazy("accountapp:hello_world")
        template_name = "accountapp/delete.html"
    ```
    파라미터 상세 내용은 12_update_view.md 참고
2. urls.py 에서 routing
    ```py
    path("delete/<int:pk>", AccountDeleteView.as_view(), name="delete"),
    ```
    - CBV의 이름은 항상 `.as_view`로 호출해야 한다.
3. delete.html 
    - 필요없는 bootstrap_form 은 삭제 (load bootstrap4 도 마찬가지)
    - action은 여전히 필요하다. url의 accountapp의 delete를 설정하고 pk도 할당한다.
    <details>
    <summary>detail.html</summary>

    ```html

    {% extends 'base.html' %}

    {% block contents %}    <!-- base.html에서 content가 아닌 contents로 변수명을 지정했기 때문에 contents로 써야 함. -->

    <div class="text-center mw-500 m-auto">
        <div class="m-5">
            <h4>
                Quit
            </h4>
        </div>
        <div>
            <form action="{% url 'accountapp:delete' pk=target_user.pk%}" method="post">
                {% csrf_token %}
                <div class="m-5">
                <input type="submit"
                    class="btn btn-dark rounded-pill px-5">
                </div>
            </form>
        </div>
    </div>


    {% endblock %}
    ```
    </details>
4. delete.html로 이동해야 하므로 detail.html에서 이동하는 링크를 생성한다.
    - update info 링크와 동일한 방식
     ```html
    <div>
        <a href="{% url 'accountapp:delete' pk=target_user.pk %}">
            Quit
        </a>
    </div>    
    ```
5. quit 버튼을 빨간색으로 변환한다.
    - delete.html에서 btn을 danger로 변경한다.
    ```html
    <input type="submit"
        class="btn btn-danger rounded-pill px-5">
    </div>
    ```