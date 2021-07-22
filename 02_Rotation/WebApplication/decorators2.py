def decorator(func):
    def decorated(width, height):
        if width > 0 and height > 0:
            return func(width, height)  # 여기도 return 필요
        else:
            raise ValueError("width and height must be greater than zero")

    return decorated


@decorator
def triangle(width, height):
    return width * height / 2


@decorator
def rectangle(width, height):
    return width * height


# triangle(-1, 5)
num = triangle(1, 5)
print(num)

# rectangle(3, 6)
# rectangle(-3, -6)
