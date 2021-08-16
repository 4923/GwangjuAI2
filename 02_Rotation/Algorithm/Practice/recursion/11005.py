# 진법 변환 2
# 문제
# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.


# try 1 : for/while loop
# N, B = map(int, input().split())


# def ascii(num):  # 10 ~ 35 -> A ~ Z, return str
#     if 10 <= num <= 35:
#         return chr(num + 55)
#     return str(num)


# converted = []
# while N > 0:
#     N, mod = divmod(N, B)
#     converted.append(ascii(mod))

# converted.reverse()
# result = "".join(converted)
# print(result)

# 0 0 입력시 00 출력되게해서 한 번 틀림 (몫이 0일때를 종료 조건으로 잡고 몫이 0이면 남은 값 다 털었는데 그렇게 하면 BOJ 80%초반에서 오답)

# ----------------- #

# try 2 : recursion


def ascii(num):  # 10 ~ 35 -> A ~ Z, return str
    if 10 <= num <= 35:
        return chr(num + 55)
    return str(num)


def convert(converted, N, B):
    if not N > 0:
        converted.reverse()
        return converted
    N, mod = divmod(N, B)
    converted.append(ascii(mod))
    convert(converted, N, B)


def main():
    converted = []
    N, B = map(int, input().split())
    if N == 0:  # 0 10 에서 출력값 없어지는 문제
        converted.append(str(0))
    else:
        convert(converted, N, B)

    print("".join(converted))


if __name__ == "__main__":
    main()


# while lopo와 시간은 동일
