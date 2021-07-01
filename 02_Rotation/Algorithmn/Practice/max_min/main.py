# 최대값, 최소값 구하기

def max_min(numbers = list(map(int, input().split()))):
    MAX, MIN = numbers[0], numbers[0]
    for number in numbers:
        if number > MAX: MAX = number
        if number < MIN: MIN = number 
    return (MAX, MIN)

print(max_min())
