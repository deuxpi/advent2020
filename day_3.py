class TreeMap:
    def __init__(self, map_input):
        self._map_input = map_input
        self._width = len(self._map_input[0])

    def is_tree(self, x, y):
        return self._map_input[y][x % self._width] == "#"

    def height(self):
        return len(self._map_input)


if __name__ == "__main__":
    with open("day_3.input") as map_file:
        map_input = [line.strip() for line in map_file.readlines()]
    tree_map = TreeMap(map_input)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    solution = 1

    for dx, dy in slopes:
        trees = 0
        x = 0
        for y in range(0, tree_map.height(), dy):
            if tree_map.is_tree(x, y):
                trees += 1
            x += dx
        print("Right %d, down %d: %d" % (dx, dy, trees))
        solution *= trees

    print(solution)
