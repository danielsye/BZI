import os
import pandas as pd

def merge_files(directory_path, output_file):
    os.chdir(directory_path)
    """
    Merges all .csv and .xlsx files in the specified directory into a single output file.

    Args:
        directory_path (str): The path to the directory containing the .csv and .xlsx files.
        output_file (str): The name of the output file where the merged content will be saved.
    """
    if not os.path.isdir(directory_path):
        raise ValueError(f"The directory '{directory_path}' does not exist.")

    merged_content = []

    # Iterate through all files in the specified directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
            merged_content.append(df)
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(file_path)
            merged_content.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    if merged_content:
        merged_df = pd.concat(merged_content, ignore_index=True)
        # Save to output file based on its extension
        if output_file.endswith('.csv'):
            merged_df.to_csv(output_file, index=False)
        elif output_file.endswith('.xlsx'):
            merged_df.to_excel(output_file, index=False)
        else:
            raise ValueError("Output file must have a .csv or .xlsx extension.")
        
        print(f"Merged {len(merged_content)} files into '{output_file}' in '{directory_path}'.")
    else:
        print("No .csv or .xlsx files found in the specified directory.")
