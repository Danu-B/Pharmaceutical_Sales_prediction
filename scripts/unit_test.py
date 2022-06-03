import os
import sys
import unittest
import pandas as pd

#Unittest for my module 
sys.path.append(os.path.abspath(os.path.join('../scripts')))
from file_handler import FileHandler


class Unit_Test(unittest.TestCase):

    def setUp(self):
        self.helper = FileHandler()

    def test_to_csv(self):
        df = pd.DataFrame({'unit': range(1,4), 'test': range(3,6)})
        self.helper.to_csv(df, '../data/tests.csv', False)
        df2 = pd.read_csv('../data/tests.csv')
        self.assertEqual(df.shape, df2.shape)

    def test_read_csv(self):
        df = self.helper.read_csv('../data/tests.csv')
        df2 = pd.read_csv('../data/tests.csv')
        self.assertEqual(df.shape, df2.shape)

if __name__ == '__main__':
    unittest.main()
