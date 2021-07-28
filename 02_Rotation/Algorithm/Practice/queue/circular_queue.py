# 원형 큐 / 환형큐 구현


class circular_queue:
    def __init__(self, N):
        self.array = [None for _ in range(N)]  # 몇개 필요?
        self.front_idx = 0
        self.back_idx = N - 1
    
    def is_full(self):
        self.back_idx 

    def push(self, num):
        self.circular_queue[self.back_idx] = num
        self.back_idx += 1

    def pop(self)