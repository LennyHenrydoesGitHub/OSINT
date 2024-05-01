# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 03:35:32 2024

@author: Neymat
"""

import pandas as pd

def read_country_codes(file_path):
    country_codes = []
    with open(file_path, 'r') as file:
        for line in file:
            country_codes.append(line.strip())
    return country_codes

file_path = 'CSI.txt'  # Replace 'country_codes.txt' with the path to your file
country_codes_list = read_country_codes(file_path)
print(country_codes_list)


def filter_csv_by_country_codes(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    print(df)
    # Extract the country codes from the first row
    country_codes = df.columns.tolist()
    
    # Remove the first element (as it's not a country code)
    first_column = country_codes.pop(0)
    notafrica = [line for line in country_codes_list if line not in country_codes]
    for afr in notafrica:
        df[afr] = 0
    
    print(notafrica)
    
    # Filter columns based on country codes
    df_filtered = df[[first_column] + country_codes_list]  # Keep the 'Country' column and the selected country code columns
    
    return df_filtered

def write_filtered_csv(filtered_df, output_file):
    # Write the filtered DataFrame to a new CSV file
    filtered_df.to_csv(output_file, index=False)


# Provide the path to your CSV file
csv_file_path = 'matrix_names-CSI.csv'
# Call the function to filter the CSV
filtered_df = filter_csv_by_country_codes(csv_file_path)

# Provide the path for the new filtered CSV file
output_csv_path = 'matrix_names-CSI.csv'

# Write the filtered DataFrame to the new CSV file
write_filtered_csv(filtered_df, output_csv_path)

print("Filtered CSV file has been created successfully!")




# Output the filtered DataFrame
print(filtered_df)