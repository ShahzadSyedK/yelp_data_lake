import unittest
import sys
import os

# Ensure the src and tests directories are in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def run_all_tests():
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)

if __name__ == "__main__":
    run_all_tests()
