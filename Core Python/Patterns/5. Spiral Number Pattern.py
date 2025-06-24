def spiral_number_pattern(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1
    direction = 0  # 0: right, 1: down, 2: left, 3: up

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        direction = (direction + 1) % 4

    for row in matrix:
        print(*row)


spiral_number_pattern(6)