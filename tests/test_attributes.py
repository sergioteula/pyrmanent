import os
import unittest

from pyrmanent import Pyrmanent


class Example(Pyrmanent):
    def __init__(self):
        self.menu = "pizza"
        if hasattr(self, "updated"):
            self.drink = "cola"
        super().__init__()


class TestAttributes(unittest.TestCase):
    def test_attributes(self):
        self._clean()
        example = Example()
        self.assertTrue(hasattr(example, "menu"))
        self.assertFalse(hasattr(example, "drink"))

    def test_attributes_updated(self):
        example = Example()
        example.updated = True
        example.__init__()

        self.assertEqual("cola", example.drink)
        self._clean()

    @staticmethod
    def _clean():
        try:
            os.remove("Example.pickle")
        except OSError:
            pass
