class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 #точная стоимость пути
        self.h = 0 #предполагаемая стоимость
        self.f = 0 #стоимость текущего узла

    def __eq__(self, other):
        return self.position == other.position

