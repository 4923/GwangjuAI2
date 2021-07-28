def insertion_sort(num_list):
    # bef_n_list = num_list,copy() 는 얕은 copy
    # list는 mutable하므로 copy()로 가능
    # 여기서 num_list를 받지 않으면 전역변수화 되어서 번거로워 진다.

    # 값을 교환해야 할 때는 index로 도는게 낫다.
    # 변수 받아서 값을 변경해도 list가 변하지는 않음
    # 값 가져오면서 enumerate 해도 상관 없지만 이건 알고리즘 문제풀이에서는 잘 쓰지 않는다.
    # 숫자랑 값을 같이 묶어서 새로만드는 작업이기 때문에 작업 횟수가 늘어난다.
    #
    # 조건을 만족하지 않는 동안 반복해야 하므로 반복문을 한번 더 써야 한다.
    #
    # for문도 while문도 ok
    # 교환 조건 1: 일차적으로 끝에 도달하기 전
    # 자기 앞의 값을 볼 것이므로 i가 0보다 클 동안이 조건 (끝에 도달한다는 조건)
    # 교환 조건 2: 앞에 있는 값이 나보다 큰 값일 때 변경한다.
    # 교환 조건 둘 다 만족해야 하므로 조건은 and로 연결한다.

    # if문이 and로 연결된 경우 앞의 값이 False일 경우 앞이 틀리면 뒤는 해석하지 않고 중단

    # A or B 의 not : not A and B (집합으로 확인 가능)
    return []


def selection_sort():
    # 최솟값을 찾는것이 core (최대값도 상관 X)
    # 최솟값을 기준 범위의 첫번째 값과 위치를 바꾼다.
    # 왜 교환을 하는가? 교환을 하게 되면 두번째 최솟값을 찾게 된다 : 이제 두번쨰 최솟값은 2번째 위치에 이동

    # 부분정렬
    # 느린 이유가 있다. 본 위치까지는 정렬이 되었다는 보장이 있다.
    return []


def bubble_sort():

    return []


n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort()
print(" ".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort()
print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort()
print(" ".join(map(str, bubble_sorted_list)))
