from typing import Optional, Set


if __name__ == "__main__":
    with open("day_6.input") as answer_file:
        group: Optional[Set] = None
        counts = 0
        for line in answer_file.readlines():
            if line == "\n":
                if group is not None:
                    counts += len(group)
                group = None
            else:
                if group is None:
                    group = set(list(line.strip()))
                else:
                    group.intersection_update(list(line.strip()))
        if group is not None:
            counts += len(group)
        print(counts)
