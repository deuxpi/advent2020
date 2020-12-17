from typing import List


def match_fields(rules, field):
    for label in rules:
        ranges = rules[label]
        for r in ranges:
            if field >= r[0] and field <= r[1]:
                yield label
                break


def match_all(rules, values):
    for label in rules:
        ranges = rules[label]
        if all(
            any(value >= r[0] and value <= r[1] for r in ranges) for value in values
        ):
            yield label


if __name__ == "__main__":
    rules = {}
    nearby_tickets = []

    parsing = "rules"
    with open("day_16.input") as ticket_file:
        for line in ticket_file.readlines():
            line = line.strip()
            if parsing == "rules":
                if line == "":
                    parsing = "your ticket"
                    continue
                label, values = line.split(":")
                ranges = [
                    [int(r) for r in rr.split("-")] for rr in values.split(" or ")
                ]
                rules[label] = ranges
            elif parsing == "your ticket":
                if line == "":
                    parsing = "nearby tickets"
                    continue
                if line == "your ticket:":
                    continue
                your_ticket = [int(number) for number in line.split(",")]
            elif parsing == "nearby tickets":
                if line == "nearby tickets:":
                    continue
                nearby_tickets.append([int(number) for number in line.split(",")])

    error_rate = 0
    valid_tickets: List[List[int]] = []
    for ticket in nearby_tickets:
        valid = True
        for field in ticket:
            m = list(match_fields(rules, field))
            if not m:
                error_rate += field
                valid = False
        if valid:
            valid_tickets.append(ticket)
    print(error_rate)

    num_fields = len(rules)
    mm = []
    for i in range(num_fields):
        m = match_all(rules, [t[i] for t in valid_tickets])
        mm.append(
            [
                f
                for f in m
                if f
                not in [
                    "departure time",
                    "arrival station",
                    "zone",
                    "departure track",
                    "type",
                    "duration",
                    "route",
                    "arrival platform",
                    "departure date",
                    "departure location",
                    "departure station",
                    "class",
                    "arrival location",
                    "row",
                    "departure platform",
                ]
            ]
        )
    for m in mm:
        print(m)

    departure_fields = [2, 7, 9, 12, 18, 19]
    answer = 1
    for i in departure_fields:
        answer *= your_ticket[i]
    print(answer)
