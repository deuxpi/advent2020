import operator
import re


class Calculator:
    def __init__(self, expr):
        self.expr = expr
        self._s = []

    def calc(self):
        self._s.append((operator.add, 0))
        s = (operator.add, 0)
        for tok in re.findall(r"\(|\)|\d+|[+*]", self.expr):
            if tok == "+":
                s = (operator.add, s[1])
            elif tok == "*":
                sp = self._s.pop()
                self._s.append((operator.mul, sp[0](sp[1], s[1])))
                s = (operator.add, 0)
            elif tok.isdigit():
                s = (None, s[0](s[1], int(tok)))
            elif tok == "(":
                self._s.append(s)
                self._s.append((operator.add, 0))
                s = (operator.add, 0)
            elif tok == ")":
                sp = self._s.pop()
                s = (None, sp[0](sp[1], s[1]))
                sp = self._s.pop()
                s = (None, sp[0](sp[1], s[1]))
            else:
                raise RuntimeError("unknown token %s" % tok)
        while self._s:
            sp = self._s.pop()
            s = (None, sp[0](sp[1], s[1]))
        return s[1]


print(Calculator("1 + 2 * 3 + 4 * 5 + 6").calc())
print(Calculator("2 * 3 + (4 * 5)").calc())
print(Calculator("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2").calc())

if __name__ == "__main__":
    with open("day_18.input") as homework_file:
        homework = [line.strip() for line in homework_file.readlines()]
    print(sum([Calculator(line).calc() for line in homework]))
