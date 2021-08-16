# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

N, B = map(str, input().split())

result, N = 0, list(N)
for idx in range(len(N)):
    digit = N.pop()  # str
    toDecimal = int(B) ** idx
    if not digit.isdigit():
        digit = ord(digit) - 55
    # print(digit, type(digit))
    result += toDecimal * int(digit)

print(result)


# try 1 : isdigit, isnumeric 모두 같은 문제 발생
# TypeError(연산, 함수가 계산할 때 데이터의 유형이 잘못되었을 때)
# N이 str인 상황에서 loop 돌렸기 때문인듯

# ------------------------ #


def to10(list_N, B, index, result):
    if len(list_N) == 0:
        print(result)
        return result

    digit = list_N.pop()
    if not digit.isdigit():
        digit = ord(digit) - 55
    result += int(digit) * int(B) ** index
    # print(f"(digit {digit}) * (index {index}) ** (B {B}) =  {result} ")

    index += 1
    to10(list_N, B, index, result)


def main():
    N, B = map(str, input().split())
    to10(list(N), B, index=0, result=0)


if __name__ == "__main__":
    main()


# try 2 : 재귀로 풀었을 때 입력값 10 10 에서 정답 1 출력되는 문제
# 10이라는 값이 10진법일때 이를 10진법으로 변환하면 10이 출력되어야 함.
# (digit 1) * (index 0) * (B 10) =  result : 1
# (digit 0) * (index 1) * (B 10) =  result : 1
# 1
# digit이 1 -> 0 으로 잡히기 때문. 왼쪽부터 시작이니 당연히 왼쪽부터 십의자리수가 잡힌다.
# -> RESOLVE
