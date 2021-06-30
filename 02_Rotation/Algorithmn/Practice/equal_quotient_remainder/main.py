# 나머지와 몫이 같은 수 구하기

# solution 1 : summation
"""
number / N = Quotient ... Remainder
number = N * Quotient + Remainder

\because Quotient == Remainder
if Quotient = Remainder = X
\therefore number = N * X + X = X * (N + 1)
"""

# input
def solution1(N=int(input())):
    answer = 0
    for X in range(N - 1, 0, -1):  # 자기자신으로 나누면 나머지가 0이므로 범위에서 제외
        answer += (N + 1) * X  # 공식에 따라 N+1에 변화하는 값 X를 곱하여 총계에 합산
    return answer


print(solution1())

# # solution 2 : if condition
# 최대값인 N * N -1 까지 돌면서 N - 1 까지의 수로 나눈 후 나머지와 몫 비교


def solution2(N=int(input())):
    answer = 0
    for num in range(1, N * N):
        if num // N == num % N:
            answer += num
    return answer


print(solution2())
