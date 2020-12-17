from copy import deepcopy
from itertools import product
from typing import Any, List, Tuple


class PocketDimension:
    def __init__(self, dims, initial_state: List[str]):
        self._dims = dims
        self._size = len(initial_state) + 12
        self._off = 6
        g: Any = ["." for x in range(self._size)]
        for d in range(dims - 1):
            g = [deepcopy(g) for n in range(self._size)]
        self._grid = g
        for y in range(len(initial_state)):
            for x, state in enumerate(initial_state[y]):
                if dims == 3:
                    self._set((x, y, 0), state)
                else:
                    self._set((x, y, 0, 0), state)

    def _get(self, v: Tuple[int, ...]) -> str:
        min_d = -self._off
        max_d = self._size - self._off - 1
        if any(d < min_d or d > max_d for d in v):
            return "."
        g = self._grid
        for d in v[::-1]:
            g = g[d + self._off]
        return g

    def _set(self, v: Tuple[int, ...], state: str) -> None:
        g = self._grid
        for d in v[-1:0:-1]:
            g = g[d + self._off]
        g[v[0] + self._off] = state

    def boot(self):
        for i in range(6):
            self.execute_cycle()

    def execute_cycle(self):
        grid = []
        if self._dims == 3:
            for z in range(self._size):
                plane = []
                for y in range(self._size):
                    plane.append(
                        [
                            self._change_state(
                                (x - self._off, y - self._off, z - self._off)
                            )
                            for x in range(self._size)
                        ]
                    )
                grid.append(plane)
        else:
            for w in range(self._size):
                hyperplane = []
                for z in range(self._size):
                    plane = []
                    for y in range(self._size):
                        plane.append(
                            [
                                self._change_state(
                                    (
                                        x - self._off,
                                        y - self._off,
                                        z - self._off,
                                        w - self._off,
                                    )
                                )
                                for x in range(self._size)
                            ]
                        )
                    hyperplane.append(plane)
                grid.append(hyperplane)
        self._grid = grid

    def _add(self, v, dv):
        return tuple([x + dx for x, dx in zip(v, dv)])

    def _change_state(self, v):
        if self._get(v) == "#":
            if self._three_or_four(
                (
                    self._get(self._add(v, dv))
                    for dv in product([-1, 0, 1], repeat=self._dims)
                )
            ):
                return "#"
            else:
                return "."
        else:
            if self._three(
                (
                    self._get(self._add(v, dv))
                    for dv in product([-1, 0, 1], repeat=self._dims)
                )
            ):
                return "#"
            else:
                return "."

    def _three(self, g) -> bool:
        count = 0
        for state in g:
            if state == "#":
                count += 1
                if count > 3:
                    return False
        return count == 3

    def _three_or_four(self, g) -> bool:
        count = 0
        for state in g:
            if state == "#":
                count += 1
                if count > 4:
                    return False
        return count == 3 or count == 4

    def print_grid(self):
        for z in range(self._size):
            if self._dims == 3:
                print("z=%d" % (z - self._off))
                for y in range(self._size):
                    print("".join(self._grid[z][y]))
                print()
            else:
                for w in range(self._size):
                    print("z=%d, w=%d" % (z - self._off, w - self._off))
                    for y in range(self._size):
                        print("".join(self._grid[w][z][y]))
                    print()

    def count_active(self) -> int:
        count = 0
        if self._dims == 3:
            for z in range(self._size):
                for y in range(self._size):
                    count += sum([state == "#" for state in self._grid[z][y]])
        else:
            for w in range(self._size):
                for z in range(self._size):
                    for y in range(self._size):
                        count += sum([state == "#" for state in self._grid[w][z][y]])
        return count


if __name__ == "__main__":
    with open("day_17.input") as initial_state_file:
        initial_state = [line.strip() for line in initial_state_file.readlines()]
    # initial_state = [".#.", "..#", "###"]
    pd = PocketDimension(4, initial_state)
    pd.boot()
    pd.print_grid()
    print(pd.count_active())
