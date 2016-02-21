import unittest
from BL.StringCreator import  obtain_pairs_number

class EvaluateTestCases(unittest.TestCase):
    def test_WhenEvaluateA_ItShouldBe0(self):
        """
        When the string list is '['A']' the number of pairs should be 0
        """

        'Arrange'
        string_list = ['A']
        expected_value = 0

        'Act'
        current_value = obtain_pairs_number(string_list)

        'Assert'
        self.assertEqual(expected_value, current_value)

    def test_WhenEvaluateB_ItShouldBe0(self):
        """
        When the string list is '['B']' the number of pairs should be 0
        :return:
        """

        'Arrange'
        string_list = ['B']
        expected_value = 0

        'Act'
        current_value = obtain_pairs_number(string_list)

        'Assert'
        self.assertEqual(expected_value, current_value)

    def test_WhenEvaluateAB_ItShouldBe1(self):
        """
        When the string list is '['A', 'B']' the number of pairs should be 0
        :return:
        """

        'Arrange'
        string_list = ['A', 'B']
        expected_value = 1

        'Act'
        current_value = obtain_pairs_number(string_list)

        'Assert'
        self.assertEqual(expected_value, current_value)

    def test_WhenEvaluateBA_ItShouldBe0(self):
        """
        When the string list is '['B', 'A']' the number of pairs should be 0
        :return:
        """

        'Arrange'
        string_list = ['B', 'A']
        expected_value = 0

        'Act'
        current_value = obtain_pairs_number(string_list)

        'Assert'
        self.assertEqual(expected_value, current_value)

    def test_WhenEvaluateBAB_ItShouldBe1(self):
        """
        When the string list is '['B', 'A', 'B']' the number of pairs should be 0
        :return:
        """

        'Arrange'
        string_list = ['B', 'A', 'B']
        expected_value = 1

        'Act'
        current_value = obtain_pairs_number(string_list)

        'Assert'
        self.assertEqual(expected_value, current_value)

    def test_WhenEvaluateBABB_ItShouldBe2(self):
        """
        When the string list is '['B', 'A', 'B', 'B']' the number of pairs should be 2
        :return:
        """

        'Arrange'
        string_list = ['B', 'A', 'B', 'B']
        expected_value = 2

        'Act'
        current_value = obtain_pairs_number(string_list)

        'Assert'
        self.assertEqual(expected_value, current_value)

    def test_WhenEvaluateBABBA_ItShouldBe2(self):
        """
        When the string list is '['B', 'A', 'B', 'B', 'A']' the number of pairs should be 2
        :return:
        """

        'Arrange'
        string_list = ['B', 'A', 'B', 'B', 'A']
        expected_value = 2

        'Act'
        current_value = obtain_pairs_number(string_list)

        'Assert'
        self.assertEqual(expected_value, current_value)

    def test_WhenEvaluateBABBAAB_ItShouldBe5(self):
        """
        When the string list is '['B', 'A', 'B', 'B', 'A', 'A', 'B']' the number of pairs should be 5
        :return:
        """

        'Arrange'
        string_list = ['B', 'A', 'B', 'B', 'A', 'A', 'B']
        expected_value = 5

        'Act'
        current_value = obtain_pairs_number(string_list)

        'Assert'
        self.assertEqual(expected_value, current_value)
