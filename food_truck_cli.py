import pandas as pd
import argparse
import os

def load_data(filepath):
    #load data from file
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file at {filepath} does not exist.")
    return pd.read_csv(filepath)

def search_food_trucks(df, food_item):
   #search for food trucks based on cravings
    df['FoodItems'] = df['FoodItems'].fillna('')
    return df[df['FoodItems'].str.contains(food_item, case=False)]

def main():
    # Define the file path for the CSV
    filepath = 'C:/Users/khing/OneDrive/Desktop/python/Mobile_Food_Facility_Permit.csv'

    # Load data
    try:
        df = load_data(filepath)
    except FileNotFoundError as e:
        print(e)
        return

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Search for food trucks by food name")
    parser.add_argument('FoodItems', type=str, help="Food name to search for")
    args = parser.parse_args()

    # Search for the food trucks
    food_search = search_food_trucks(df, args.FoodItems)

    # Sort alphabetically by applicant
    food_search_sorted = food_search.sort_values(by='Applicant')

    # Display results
    if not food_search_sorted.empty:
        for idx, row in food_search_sorted.iterrows():
            print(f"{row['Applicant']} - {row['LocationDescription']}")
    else:
        print(f"Food truck not available: {args.FoodItems}")

if __name__ == "__main__":
    main()
