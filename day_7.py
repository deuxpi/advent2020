from collections import Counter
from typing import Dict, List, Optional, Tuple
import re


class Tree(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]


def parse_rule(rule: str) -> Tuple[str, List[Tuple[str, int]]]:
    m = re.match(r"^(?P<container_color>[a-z]+ [a-z]+) bags contain", rule)
    if m is None:
        raise
    container_color = m.group("container_color")
    mm = [
        (m.group("color"), int(m.group("quantity")))
        for m in re.finditer(
            r"(?P<quantity>\d+) (?P<color>[a-z]+ [a-z]+) bags?(?:, |\.)", rule
        )
    ]
    return container_color, mm


def expand(
    tree: Tree,
    root_color: str,
    initial_quantity: int = 1,
    colors: Optional[Counter] = None,
) -> Dict[str, int]:
    if colors is None:
        colors = Counter()
    for color, quantity in tree[root_color]:
        quantity = initial_quantity * quantity
        colors[color] += quantity
        expand(tree, color, quantity, colors)
    return dict(colors)


if __name__ == "__main__":
    contains = Tree()
    contained = Tree()
    with open("day_7.input") as rule_file:
        for rule in rule_file.readlines():
            container_color, contents = parse_rule(rule)
            contains[container_color] = contents
            for color, quantity in contents:
                contained[color].append((container_color, quantity))
    print(len(expand(contained, "shiny gold")))
    print(sum(expand(contains, "shiny gold").values()))
