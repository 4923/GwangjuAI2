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
        print("\t", answer, (N + 1) * X, X)
    return answer


print(solution1())

# # solution 2 : if condition
# def solution2(N=int(input())):
#     answer, div = 0, 1
#     for num in range(N * (N - 1)):
#         print(num)
#         if div == N:
#             return answer
#         if num // div == num - (div * N):
#             answer += num
#         div += 1
#     return "Fail"


# # print(solution2())

# N = int(input())
# print(N)
# answer, div = 0, 1
# for num in range(N * (N - 1)):
#     print(num)
#     if div == N:
#         break
#     if num // div == num - (div * N):
#         answer += num
#     div += 1

# print()
# print(answer)
