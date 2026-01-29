# Import a powerful tool called "pandas" that you'll use to work with and organize data easily
import pandas as pd
import os 

file_name = 'grocery_list.csv'

if os.path.exists(file_name):
    # Load the grocery list from the CSV file
    grocery_list_df = pd.read_csv(file_name)

    # Extract the items from the DataFrame and store them in a list
    grocery_list = grocery_list_df['item'].tolist()

    # Print the grocery list and inspect the output
    print(grocery_list)
else:
    print(f"Error: The file '{file_name}' was not found in the current directory.")
    print("Please ensure you have followed the instructions on the Coursera site to extract the files from the zip archive.")