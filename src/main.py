'''
Assignment1
Submitted by Anvitha Hiriadka
Date: 01/17/2025

Dataset used : https://www.kaggle.com/datasets/shibumohapatra/house-price/data
'''
#Importing the required libraries
import pandas as pd
import numpy as np
import json


class HousePriceAnalysis:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = None

    """Loading the dataset from the given file path"""
    def load_data(self):
        print(f"Loading data from {self.data_file}...")
        self.df = pd.read_csv(self.data_file)
        print("Data loaded successfully.")

    """Clean the dataset by handling missing values and duplicates"""
    def clean_data(self):
        print("Cleaning data...")

        # Impute missing values in 'total_bedrooms' column with the median value
        median_bedrooms = self.df['total_bedrooms'].median()
        self.df['total_bedrooms'] = self.df['total_bedrooms'].replace(r'^\s*$', np.nan, regex=True)
        self.df['total_bedrooms'] = self.df['total_bedrooms'].fillna(median_bedrooms)

        # Removing any duplicate records
        duplicate_records = self.df.duplicated().sum()
        if duplicate_records > 0:
            print(f"Removing {duplicate_records} duplicate records...")
            self.df = self.df.drop_duplicates()

        print("Data cleaned successfully.")

    """Compute and return aggregate statistics."""
    def compute_aggregates(self):
        print("Computing aggregates...")

        # 1. Total number of house records
        total_houses = self.df.shape[0]

        # 2. Average house price
        average_price = self.df['median_house_value'].mean()

        # 3. Average rooms-to-household ratio
        self.df['rooms_to_household_ratio'] = self.df['total_rooms'] / self.df['households']
        average_rooms_to_household_ratio = self.df['rooms_to_household_ratio'].mean()

        # 4. Average population
        average_population = self.df['population'].mean()

        # 5. Median income distribution by ocean proximity
        median_income_by_proximity = self.df.groupby('ocean_proximity')['median_income'].median().to_dict()

        # 6. Maximum and minimum median house values
        max_house_value = self.df['median_house_value'].max()
        min_house_value = self.df['median_house_value'].min()

        # 7. Count of blocks by ocean proximity
        blocks_by_proximity = self.df['ocean_proximity'].value_counts().to_dict()

        # Aggregates dictionary
        aggregates = {
            "total_houses": total_houses,
            "average_house_price": average_price,
            "rooms-to-household_ratio": average_rooms_to_household_ratio,
            "average_population": average_population,
            "median_income_by_proximity": median_income_by_proximity,
            "max_house_value": int(max_house_value),
            "min_house_value": int(min_house_value),
            "blocks_by_proximity": blocks_by_proximity
        }

        print("Aggregates computed successfully.")
        return aggregates

    """Save the computed aggregates to a JSON file."""
    def save_aggregates(self, aggregates, output_file):
        print(f"Saving aggregates to {output_file}...")
        with open(output_file, 'w') as f:
            json.dump(aggregates, f, indent=4)
        print(f"Aggregates saved to {output_file}.")

    """Run the full analysis (load, clean, compute, and save aggregates)."""
    def run(self, output_file):
        self.load_data()
        self.clean_data()
        aggregates = self.compute_aggregates()
        self.save_aggregates(aggregates, output_file)


if __name__ == "__main__":
    data_file = 'src/1553768847-housing.csv'
    output_file = 'src/house_price_aggregates.json'
    # Create an instance of HousePriceAnalysis and run the analysis
    analysis = HousePriceAnalysis(data_file)
    analysis.run(output_file)
