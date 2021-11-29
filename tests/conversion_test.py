import unittest
from convert import Convert
import pandas as pd
import pandas.testing as pd_testing


class ConversionTest(unittest.TestCase):

    def setUp(self) -> None:
        """Setup a converter to be used by other classes"""
        self.convert = Convert()
        dic = {'visitor_country': ['AL', 'AF', 'IN']}
        # Add test dataframe
        self.before_map_country = pd.DataFrame.from_dict(dic)
        # Add custom assertion to runtime
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataFrameEqual)

    def assertDataFrameEqual(self, a, b, msg):
        """Create assert method to compare dataframes"""
        try:
            pd_testing.assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def test_country_to_continent_one(self):
        """Test country code to continent conversion with valid input"""
        self.assertEqual(self.convert.to_continent_code('AF'), 'AS', 'Should be AS')

    def test_country_to_continent_two(self):
        """Test country code to continent conversion with invalid input"""
        self.assertRaises(KeyError, self.convert.to_continent_code, 'abcd')

    def test_country_to_continent_three(self):
        """Test country code to continent conversion with valid but unrecognized input"""
        self.assertRaises(KeyError, self.convert.to_continent_code, 'xx')

    def test_continent_name_one(self):
        """Test continent code to full name with valid input"""
        self.assertEqual(self.convert.to_continent_name('EU'), 'Europe', 'Should be Europe')

    def test_continent_name_two(self):
        """Test continent code to full name with invalid input"""
        self.assertRaises(KeyError, self.convert.to_continent_name, 'XYZ')

    def test_continent_name_three(self):
        """Test continent code to full name with valid but unrecognized input"""
        self.assertRaises(KeyError, self.convert.to_continent_name, 'XX')

    def test_map_to_continent_code(self):
        """Test mapping of continent names to entire dataframe column"""
        continent_code = self.convert.map_to_continent_code(self.before_map_country)
        data = {'index': [0, 1, 2], 'visitor_country': ['Europe', 'Asia', 'Asia']}
        expected_df = pd.DataFrame.from_dict(data)
        self.assertDataFrameEqual(continent_code, expected_df,
                                  "visitor_country should be 'EU', 'AS', 'AS'")


if __name__ == '__main__':
    unittest.main()
