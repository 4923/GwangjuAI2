def insertion_sort():
    # 각각의 모든 요소를 이미 정렬된 앞의 배열 부분과 비교하여 적절한 위치로 옮겨 삽입한다.
    # i번째값을 비교하는 상황에서 i-1까지는 정렬된 배열이다

    # 자신의 위치를 어떻게 찾지?
    # 뒤에서부터 쫓아가며 자기보다 큰 값이 있을 경우 그 직전에 삽입
    # (insert 사용할 수 없으니 끝에서부터 자리 비교해가며 적절한 자리까지 swap)
    for now in range(n):
        for swap in range(now, 0, -1):  # 직전까지 / 이전값과 비교
            if num_list[swap - 1] > num_list[swap]:
                num_list[swap - 1], num_list[swap] = num_list[swap], num_list[swap - 1]
    return num_list


def selection_sort():
    # 주어진 리스트 범위내에서 (0부터끝까지) 최솟값을찾는다
    # 처음 위치에 최솟값을 넣는다. (교환한다.)
    # 다음 인덱스 (1부터 끝까지) 범위 내에서 최솟값을 찾는다.
    # 처음 위치에 최솟값을 넣는다. (이하동일)
    # => 최소값을 골라 맨 앞에 차례로 (맨 앞 : num_list[start], not num_list[0]) 쌓아나가는 정렬

    for start in range(n):
        min_idx = start  # 최소값은 첫 인덱스~끝인덱스에서 가장 작은 값. 인덱스로 저장
        for search in range(start, n):
            if num_list[search] < num_list[min_idx]:
                min_idx = search
        num_list[start], num_list[min_idx] = num_list[min_idx], num_list[start]
    return num_list


def bubble_sort():
    # 전부 탐색
    for i in range(n):
        for j in range(i):
            if num_list[i] < num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list


# 기준값
n = int(input("how many number will you input : "))
num_list = []

# 입력
for i in range(n):
    num = int(input(f"[{i}] input your number : "))
    num_list.append(num)

# 실행

insertion_sorted_list = insertion_sort(
    num_list
)  # 여기에 num_list를 parameter로 넘기지 않으면 전역변수로 사용하기 때문에 불편함 (상관이 없기는 함)
print(" ".join(map(str, insertion_sorted_list)))

# selection_sorted_list = selection_sort()
# print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort()
print(" ".join(map(str, bubble_sorted_list)))
