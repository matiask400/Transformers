import pandas as pd
import os

def convert_text_to_numbers(df):
    """Convert all text cells that represent numbers to numeric values."""
    for column in df.columns:
        try:
            df[column] = pd.to_numeric(df[column], errors='coerce')
        except Exception as e:
            pass            
    return df

for i in range(2):
    # Path to the folder containing the CSV files
    input_folder = f'test_dataset/process_data/results2/temperature-{i}'  # Change this path to the location of your folder
    output_folder = 'test_dataset/process_data/excel'  # Change this path to the location where you want to save the Excel files

    # Ensure that the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            # Build the full path of the CSV file
            csv_file_path = os.path.join(input_folder, filename)
            
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(csv_file_path)
            
            # Convert text to numbers
            df = convert_text_to_numbers(df)
            
            # Build the Excel filename with the 'temperature-0_' prefix
            excel_filename = f'temperature-{i}_' + filename.replace('.csv', '.xlsx')
            excel_file_path = os.path.join(output_folder, excel_filename)
            
            # Save the DataFrame to an Excel file
            df.to_excel(excel_file_path, index=False, engine='openpyxl')
            
            print(f'Converted: {filename} to {excel_filename}')

print('Conversion completed.')
