import unittest
import day_1


class TestDay1(unittest.TestCase):
    def test_trivial_find_sum_of_two(self):
        report = [1, 2]
        self.assertEqual(day_1.find_sum(report, 2, 3), [1, 2])

    def test_trivial_find_sum_of_three(self):
        report = [1, 2, 3]
        self.assertEqual(day_1.find_sum(report, 3, 6), [1, 2, 3])

    def test_find_sum_of_two(self):
        report = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(day_1.find_sum(report, 2), [1721, 299])

    def test_find_sum_of_three(self):
        report = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(day_1.find_sum(report, 3), [979, 366, 675])

    def test_find_not_less_than_requested_number_of_entries(self):
        report = [4, 3, 2, 1]
        self.assertEqual(day_1.find_sum(report, 2, 3), [2, 1])

    def test_find_not_more_than_requested_number_of_entries(self):
        report = [4, 3, 2, 5]
        self.assertEqual(day_1.find_sum(report, 2, 9), [4, 5])

    def test_failure_to_find_sum(self):
        report = [1, 2, 3]
        self.assertEqual(day_1.find_sum(report, 2, 10), [])


if __name__ == "__main__":
    unittest.main()
