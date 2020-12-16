from typing import Dict


starting_numbers = [1, 12, 0, 20, 8, 16]
last_time_spoken: Dict[int, int] = {}
turn = 1
last_number = None
while turn <= 30000000:
    if turn <= len(starting_numbers):
        number = starting_numbers[turn - 1]
    else:
        if last_number is not None and last_number in last_time_spoken:
            number = turn - last_time_spoken[last_number]
        else:
            number = 0
    if last_number is not None:
        last_time_spoken[last_number] = turn
    print(turn, number)
    last_number = number
    turn += 1
