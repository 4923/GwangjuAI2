# decorators3
def is_user(func):
    def decorated(user):
        if not user.authority:
            raise PermissionError("User is not authorized")
        return func(user)

    return decorated


# decorators2
def is_positive(func):
    def decorated(user, width, height):
        if width > 0 and height > 0:
            return func(user, width, height)  # 여기도 return 필요
        else:
            raise ValueError("width and height must be greater than zero")

    return decorated


class User:
    def __init__(self, authority):
        self.is_authenticated = authority


user = User(authority=False)


@is_positive
@is_user
def triangle(user, width, height):
    return width * height / 2


@is_positive
@is_user
def rectangle(user, width, height):
    return width * height


# triangle(-1, 5)
num = triangle(user, 1, 5)
print(num)

# rectangle(3, 6)
# rectangle(-3, -6)
