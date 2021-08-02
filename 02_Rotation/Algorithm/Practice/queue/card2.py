from collections import deque


def card(N, Q):
    for _ in range(N - 1):
        remove = Q.popleft()  # 맨 위의 카드는 제거
        back = Q.popleft()
        Q.append(back)
    return Q[0]


def card2(N, Q):
    for _ in range(N - 1):
        Q.popleft()  # 맨 위의 카드는 제거
        Q.append(Q.popleft())
    return Q[0]


def main():
    N = int(input("Input N : "))
    Q = deque([num + 1 for num in range(N)])
    last_card = card(N, Q)
    print(last_card)


if __name__ == "__main__":
    main()
