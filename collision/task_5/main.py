class RectCorrectError(Exception):
    pass
def validate_rectangle(rect, index):
    if not isinstance(rect, list) or len(rect) != 2:
        raise RectCorrectError(f"Прямоугольник {index} должен быть списком из 2 точек, получено: {rect}")
    for i, point in enumerate(rect):
        if not isinstance(point, (tuple, list)) or len(point) != 2:
            raise RectCorrectError(
                f"Прямоугольник {index}: точка {i+1} должна быть кортежем/списком из 2 чисел, "
                f"получено: {point}"
            )
        x, y = point
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise RectCorrectError(
                f"Прямоугольник {index}: точка {i+1} должна содержать числа, получено: {point}"
            )
    (x_left, y_bottom), (x_right, y_top) = rect
    if x_left >= x_right:
        raise RectCorrectError(
            f"Прямоугольник {index}: x-координата левой точки ({x_left}) должна быть меньше x-координаты правой точки ({x_right})"
        )
    if y_bottom >= y_top:
        raise RectCorrectError(
            f"Прямоугольник {index}: y-координата нижней точки ({y_bottom}) должна быть меньше y-координаты верхней точки ({y_top})"
        )
def intersect_two_rects(rect1, rect2):
    (x1_left, y1_bottom), (x1_right, y1_top) = rect1
    (x2_left, y2_bottom), (x2_right, y2_top) = rect2
    intersect_left = max(x1_left, x2_left)
    intersect_right = min(x1_right, x2_right)
    intersect_bottom = max(y1_bottom, y2_bottom)
    intersect_top = min(y1_top, y2_top)
    if intersect_left >= intersect_right or intersect_bottom >= intersect_top:
        return None
    return [(intersect_left, intersect_bottom), (intersect_right, intersect_top)]
def rectangle_area(rect):
    (x_left, y_bottom), (x_right, y_top) = rect
    width = x_right - x_left
    height = y_top - y_bottom
    return width * height
def intersectionAreaMultiRect(rectangles):
    for i, rect in enumerate(rectangles):
        validate_rectangle(rect, i)
    n = len(rectangles)
    if n == 0:
        return 0.0
    if n == 1:
        return rectangle_area(rectangles[0])
    def intersection_of_k_rects(indices):
        if not indices:
            return None
        result = rectangles[indices[0]]
        for idx in indices[1:]:
            result = intersect_two_rects(result, rectangles[idx])
            if result is None: 
                return None
        
        return result
    current_intersection = rectangles[0]
    for i in range(1, len(rectangles)):
        current_intersection = intersect_two_rects(current_intersection, rectangles[i])
        if current_intersection is None:
            return 0.0 
    return rectangle_area(current_intersection)
if __name__ == "__main__":
    rectangles1 = [
        [(0, 0), (4, 4)],
        [(1, 1), (5, 5)],
        [(2, 2), (6, 6)]
    ]
    print(f"Пример 1: {intersectionAreaMultiRect(rectangles1)}") 
    rectangles2 = [
        [(0, 0), (2, 2)],
        [(3, 3), (5, 5)],
        [(1, 1), (4, 4)]  
    ]
    print(f"Пример 2: {intersectionAreaMultiRect(rectangles2)}")  
    rectangles3 = [
        [(0, 0), (3, 3)],
        [(0, 0), (3, 3)],
        [(0, 0), (3, 3)]
    ]
    print(f"Пример 3: {intersectionAreaMultiRect(rectangles3)}") 
    rectangles4 = [
        [(-2, -2), (2, 2)],
        [(-1, -1), (3, 3)],
        [(0, 0), (4, 4)]
    ]
    print(f"Пример 4: {intersectionAreaMultiRect(rectangles4)}")
    try:
        rectangles5 = [
            [(0, 0), (3, 3)],
            [(5, 5), (1, 1)]  
        ]
        print(f"Пример 5: {intersectionAreaMultiRect(rectangles5)}")
    except RectCorrectError as e:
        print(f"Пример 5 ошибка: {e}")
    rectangles6 = [
        [(1, 1), (4, 4)]
    ]
    print(f"Пример 6: {intersectionAreaMultiRect(rectangles6)}")  
    rectangles7 = []
    print(f"Пример 7: {intersectionAreaMultiRect(rectangles7)}") 
