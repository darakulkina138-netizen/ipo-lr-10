def isCollisionRect(rect1, rect2):
    left1, bottom1 = rect1[0]
    right1, top1 = rect1[1]
    left2, bottom2 = rect2[0]
    right2, top2 = rect2[1]
    intersect_x = (left1 < right2) and (left2 < right1)
    intersect_y = (bottom1 < top2) and (bottom2 < top1)
    return intersect_x and intersect_y
if __name__ == "__main__":
    rect1 = [(-3.4, 1), (9.2, 10)]
    rect2 = [(-7.4, 0), (13.2, 12)]
    print(f"Пример 1: {isCollisionRect(rect1, rect2)}")
    rect3 = [(1, 1), (2, 2)]
    rect4 = [(3, 0), (13, 1)]
    print(f"Пример 2: {isCollisionRect(rect3, rect4)}") 
    rect5 = [(1, 1), (2, 2)]
    rect6 = [(0, 3), (3, 4)]
    print(f"Пример 3: {isCollisionRect(rect5, rect6)}") 
    rect7 = [(0, 0), (4, 4)]
    rect8 = [(2, 2), (6, 6)]
    print(f"Пример 4: {isCollisionRect(rect7, rect8)}")
    rect9 = [(1, 1), (3, 3)]
    rect10 = [(0, 0), (4, 4)]
    print(f"Пример 5: {isCollisionRect(rect9, rect10)}")
    rect11 = [(0, 0), (2, 2)]
    rect12 = [(2, 0), (4, 2)]
    print(f"Пример 6: {isCollisionRect(rect11, rect12)}")
