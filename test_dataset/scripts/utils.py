import pandas as pd
import os

def convert_text_to_numbers(df):
    """
    Convert all text-based numeric representations in a DataFrame to actual numeric values.

    This function iterates over each column of the given DataFrame and attempts to convert
    values to numeric types. If conversion is not possible, the value is replaced with NaN.

    Parameters:
    df (pd.DataFrame): Input DataFrame with potential text-based numbers.

    Returns:
    pd.DataFrame: DataFrame with converted numeric values where applicable.
    """
    for column in df.columns:
        try:
            df[column] = pd.to_numeric(df[column], errors='coerce')
        except Exception:
            pass  # If an error occurs, keep the original values
    return df

def convert_csv_to_excel(input_base_folder, output_folder, temperature_range=(0, 1)):
    """
    Convert all CSV files in the specified input folder to Excel format.

    This function processes CSV files stored in subdirectories corresponding to different 
    temperature categories (e.g., temperature-0, temperature-1). It ensures numerical values 
    are correctly formatted and saves the processed data as Excel files in the designated output folder.

    Parameters:
    input_base_folder (str): The base path where CSV files are stored.
    output_folder (str): The path where converted Excel files will be saved.
    temperature_range (tuple): The range of temperature categories to process.

    Returns:
    None
    """
    os.makedirs(output_folder, exist_ok=True)  # Ensure the output directory exists

    for i in range(temperature_range[0], temperature_range[1] + 1):
        input_folder = os.path.join(input_base_folder, f'temperature-{i}')
        
        if not os.path.exists(input_folder):
            print(f"Warning: Input folder '{input_folder}' does not exist. Skipping...")
            continue  # Skip if the folder does not exist

        # Process each CSV file in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith('.csv'):
                csv_file_path = os.path.join(input_folder, filename)
                
                # Load the CSV file into a DataFrame
                df = pd.read_csv(csv_file_path)
                
                # Convert text-based numbers to numeric values
                df = convert_text_to_numbers(df)
                
                # Generate the corresponding Excel filename with temperature prefix
                excel_filename = f'temperature-{i}_' + filename.replace('.csv', '.xlsx')
                excel_file_path = os.path.join(output_folder, excel_filename)
                
                # Save the DataFrame to an Excel file
                df.to_excel(excel_file_path, index=False, engine='openpyxl')
                
                print(f'Converted: {filename} → {excel_filename}')

    print('Conversion completed.')

# Execute the script
if __name__ == "__main__":
    convert_csv_to_excel(
        input_base_folder=r"test_dataset/outputs/visualizations/csv/results2",
        output_folder=r"test_dataset/outputs/visualizations/excel/results2",
        temperature_range=(0, 1)
    )
