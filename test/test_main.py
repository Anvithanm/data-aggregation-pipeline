'''
Assignment1 - Unit test cases for the main code snippet
Submitted by Anvitha Hiriadka
Date: 01/18/2025
'''

#Importing the required libraries
import unittest
import pandas as pd
import numpy as np
import os
import json

# Add the 'src' folder to the Python path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the HousePriceAnalysis class from main.py
from main import HousePriceAnalysis

class TestMain(unittest.TestCase):
    def setUp(self):
        """Set up a sample dataset for testing."""
        self.sample_data = pd.DataFrame({
            "total_rooms": [6, 10, 20],
            "households": [2, 5, 4],
            "population": [50, 100, 150],
            "median_house_value": [200000, 300000, 250000],
            "ocean_proximity": ["NEAR BAY", "INLAND", "NEAR BAY"],
            "median_income": [4.5, 3.2, 5.1],
            "total_bedrooms": [3, np.nan, 8]
        })
        self.output_file = "test_aggregates.json"

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    """Test Case to test if data is loaded correctly."""
    def test_load_data(self):
        filepath = 'test.csv'
        self.sample_data.to_csv(filepath, index=False)

        # Create an instance of HousePriceAnalysis
        analysis = HousePriceAnalysis(filepath)
        analysis.load_data()
        
        # Check if data is loaded correctly
        self.assertEqual(analysis.df.shape, self.sample_data.shape)

    """Test Case to check if missing values and duplicates are handled correctly"""
    def test_clean_data(self):
        # Create an instance of HousePriceAnalysis
        analysis = HousePriceAnalysis(None)
        # Directly set the dataframe
        analysis.df = self.sample_data  
        
        # Clean the data
        analysis.clean_data()

        # Test that NaN in 'total_bedrooms' is replaced with median
        median_bedrooms = self.sample_data['total_bedrooms'].median()
        self.assertEqual(analysis.df['total_bedrooms'].iloc[1], median_bedrooms)

        # Test that no duplicates are present
        self.assertEqual(analysis.df.duplicated().sum(), 0)

    """Test Case to check if aggregates are computed correctly"""
    def test_compute_aggregates(self):
        # Create an instance of HousePriceAnalysis
        analysis = HousePriceAnalysis(None)
        # Directly set the dataframe
        analysis.df = self.sample_data  
        
        # Clean the data
        analysis.clean_data()
        
        # Compute aggregates
        aggregates = analysis.compute_aggregates()

        # Total houses
        self.assertEqual(aggregates["total_houses"], 3)

        # Average house price
        expected_avg_price = self.sample_data["median_house_value"].mean()
        self.assertEqual(aggregates["average_house_price"], expected_avg_price)

        # Rooms-to-household ratio
        self.sample_data['rooms_to_household_ratio'] = self.sample_data['total_rooms'] / self.sample_data['households']
        expected_ratio = self.sample_data['rooms_to_household_ratio'].mean()
        self.assertAlmostEqual(aggregates["rooms-to-household_ratio"], expected_ratio, places=2)

        # Average population
        expected_population = self.sample_data["population"].mean()
        self.assertEqual(aggregates["average_population"], expected_population)

        # Median income by proximity
        expected_income_by_proximity = self.sample_data.groupby("ocean_proximity")["median_income"].median().to_dict()
        self.assertEqual(aggregates["median_income_by_proximity"], expected_income_by_proximity)

        # Maximum and minimum house values
        self.assertEqual(aggregates["max_house_value"], int(self.sample_data["median_house_value"].max()))
        self.assertEqual(aggregates["min_house_value"], int(self.sample_data["median_house_value"].min()))

        # Count of blocks by proximity
        expected_blocks_by_proximity = self.sample_data["ocean_proximity"].value_counts().to_dict()
        self.assertEqual(aggregates["blocks_by_proximity"], expected_blocks_by_proximity)

    """Test Case to check if aggregates are saved correctly to a JSON file"""
    def test_save_aggregates(self):
        # Create an instance of HousePriceAnalysis
        analysis = HousePriceAnalysis(None)
        # Directly set the dataframe
        analysis.df = self.sample_data
        
        # Cleaning the data
        analysis.clean_data()
        
        # Computing aggregates
        aggregates = analysis.compute_aggregates()

        # Saving aggregates
        analysis.save_aggregates(aggregates, self.output_file)

        # Verifying the file exists
        self.assertTrue(os.path.exists(self.output_file))

        # Verifying file content
        with open(self.output_file, 'r') as f:
            saved_data = json.load(f)
            self.assertEqual(saved_data, aggregates)

if __name__ == "__main__":
    unittest.main()
