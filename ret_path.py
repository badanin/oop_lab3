import numpy as np


class RetPath:

    # Функция пути
    def return_path(current_node, maze):
        path = []
        no_rows, no_columns = np.shape(maze)
        # инициализируем лабиринт с -1
        result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        # Получаем обратный путь
        path = path[::-1]
        start_value = 0
        # обновляем путь в обраном порядке увеличивая на 1
        for i in range(len(path)):
            result[path[i][0]][path[i][1]] = start_value
            start_value += 1
        return result
