class Ship:
    def __init__(self):
        self.course = 0
        self.ns = 0
        self.ew = 0
        self.waypoint_ns = 1
        self.waypoint_ew = 10

    def navigate(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])
        if action == "N" or (action == "F" and self.course == 90):
            self.ns += value
        elif action == "S" or (action == "F" and self.course == 270):
            self.ns -= value
        elif action == "E" or (action == "F" and self.course == 0):
            self.ew += value
        elif action == "W" or (action == "F" and self.course == 180):
            self.ew -= value
        elif action == "L":
            self.course = (self.course + value) % 360
        elif action == "R":
            self.course = (self.course - value) % 360
        else:
            raise RuntimeError(
                "action %s value %d course %d" % (action, value, self.course)
            )

    def move_waypoint(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])
        if action == "N":
            self.waypoint_ns += value
        elif action == "S":
            self.waypoint_ns -= value
        elif action == "E":
            self.waypoint_ew += value
        elif action == "W":
            self.waypoint_ew -= value
        elif (action == "L" and value == 90) or (action == "R" and value == 270):
            self.waypoint_ns, self.waypoint_ew = self.waypoint_ew, -self.waypoint_ns
        elif (action == "L" or action == "R") and value == 180:
            self.waypoint_ns, self.waypoint_ew = -self.waypoint_ns, -self.waypoint_ew
        elif (action == "L" and value == 270) or (action == "R" and value == 90):
            self.waypoint_ns, self.waypoint_ew = -self.waypoint_ew, self.waypoint_ns
        elif action == "F":
            self.ns += self.waypoint_ns * value
            self.ew += self.waypoint_ew * value
        else:
            raise RuntimeError(
                "action %s value %d course %d" % (action, value, self.course)
            )

    def distance(self):
        return abs(self.ns) + abs(self.ew)


if __name__ == "__main__":
    with open("day_12.input") as instruction_file:
        instructions = [line.strip() for line in instruction_file.readlines()]

    ship = Ship()
    for instruction in instructions:
        ship.navigate(instruction)
    print(ship.distance())

    ship = Ship()
    for instruction in instructions:
        ship.move_waypoint(instruction)
    print(ship.distance())
