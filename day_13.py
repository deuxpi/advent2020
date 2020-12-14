import math
from number_theory import crt


if __name__ == "__main__":
    with open("day_13.input") as input_file:
        timestamp = int(input_file.readline())
        schedule = input_file.readline().strip().split(",")

    min_wait_time = math.inf
    for bus in schedule:
        if bus == "x":
            continue
        bus_id = int(bus)
        wait_time = bus_id - (timestamp % bus_id)
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            earliest_bus = bus_id
    print(min_wait_time * earliest_bus)

    t = 0
    m = 1
    for delay, bus in enumerate(schedule):
        if bus == "x":
            continue
        bus_id = int(bus)
        t = crt(t, bus_id - delay, m, bus_id)
        m *= bus_id
    print(t)
