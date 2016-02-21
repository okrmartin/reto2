import unittest
from Tests.BL import EvaluateTests, ExpandTest

if __name__ == '__main__':
    test_classes_to_run = [EvaluateTests, ExpandTest]
    loader = unittest.TestLoader()

    suites = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites.append(suite)

    all_suites = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_suites)
