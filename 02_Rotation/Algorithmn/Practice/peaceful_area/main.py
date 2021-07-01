# 휴식을 위하여

import sys 

def solve1():
    # input : a b R / N / coordinates 
    noisy_x, noisy_y, R = map(int, sys.stdin.readline().strip().split())
    N = int(sys.stdin.readline().strip())
    shades = [ 
        sys.stdin.readline().strip().split()    # list로 넘길 것 (문자열로 들어가는데 어떻게 변환하냐)
        for _ in range(N)
    ]

    answers = []
    for shade in shades:
        x, y = float(shade[0]), float(shade[1])
        if (x - noisy_x) ** 2 + (y - noisy_y) ** 2 >= R ** 2:
            answers.append('silent')
        else: answers.append('noisy')

    [print(answer) for answer in answers]

solve1()