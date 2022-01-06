import os
import unittest

from pyrmanent import Pyrmanent


class Example(Pyrmanent):
    def __init__(self):
        self.menu = "pizza"
        super().__init__()


class TestReset(unittest.TestCase):
    def test_reset(self):
        example = Example()
        example.menu = "rice"
        example.drink = "cola"
        example.save()
        self.assertEqual(example.menu, "rice")
        self.assertTrue(hasattr(example, "drink"))

        example.reset()
        example = Example()
        self.assertEqual(example.menu, "pizza")
        self.assertFalse(hasattr(example, "drink"))

    def setUp(self):
        self._clean()

    def tearDown(self):
        self._clean()

    @staticmethod
    def _clean():
        try:
            os.remove("Example.pickle")
        except OSError:
            pass
