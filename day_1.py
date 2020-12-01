from typing import List


def find_sum(report: List[int], num_entries: int, sum_to: int = 2020) -> List[int]:
    if num_entries == 0:
        return []
    for i, entry in enumerate(report):
        rest = find_sum(report[i + 1 :], num_entries - 1, sum_to - entry)
        if len(rest) == num_entries - 1 and entry + sum(rest) == sum_to:
            return [entry] + rest
    return []


if __name__ == "__main__":
    with open("day_1.input") as input_file:
        report = [int(entry) for entry in input_file.readlines()]
        entries = find_sum(report, 2)
        print("%d * %d = %d" % (entries[0], entries[1], entries[0] * entries[1]))
        entries = find_sum(report, 3)
        print(
            "%d * %d * %d = %d"
            % (entries[0], entries[1], entries[2], entries[0] * entries[1] * entries[2])
        )
