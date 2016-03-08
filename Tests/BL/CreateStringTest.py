import unittest
from BL.StringCreator import CreateString


class EvaluateTestCases(unittest.TestCase):
    def test_WhenCreate3couplesWith3chars_ItShouldReturnTheEmptyString(self):
        """

        :return:
        """

        # Arrange

        # Act
        result = CreateString(3, 3)

        # Assert
        self.assertFalse(result)
