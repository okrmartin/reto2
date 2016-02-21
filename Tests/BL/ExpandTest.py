import unittest
from BL.StringCreator import Expand


class ExpandTestCases(unittest.TestCase):
    """ExpandTestCases"""

    def test_WhenExpandNilString(self):
        """
        When the value to expand is ''
        the expected value should be ['']
        """

        'Arrange'
        value = ['']
        expected_value = [['']]

        'Act'
        current_value = Expand(value)

        'Assert'
        self.assertEqual(1, len(current_value))
        self.assertEqual(expected_value, current_value)

    def test_WhenExpandOneAChar(self):
        """
        When the value to expand is 'A'
        the expected value should be ['B']
        """

        'Arrange'
        value = ['A']
        expected_value = [['B']]

        'Act'
        current_value = Expand(value)

        'Assert'
        self.assertEqual(1, len(current_value))
        self.assertEqual(expected_value, current_value)

    def test_WhenExpandOneBChar(self):
        """
        When the value to expand is 'B'
        the expected value should be ['A']
        """

        'Arrange'
        value = ['B']
        expected_value = [['A']]

        'Act'
        current_value = Expand(value)

        'Assert'
        self.assertEqual(1, len(current_value))
        self.assertEqual(expected_value, current_value)

    def test_WhenExpandAAChar(self):
        """
        When the value to expand is '['A', 'A']'
        the expected value should be [['A', 'B'], ['B', 'A']]
        """

        'Arrange'
        value = ['A', 'A']
        expected_value = [['A', 'B'], ['B', 'A']]

        'Act'
        current_value = Expand(value)

        'Assert'
        self.assertEqual(expected_value, current_value)
