def intersectionAreaRect(rect1, rect2):
    for i, rect in enumerate([rect1, rect2], 1):
        if not isinstance(rect, list) or len(rect) != 2:
            raise ValueError(f"Прямоугольник {i} должен быть списком из 2 точек (левая нижняя и правая верхняя)")
        left_bottom = rect[0]
        right_top = rect[1]
        for point_name, point in [("левой нижней", left_bottom), ("правой верхней", right_top)]:
            if not (isinstance(point, (list, tuple)) and len(point) == 2):
                raise ValueError(
                    f"Прямоугольник {i}: {point_name} точка должна быть кортежем или списком из 2 чисел, "
                    f"получено: {point}"
                )
        x_left, y_bottom = left_bottom
        x_right, y_top = right_top
        for coord_name, coord in [("x_left", x_left), ("y_bottom", y_bottom), 
                                  ("x_right", x_right), ("y_top", y_top)]:
            if not isinstance(coord, (int, float)):
                raise ValueError(f"Прямоугольник {i}: координата {coord_name} должна быть числом, "
                               f"получено: {coord} (тип: {type(coord).__name__})")
        if x_left >= x_right:
            raise ValueError(f"Прямоугольник {i}: x-координата левой точки ({x_left}) должна быть меньше x-координаты правой точки ({x_right})")
        if y_bottom >= y_top:
            raise ValueError(f"Прямоугольник {i}: y-координата нижней точки ({y_bottom}) должна быть меньше y-координаты верхней точки ({y_top})")
    x1_left, y1_bottom = rect1[0]
    x1_right, y1_top = rect1[1]
    x2_left, y2_bottom = rect2[0]
    x2_right, y2_top = rect2[1]
    intersect_left = max(x1_left, x2_left)
    intersect_right = min(x1_right, x2_right) 
    intersect_bottom = max(y1_bottom, y2_bottom)
    intersect_top = min(y1_top, y2_top) 
    if intersect_left >= intersect_right or intersect_bottom >= intersect_top:
        return 0 
    width = intersect_right - intersect_left
    height = intersect_top - intersect_bottom
    area = width * height
    return area
if __name__ == "__main__":
    rect1 = [(-3.4, 1), (9.2, 10)]
    rect2 = [(-7.4, 0), (13.2, 12)]
    print(f"Пример 1 площадь пересечения: {intersectionAreaRect(rect1, rect2):.2f}")
    try:
        rect15 = [(0, 0), (3)]  
        rect16 = [(0, 0), (3, 3)]
        result = intersectionAreaRect(rect15, rect16)
        print(f"Результат: {result}")
    except ValueError as e:
        print(f"Пример 2 ошибка: {e}")
    try:
        rect17 = [(0, 0), 3] 
        rect18 = [(0, 0), (3, 3)]
        result = intersectionAreaRect(rect17, rect18)
        print(f"Результат: {result}")
    except ValueError as e:
        print(f"Пример 3 ошибка: {e}")
    try:
        rect19 = [(0, "a"), (3, 3)]
        rect20 = [(0, 0), (3, 3)]
        result = intersectionAreaRect(rect19, rect20)
        print(f"Результат: {result}")
    except ValueError as e:
        print(f"Пример 4 ошибка: {e}")
