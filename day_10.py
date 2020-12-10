from collections import Counter
from typing import Dict, List, Tuple


memo: Dict[Tuple[int, int], int] = {}


def arrangements(adapters: List[int], joltage: int = 0) -> int:
    k = (len(adapters), joltage)
    if k in memo:
        return memo[k]
    if len(adapters) == 0:
        return 0
    adapter = adapters[0]
    n = arrangements(adapters[1:], joltage)
    if adapter > joltage and adapter <= joltage + 3:
        if len(adapters) == 1:
            n += 1
        else:
            n += arrangements(adapters[1:], adapter)
    memo[k] = n
    return n


def differences(adapters):
    adapters.append(0)
    adapters.sort()
    diffs = Counter()
    for i, a in enumerate(adapters[:-1]):
        diffs[adapters[i + 1] - a] += 1
    return dict(diffs)


if __name__ == "__main__":
    with open("day_10.input") as adapter_file:
        adapters = [int(line) for line in adapter_file.readlines()]
    builtin_adapter = max(adapters) + 3
    adapters.append(builtin_adapter)
    d = differences(adapters.copy())
    print(d[1] * d[3])

    adapters.sort()
    print(arrangements(adapters))
