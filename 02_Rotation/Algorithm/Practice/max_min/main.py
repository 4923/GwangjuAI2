# 최대값, 최소값 구하기

# solution 1
def max_min(numbers=list(map(int, input().split()))):
    MAX, MIN = numbers[0], numbers[0]
    for number in numbers:
        if number > MAX:
            MAX = number
        if number < MIN:
            MIN = number
    return (MAX, MIN)


print(max_min())

# solution 2 : halving

# find_max
def find_max(numbers):
    MAX = numbers[0]
    for number in numbers:
        if number > MAX:
            MAX = number
    return MAX


def halving(numbers):
    leng = len(numbers)
    # MAX_1, MAX_2 = find_max(numbers[:leng//2]), find_max(numbers[leng//2:])
    # eh.......
