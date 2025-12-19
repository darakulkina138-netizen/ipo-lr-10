class RectCorrectError(Exception):
    pass
def isCollisionRect(rect1, rect2):
    for rect in [rect1, rect2]:
        x1, y1 = rect[0]
        x2, y2 = rect[1]
        if x1 > x2 or y1 > y2:
            raise RectCorrectError(f"Некорректный прямоугольник: {rect}. "
                                  f"Первая точка должна быть левым нижним углом, "
                                  f"вторая - правым верхним.")
    x1_left, y1_bottom = rect1[0]
    x1_right, y1_top = rect1[1]
    x2_left, y2_bottom = rect2[0]
    x2_right, y2_top = rect2[1]
    if (x1_right > x2_left and x2_right > x1_left and
        y1_top > y2_bottom and y2_top > y1_bottom):
        return True
    return False
print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)])) 
print(isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)])) 
try:
    print(isCollisionRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])) 
except RectCorrectError as e:
    print(f"Ошибка: {e}")
