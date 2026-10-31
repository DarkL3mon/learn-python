import pytest
import unittest

from algorithms import basicMath

class TestForLoop(unittest.TestCase):
    @staticmethod
    def test_sum_all_digits():
        """Test the sum_all_digits function."""
        # Assert that the sum of all digits in the list
        assert basicMath.sum_all_digits([1, 2, 3, 4, 5, 6, 7, 11]) == 30
        with pytest.raises(ValueError):
            basicMath.sum_all_digits([1, 2, 3, 4, 5, 6, 7, 11, "abc"])

        # Assert that the sum of all digits in the set
        assert basicMath.sum_all_digits({1, 2, 3, 4, 5, 6, 7, 11}) == 30
        with pytest.raises(ValueError):
            basicMath.sum_all_digits({1, 2, 3, 4, 5, 6, 7, 11, "abc"})

        # Assert that the sum of all digits in the tuple
        assert basicMath.sum_all_digits((1, 2, 3, 4, 5, 6, 7, 11)) == 30
        with pytest.raises(ValueError):
            basicMath.sum_all_digits((1, 2, 3, 4, 5, 6, 7, 11, "abc"))

        # Assert that the sum of all digits in the number
        assert basicMath.sum_all_digits(123456711) == 30

        # Assert that the sum of all digits in the string
        assert basicMath.sum_all_digits("123456711") == 30
        with pytest.raises(ValueError):
            basicMath.sum_all_digits("123456711abc")

    @staticmethod
    def test_sum_timestamp_digits():
        """Test the sum_timestamp_digits function."""
        # Assert that the sum of digits in the current timestamp is an integer
        assert isinstance(basicMath.sum_timestamp_digits(), int)
        assert basicMath.sum_timestamp_digits() >= 0  # The sum should be non-negative

    @staticmethod
    def test_lookup_for_digit():
        """Test the lookup_for_digit function."""
        assert basicMath.lookup_for_digit(3, [1, 2, 3, 4, 5]) == True
        assert basicMath.lookup_for_digit(6, [1, 2, 3, 4, 5]) == False
        assert basicMath.lookup_for_digit(1, 102030) == True
        assert basicMath.lookup_for_digit(6, 102030) == False
        assert basicMath.lookup_for_digit(1, "102030") == True
        assert basicMath.lookup_for_digit(6, "102030") == False

    @staticmethod
    def test_count_digit_occurrences():
        """Test the count_digit_occurrences function."""
        assert basicMath.count_digit_occurrences(3, [1, 2, 3, 4, 5]) == 1
        assert basicMath.count_digit_occurrences(6, [1, 2, 3, 4, 5]) == 0
        assert basicMath.count_digit_occurrences(0, 102030) == 3
        assert basicMath.count_digit_occurrences(6, 102030) == 0
        assert basicMath.count_digit_occurrences(0, "102030") == 3
        assert basicMath.count_digit_occurrences(6, "102030") == 0
