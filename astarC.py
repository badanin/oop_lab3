import numpy as np
from NodeC import Node
from ret_path import RetPath


class AStar:

    def search(self, maze, cost, start, end):
        # Возврящаем кортежи пути по лабиринтам

        # начальный и конечный узел
        start_node = Node(None, tuple(start))
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, tuple(end))
        end_node.g = end_node.h = end_node.f = 0

        # еще не посещенные узлы
        yet_to_visit_list = []
        # исследованные узлы
        visited_list = []

        # Начальный узел
        yet_to_visit_list.append(start_node)

        # лимит проверок
        outer_iterations = 0
        max_iterations = (len(maze) // 2) ** 10

        # направления движения
        move = [[-1, 0],  # вверх
                [0, -1],  # влево
                [1, 0],  # вних
                [0, 1]]  # вправо

        # определение количество строк и столбцов в лабиринте
        no_rows, no_columns = np.shape(maze)

        # цикл до тех порка пока все узлы не будут посещены

        while len(yet_to_visit_list) > 0:

            # количество итераций
            outer_iterations += 1

            # Получаем текущий узел
            current_node = yet_to_visit_list[0]
            current_index = 0
            for index, item in enumerate(yet_to_visit_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # проверка лимити итераций
            if outer_iterations > max_iterations:
                print("слишком много итераций")
                return RetPath.return_path(current_node, maze)

            # отмечаем посещенные узлы
            yet_to_visit_list.pop(current_index)
            visited_list.append(current_node)

            # проверяем окончательный узел с текущем
            if current_node == end_node:
                return RetPath.return_path(current_node, maze)

            # создаем дочерних
            children = []

            for new_position in move:

                # определяем позицию узла
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # проверка что мы не выходим за границы лабиринта
                if (node_position[0] > (no_rows - 1) or
                        node_position[0] < 0 or
                        node_position[1] > (no_columns - 1) or
                        node_position[1] < 0):
                    continue

                # проверяем на проходимость
                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                # создаем новый узел
                new_node = Node(current_node, node_position)

                # добавляем в дочерни
                children.append(new_node)

            # перебор дочерних узлов
            for child in children:

                # проверка на посещение дочерних узлов
                if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                    continue

                # создаем значения f, g, h
                child.g = current_node.g + cost
                # расчер евклидово расстояние
                child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                           ((child.position[1] - end_node.position[1]) ** 2))

                child.f = child.g + child.h

                # Если дочерний в списке и g меньше 0
                if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                    continue

                # добавляем у лист
                yet_to_visit_list.append(child)
