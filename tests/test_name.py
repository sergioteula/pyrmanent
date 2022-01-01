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
