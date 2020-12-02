import unittest
import day_2


class TestDay2(unittest.TestCase):
    def test_is_valid_password(self):
        rule = day_2.PasswordRule(1, 3, "a", "abcde")
        self.assertTrue(day_2.is_valid_password(rule))

    def test_contains_no_instances_of_letter(self):
        rule = day_2.PasswordRule(1, 3, "b", "cdefg")
        self.assertFalse(day_2.is_valid_password(rule))

    def test_contains_too_many_instances_of_letter(self):
        rule = day_2.PasswordRule(1, 3, "c", "ccccccccc")
        self.assertFalse(day_2.is_valid_password(rule))

    def test_first_position_contains_letter_and_second_does_not(self):
        rule = day_2.PasswordRule(1, 3, "a", "abcde")
        self.assertTrue(day_2.is_valid_password_2(rule))

    def test_neither_positions_contain_letter(self):
        rule = day_2.PasswordRule(1, 3, "b", "cdefg")
        self.assertFalse(day_2.is_valid_password_2(rule))

    def test_both_positions_contain_letter(self):
        rule = day_2.PasswordRule(2, 9, "c", "ccccccccc")
        self.assertFalse(day_2.is_valid_password_2(rule))


if __name__ == "__main__":
    unittest.main()
