from collections import deque


def card2(N, Q):
    for _ in range(N - 1):
        Q.popleft()  # 맨 위의 카드는 제거
        Q.append(Q.popleft())
    return Q[0]


def main():
    # N = int(input("Input N : "))      # BOJ 오답처리
    N = int(input())  # BOJ 정답
    Q = deque([num + 1 for num in range(N)])
    last_card = card2(N, Q)
    print(last_card)

    print(type(last_card))


if __name__ == "__main__":
    main()
