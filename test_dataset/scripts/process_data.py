import csv
import os

def process_leetcode_csv(input_filename, output_filename):
    """
    Process a CSV file containing LeetCode problem data and extract relevant information.

    This function reads the input CSV file, extracts the problem ID and description, 
    and saves the processed data into a new CSV file.

    Parameters:
    input_filename (str): Path to the input CSV file containing raw LeetCode problems.
    output_filename (str): Path where the processed CSV file will be saved.

    Returns:
    None
    """
    problems = []  # List to store problems as dictionaries

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    try:
        # Read data from the input CSV file
        with open(input_filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            # Skip the header if present
            next(csv_reader, None)
            
            # Process each row in the CSV file
            for fields in csv_reader:
                if len(fields) < 3:
                    continue  # Skip incomplete rows
                
                # Create a dictionary for the problem
                problem = {
                    "ID": fields[0],
                    "Description": fields[2],
                }
                
                # Add the problem dictionary to the list
                problems.append(problem)
        
        # Write data to the output CSV file
        with open(output_filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["ID", "Description"])
            
            # Write headers
            writer.writeheader()
            
            # Write rows of data
            writer.writerows(problems)

        print(f"CSV file '{output_filename}' generated successfully.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the script
if __name__ == "__main__":
    process_leetcode_csv(
        input_filename=r"test_dataset/data/raw/leetcode_problems.csv",
        output_filename=r"test_dataset/data/processed/leetcode_problems_processed_data.csv"
    )
