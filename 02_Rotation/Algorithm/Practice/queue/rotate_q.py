# https://www.acmicpc.net/problem/1021


def move_cnt(Q, target: int, current: int):
    start, end = current, target
    if current > target:
        start, end = target, current
    move_1 = (end - start) - Q[start - 1 : end].count(None)
    move_2 = (len(Q) + start - end) - (Q[: start - 1].count(None) + Q[end:].count(None))

    return move_1, move_2


def move(Q, targets: list, current=1) -> int:
    cnt = 0
    for target in targets:
        move_1, move_2 = move_cnt(Q, target, current)
        if move_2 < move_1:
            cnt += move_2
            current = target
        elif move_1 <= move_2:
            cnt += move_1
            current = target

        Q[target - 1] = None
        current += 1
    return cnt


def main():
    N, M = map(int, input("input N and M : ").split())
    targets = map(int, input("what is your targets? : ").split())  # M
    Q = [num + 1 for num in range(N)]

    cnt = move(Q, targets)
    print(cnt)


if __name__ == "__main__":
    main()


# 10 10
# 1 6 3 2 7 9 8 4 10 5
# None None ~ 일 때 cnt가 하나 더 추가됨
# 누적 cnt 8에서 10이 되어야 하는데 11이 된다.
# 그 외 BOJ 예제는 문제 X
# move에서 시작점을 start가 아닌 start-1로 잡기
