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
        os.remove("Example.pickle")

    def test_custom_folder(self):
        Example(folder="saves")
        self.assertTrue(os.path.isfile("saves/Example.pickle"))
        shutil.rmtree("saves")

    def test_custom_nested_folder(self):
        Example(folder="saves/data")
        self.assertTrue(os.path.isfile("saves/data/Example.pickle"))
        shutil.rmtree("saves")
