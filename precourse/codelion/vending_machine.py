# codelion / Chapter 2 / Python으로 만드는 메뉴 자판기
# random.choice(), time.sleep(), for loop, list, set, if-else

# import
import random, time  # random.choie(), time.sleep()

# input
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

# 메뉴 추가
append_menu = True
while append_menu:
    print(lunch)
    food = input("음식을 추가하세요 (종료 : q)").split()
    if food == ["q"]:  # 종료
        append_menu = False
    else:  # 메뉴 추가
        lunch.append(food)

lunch = set(lunch)
print(lunch)  # today's lunch menu

# 메뉴 삭제
delete_menu = True
while delete_menu:
    print(lunch)
    delete_food = input("음식을 삭제하세요 (종료 : q)").split()
    if delete_food == ["q"]:  # 종료
        delete_menu = False
    else:
        print(lunch)
        lunch -= set(delete_food)  # set - set
        print(set(delete_food))

print(f"{lunch} 중에서 선택합니다")

# 카운트다운
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# 메뉴 선택
print(random.choice(list(lunch)))  # random.choice는 list를 argument로 받는다
