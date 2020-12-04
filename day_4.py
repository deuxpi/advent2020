import re


def parse_passports(passport_input):
    passport = {}
    for line in passport_input:
        if line == "":
            yield passport
            passport = {}
        entries = [entry.split(":") for entry in line.split()]
        for key, value in entries:
            passport[key] = value
    yield passport


def valid_fields(passport):
    if int(passport["byr"]) < 1920:
        return False
    if int(passport["byr"]) > 2002:
        return False
    if int(passport["iyr"]) < 2010:
        return False
    if int(passport["iyr"]) > 2020:
        return False
    if int(passport["eyr"]) < 2020:
        return False
    if int(passport["eyr"]) > 2030:
        return False
    if not passport["hgt"].endswith("in") and not passport["hgt"].endswith("cm"):
        return False
    if passport["hgt"].endswith("cm"):
        if int(passport["hgt"][:-2]) < 150:
            return False
        if int(passport["hgt"][:-2]) > 193:
            return False
    elif passport["hgt"].endswith("in"):
        if int(passport["hgt"][:-2]) < 59:
            return False
        if int(passport["hgt"][:-2]) > 76:
            return False
    else:
        return False
    if re.fullmatch(r"#[0-9a-f]{6}", passport["hcl"]) is None:
        return False
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if re.fullmatch(r"\d{9}", passport["pid"]) is None:
        return False
    return True


def filter_valid_passports(passports):
    all_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    passports = filter(lambda passport: all_keys.issubset(passport.keys()), passports)
    passports = filter(valid_fields, passports)
    return passports


if __name__ == "__main__":
    with open("day_4.input") as passport_file:
        passports = parse_passports(
            [line.strip() for line in passport_file.readlines()]
        )
        valid_passports = filter_valid_passports(passports)
        print(len(list(valid_passports)))
