import unittest
import data
import pandas as pd
import os


class DataTest(unittest.TestCase):
    def setUp(self) -> None:
        self.link = "http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Test_Data/sample_100k_lines.json"
        self.no_link = ""
        self.random_link = "http://www.google.com"
        self.a = data.get_data(testing=True)
        self.b = data.get_data_from_url(self.link)

    def test_get_data_from_link_invalid_url(self):
        """Test function with empty string"""
        self.assertRaises(ValueError, data.get_data_from_url, self.no_link)

    def test_get_data_from_url_valid_url(self):
        """Test function with valid url that contains no json at the beginning"""
        self.assertRaises(ValueError, data.get_data_from_url, self.random_link)

    def test_get_data_from_url_correct_link(self):
        """Test function with valid url containing JSON objects"""
        self.assertIsInstance(data.get_data_from_url(self.link), pd.DataFrame, "Should be Pandas Dataframe")

    def test_local_data_shape(self):
        """Test function checking if get_url() converts all JSON objects properly into a df"""
        self.assertEqual((10003, 28), self.a.shape, "Should be (10003, 28)")

    def test_online_data_shape(self):
        """Test function checking if get_data_from_url() converts all objects properly into a df"""
        self.assertEqual((102401, 31), self.b.shape, "Should be (102401, 31")


if __name__ == '__main__':
    unittest.main()
