import unittest
import data
import pandas as pd


class DataTest(unittest.TestCase):
    def setUp(self) -> None:
        self.link = "http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Test_Data/sample_100k_lines.json"
        self.no_link = ""
        self.random_link = "http://www.google.com"

    def test_get_data_from_link_invalid_url(self):
        """Test function with empty string"""
        self.assertRaises(ValueError, data.get_data_from_url, self.no_link)

    def test_get_data_from_url_valid_url(self):
        """Test function with valid url that contains no json at the beginning"""
        self.assertRaises(ValueError, data.get_data_from_url, self.random_link)

    def test_get_data_from_url_correct_link(self):
        """Test function with valid url containing JSON objects"""
        self.assertIsInstance(data.get_data_from_url(self.link), pd.DataFrame, "Should be Pandas Dataframe")


if __name__ == '__main__':
    unittest.main()
