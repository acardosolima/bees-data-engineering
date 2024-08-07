import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import main

class TestMain(unittest.TestCase):

    def test_valid_return(self) -> None:
        self.assertEqual(main(), "main")