import os
import unittest

from pyrmanent import Pyrmanent


class Example(Pyrmanent):
    def __init__(self, name=""):
        self.menu = "pizza"
        super().__init__(name=name)


class TestPersistency(unittest.TestCase):
    def test_init_values(self):
        example = Example()
        self.assertTrue(hasattr(example, "menu"))
        self.assertEqual(example.menu, "pizza")

    def test_not_saved_values(self):
        example = Example()
        example.menu = "rice"
        example = Example()
        self.assertTrue(hasattr(example, "menu"))
        self.assertEqual(example.menu, "pizza")

    def test_saved_values(self):
        example = Example()
        example.menu = "rice"
        example.save()
        example = Example()
        self.assertTrue(hasattr(example, "menu"))
        self.assertEqual(example.menu, "rice")

    def test_values_for_different_names(self):
        first = Example(name="first")
        second = Example(name="second")
        first.menu = "rice"
        second.menu = "soup"
        first.save()
        second.save()
        first = Example(name="first")
        second = Example(name="second")
        self.assertTrue(hasattr(first, "menu"))
        self.assertTrue(hasattr(second, "menu"))
        self.assertEqual(first.menu, "rice")
        self.assertEqual(second.menu, "soup")

    def setUp(self):
        self._clean()

    def tearDown(self):
        self._clean()

    @staticmethod
    def _clean():
        for file in ["Example", "Example_first", "Example_second"]:
            try:
                os.remove(file + ".pickle")
            except OSError:
                pass
