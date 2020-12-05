from typing import List, Optional, Tuple


def seat(boarding_pass: str) -> Tuple[int, int]:
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)
    return (row, column)


def seat_id(seat: Tuple[int, int]) -> int:
    return seat[0] * 8 + seat[1]


if __name__ == "__main__":
    all_seats: List[Optional[int]] = [i for i in range(1024)]
    with open("day_5.input") as boarding_pass_file:
        boarding_passes = [line.strip() for line in boarding_pass_file.readlines()]
    seat_ids = [seat_id(seat(boarding_pass)) for boarding_pass in boarding_passes]
    print(max(seat_ids))
    for sid in seat_ids:
        all_seats[sid] = None
    empty_seat = next(
        filter(
            lambda s: s[0] > 5 and s[0] < 102,
            [divmod(seat, 8) for seat in filter(None, all_seats)],
        )
    )
    print(seat_id(empty_seat))
