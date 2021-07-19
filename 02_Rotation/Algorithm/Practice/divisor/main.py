# 약수 구하기

# solution 1 : O(N)
def divisor1(N=int(input())):
    answer = []
    for num in range(1, N + 1):
        if N % num == 0:
            answer.append(num)
    return answer


print(divisor1())

# solution 2 : O(N**0.5) ?? for 범위 줄이기
def divisor2(N=int(input())):
    answer = []
    for num in range(1, round(N ** 0.5) + 1):
        if N % num == 0:
            answer.append(num)
            answer.append(int(N / num))
    return sorted(set(answer))


print(divisor2())
