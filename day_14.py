from itertools import product
import re
from typing import List


class Memory(dict):
    def __init__(self, version):
        super()
        self.version = version

    def execute(self, program: List[str]) -> None:
        for instruction in program:
            if instruction.startswith("mask"):
                self.set_mask(instruction[7:])
            elif instruction.startswith("mem"):
                m = re.match(r"^mem\[(?P<address>\d+)\] = (?P<value>\d+)$", instruction)
                if m is None:
                    raise
                self.write(int(m.group("value")), int(m.group("address")))
            else:
                raise

    def set_mask(self, mask: str):
        if self.version == 1:
            self._mask = int(mask.translate(str.maketrans("1X", "01")), 2)
        elif self.version == 2:
            self._mask = int(mask.translate(str.maketrans("01X", "100")), 2)
            self._floating = []
            for i, bit in enumerate(mask):
                if bit == "X":
                    self._floating.append((0, 1 << (35 - i)))
        self._replace = int(mask.replace("X", "0"), 2)

    def write(self, value: int, address: int) -> None:
        if self.version == 1:
            self[address] = (value & self._mask) | self._replace
        elif self.version == 2:
            for floating in (sum(bits) for bits in product(*self._floating)):
                masked_address = (address & self._mask) | self._replace | floating
                self[masked_address] = value
        else:
            raise


if __name__ == "__main__":
    with open("day_14.input") as program_file:
        program = [line.strip() for line in program_file.readlines()]

    mem = Memory(version=1)
    mem.execute(program)
    print(sum(mem.values()))

    mem = Memory(version=2)
    mem.execute(program)
    print(sum(mem.values()))
