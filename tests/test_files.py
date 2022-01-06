import os
import shutil
import unittest

from pyrmanent import Pyrmanent


class Example(Pyrmanent):
    pass


class TestFiles(unittest.TestCase):
    def test_pickle_file(self):
        Example()
        self.assertTrue(os.path.isfile("Example.pickle"))

    def test_custom_folder(self):
        Example(folder="saves")
        self.assertTrue(os.path.isfile("saves/Example.pickle"))

    def test_custom_nested_folder(self):
        Example(folder="saves/data")
        self.assertTrue(os.path.isfile("saves/data/Example.pickle"))

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
        try:
            shutil.rmtree("saves")
        except OSError:
            pass
