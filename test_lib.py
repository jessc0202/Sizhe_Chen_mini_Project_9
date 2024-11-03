import unittest
from mylib.lib import (
    load_and_preprocess,
    calculate_basic_stats,
    get_top_countries_by_alcohol,
    compute_correlation_matrix,
    classify_and_count_categories,
)

class TestLib(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the sample data only once for all tests
        cls.csv_url = ("https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/"
                       "master/alcohol-consumption/drinks.csv")
        cls.df = load_and_preprocess(cls.csv_url)

    def test_load_and_preprocess(self):
        # Test that the data loads and columns are renamed correctly
        self.assertIn("beer", self.df.columns)
        self.assertIn("spirits", self.df.columns)
        self.assertEqual(self.df.shape[1], 6, 
                         "The DataFrame should have 6 columns after renaming")

    def test_calculate_basic_stats(self):
        # Check if statistics for 'beer' column include 'mean' and 'std'
        stats = calculate_basic_stats(self.df)
        self.assertIn("mean", stats.index)
        self.assertIn("std", stats.index)

    def test_get_top_countries_by_alcohol(self):
        # Ensure that it returns the specified number of top countries
        top_countries = get_top_countries_by_alcohol(self.df, 5)
        self.assertEqual(len(top_countries), 5, "Should return 5 top countries")
        self.assertIn("total_alcohol", top_countries.columns)

    def test_compute_correlation_matrix(self):
        # Verify that the correlation matrix has correct dimensions and values
        corr_matrix = compute_correlation_matrix(self.df)
        self.assertEqual(corr_matrix.shape, (4, 4), 
                         "Correlation matrix should be 4x4")
        self.assertTrue((corr_matrix >= -1).all().all() 
                        and (corr_matrix <= 1).all().all(), 
                        "Correlation values should be between -1 and 1")

    def test_classify_and_count_categories(self):
        # Check if consumption categories are correctly classified
        classified_df = classify_and_count_categories(self.df)
        self.assertIn("consumption_category", classified_df.columns, 
                      "Consumption category column missing")
        self.assertTrue(classified_df['consumption_category'].
                        isin(['Low', 'Moderate', 'High']).
                        all(), "Invalid category labels")

if __name__ == "__main__":
    unittest.main()