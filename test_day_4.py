import unittest
import day_4


class TestDay4(unittest.TestCase):
    def setUp(self):
        self.valid_passport = {
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm",
        }

    def test_valid_passport(self):
        self.assertEqual(
            list(day_4.filter_valid_passports([self.valid_passport])),
            [self.valid_passport],
        )

    def test_missing_fields(self):
        passport = {
            "iyr": "2013",
            "ecl": "amb",
            "cid": "350",
            "eyr": "2023",
            "pid": "028048884",
            "hcl": "#cfa07d",
            "byr": "1929",
        }
        self.assertEqual(list(day_4.filter_valid_passports([passport])), [])

    def test_invalid_birth_year(self):
        passport = self.valid_passport.copy()
        passport["byr"] = "2003"
        self.assertFalse(day_4.valid_fields(passport))

    def test_height_too_big(self):
        passport = self.valid_passport.copy()
        passport["hgt"] = "190in"
        self.assertFalse(day_4.valid_fields(passport))

    def test_invalid_height(self):
        passport = self.valid_passport.copy()
        passport["hgt"] = "190"
        self.assertFalse(day_4.valid_fields(passport))

    def test_invalid_eye_color(self):
        passport = self.valid_passport.copy()
        passport["ecl"] = "wat"
        self.assertFalse(day_4.valid_fields(passport))

    def test_invalid_passport_id(self):
        passport = self.valid_passport.copy()
        passport["pid"] = "0123456789"
        self.assertFalse(day_4.valid_fields(passport))


if __name__ == "__main__":
    unittest.main()
