import os
import unittest

from pyrmanent import Pyrmanent


class Example(Pyrmanent):
    pass


class TestName(unittest.TestCase):
    def test_custom_name(self):
        Example(name="foo")
        self.assertTrue(os.path.isfile("Example_foo.pickle"))
        os.remove("Example_foo.pickle")

    def test_no_custom_name(self):
        Example()
        self.assertTrue(os.path.isfile("Example.pickle"))
        os.remove("Example.pickle")

    def setUp(self):
        self._clean()

    def tearDown(self):
        self._clean()

    @staticmethod
    def _clean():
        for file in ["Example", "Example_foo"]:
            try:
                os.remove(file + ".pickle")
            except OSError:
                pass
