from typing import List, Set, Tuple


class HandheldGameConsole:
    def __init__(self, program: List[Tuple[str, int]]):
        self.program = program
        self._top = len(self.program) - 1
        self._reset()

    def run(self) -> bool:
        self._visited: Set[int] = set()
        while True:
            if self._pc in self._visited:
                return False
            if self._pc > self._top:
                return True
            self._visited.add(self._pc)
            self._eval(self.program[self._pc])

    def _reset(self) -> None:
        self._pc = 0
        self.acc = 0

    def _eval(self, instr: Tuple[str, int]) -> None:
        if instr[0] == "nop":
            self._pc += 1
        elif instr[0] == "acc":
            self.acc += instr[1]
            self._pc += 1
        elif instr[0] == "jmp":
            self._pc += instr[1]
        else:
            raise RuntimeError("Unknown upcode: %s" % instr[0])


if __name__ == "__main__":
    with open("day_8.input") as program_file:
        program = [
            (instr[0], int(instr[1]))
            for instr in [line.split() for line in program_file.readlines()]
        ]
    console = HandheldGameConsole(program)

    console.run()
    print(console.acc)

    for i, instr in enumerate(program):
        p = program.copy()
        if instr[0] == "jmp":
            p[i] = ("nop", instr[1])
        elif instr[0] == "nop":
            p[i] = ("jmp", instr[1])
        else:
            continue
        console = HandheldGameConsole(p)
        terminated = console.run()
        if terminated:
            print(console.acc)
            break
