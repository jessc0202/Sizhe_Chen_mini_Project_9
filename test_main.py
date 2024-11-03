import unittest
import pandas as pd
from main import main
from mylib.lib import (load_and_preprocess, 
                       calculate_basic_stats, 
                       get_top_countries_by_alcohol)

class TestMain(unittest.TestCase):
    def setUp(self):
        # Setup a sample dataframe to use in tests
        self.csv_url = (
    "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/"
    "master/alcohol-consumption/drinks.csv")
        self.df = load_and_preprocess(self.csv_url)

    def test_main_execution(self):
        # Check if the main function runs without errors
        try:
            main()
            main_executed = True
        except Exception as e:
            main_executed = False
            print("Error in main:", e)
        
        self.assertTrue(main_executed, 
                        "The main function did not execute successfully.")
    
    def test_load_and_preprocess(self):
        # Test if the data loads and renames columns correctly
        self.assertIn("beer", self.df.columns, 
                      "Column renaming failed for 'beer'")
        self.assertIn("spirits", self.df.columns, 
                      "Column renaming failed for 'spirits'")
    
    def test_calculate_basic_stats(self):
        stats = calculate_basic_stats(self.df)
        self.assertIsInstance(stats, pd.DataFrame, 
                              "Basic statistics are not returned as a DataFrame")
        self.assertIn("mean", stats.index,
                       "Statistics should include a mean value")
    
    def test_get_top_countries_by_alcohol(self):
        # Test if the function retrieves the correct top N countries
        top_5 = get_top_countries_by_alcohol(self.df, 5)
        self.assertEqual(len(top_5), 5, 
                         "Top N countries should return 5 rows")
        self.assertIn("country", top_5.columns, 
                      "Top countries DataFrame should include 'country' column")

if __name__ == "__main__":
    unittest.main()
