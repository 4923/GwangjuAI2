# 대진표 짜기
# 1팀부터 9팀까지 두 팀씩 짝짓기

import random

# 팀을 생성한 후 섞기
teams = list(range(1, 10))
random.shuffle(teams)  # return : None, inplace function

# 반으로 나누는 작업을 반복
half = len(teams) // 2
print(teams[:half], teams[half:], teams)
results = list(zip(teams[:half], teams[half:]))
print(results)
