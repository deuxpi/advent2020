class WaitingArea:
    def __init__(self, layout):
        self.layout = layout.copy()

    def apply_rules(self, strategy="adjacent", minimum_occupied_seats=5):
        new_layout = []
        occupied_seats = getattr(self, "_%s" % strategy)
        for row_index, row in enumerate(self.layout):
            new_row = []
            for col_index, seat in enumerate(row):
                new_seat = seat
                if seat == "L":
                    if not any(occupied_seats(row_index, col_index)):
                        new_seat = "#"
                elif seat == "#":
                    if (
                        sum(occupied_seats(row_index, col_index))
                        >= minimum_occupied_seats
                    ):
                        new_seat = "L"
                new_row.append(new_seat)
            new_layout.append(new_row)
        self.layout = new_layout

    def __hash__(self):
        return hash(str(self.layout))

    def print_layout(self):
        for row in self.layout:
            print("".join(row))

    def _adjacent(self, row, column):
        last_row = len(self.layout) - 1
        last_column = len(self.layout[0]) - 1
        if row > 0:
            yield (self.layout[row - 1][column] == "#")
            if column > 0:
                yield (self.layout[row - 1][column - 1] == "#")
            if column < last_column:
                yield (self.layout[row - 1][column + 1] == "#")
        if column > 0:
            yield (self.layout[row][column - 1] == "#")
        if column < last_column:
            yield (self.layout[row][column + 1] == "#")
        if row < last_row:
            yield (self.layout[row + 1][column] == "#")
            if column > 0:
                yield (self.layout[row + 1][column - 1] == "#")
            if column < last_column:
                yield (self.layout[row + 1][column + 1] == "#")

    def _find_occupied_seat(self, row_iter, column_iter_f):
        for row in row_iter:
            for column in column_iter_f(row):
                if column < 0 or column >= len(self.layout[0]):
                    continue
                if self.layout[row][column] == "#":
                    return True
                if self.layout[row][column] == "L":
                    return False
        return False

    def _first_visible(self, row, column):
        yield self._find_occupied_seat(
            range(row - 1, -1, -1), lambda i: [column - (row - i)]
        )
        yield self._find_occupied_seat(range(row - 1, -1, -1), lambda _: [column])
        yield self._find_occupied_seat(
            range(row - 1, -1, -1), lambda i: [column + (row - i)]
        )
        yield self._find_occupied_seat([row], lambda _: range(column - 1, -1, -1))
        yield self._find_occupied_seat(
            [row], lambda _: range(column + 1, len(self.layout[0]))
        )
        yield self._find_occupied_seat(
            range(row + 1, len(self.layout)), lambda i: [column - (i - row)]
        )
        yield self._find_occupied_seat(
            range(row + 1, len(self.layout)), lambda _: [column]
        )
        yield self._find_occupied_seat(
            range(row + 1, len(self.layout)), lambda i: [column + (i - row)]
        )


def count_occupied_seats(layout, minimum_occupied_seats, strategy):
    waiting_area = WaitingArea(layout)

    visited = set()
    while True:
        waiting_area.apply_rules(
            strategy=strategy, minimum_occupied_seats=minimum_occupied_seats
        )
        if waiting_area in visited:
            print(
                sum([sum([seat == "#" for seat in row]) for row in waiting_area.layout])
            )
            break
        visited.add(waiting_area)


if __name__ == "__main__":
    with open("day_11.input") as waiting_area_file:
        layout = [line.strip() for line in waiting_area_file.readlines()]
    count_occupied_seats(layout, 4, "adjacent")
    count_occupied_seats(layout, 5, "first_visible")
