import unittest
from src.main import main


class TestMain(unittest.TestCase):

    def test_valid_return(self) -> None:
        self.assertEqual(main(), "main")