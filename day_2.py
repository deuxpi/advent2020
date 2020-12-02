from typing import Callable, List, NamedTuple, Set


class PasswordRule(NamedTuple):
    policy_1: int
    policy_2: int
    letter: str
    password: str


def parse_rule(rule: str) -> PasswordRule:
    range_rule, letter, password = rule.split()
    policies = [int(r) for r in range_rule.split("-")]
    letter = letter[0]
    return PasswordRule(policies[0], policies[1], letter, password)


def is_valid_password(rule: PasswordRule) -> bool:
    if rule.password.count(rule.letter) < rule.policy_1:
        return False
    if rule.password.count(rule.letter) > rule.policy_2:
        return False
    return True


def is_valid_password_2(rule: PasswordRule) -> bool:
    first_position = rule.password[rule.policy_1 - 1]
    second_position = rule.password[rule.policy_2 - 1]
    if first_position != rule.letter and second_position != rule.letter:
        return False
    if first_position == rule.letter and second_position == rule.letter:
        return False
    return True


def filter_valid_rules(
    rules: List[PasswordRule], policy: Callable[[PasswordRule], bool]
) -> Set[PasswordRule]:
    return set(filter(lambda rule: policy(rule), rules))


if __name__ == "__main__":
    with open("day_2.input") as password_file:
        password_rules = [parse_rule(line) for line in password_file.readlines()]

        valid_rules = filter_valid_rules(password_rules, is_valid_password)
        print(len(valid_rules))

        valid_rules = filter_valid_rules(password_rules, is_valid_password_2)
        print(len(valid_rules))
