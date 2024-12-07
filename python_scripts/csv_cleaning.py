import pandas as pd

# Load the CSV file
file_path = 'your.csv'  # Replace with the path to your file

data = pd.read_csv(file_path)


def split_text_blocks(data):

    processed_rows = []

    # Iterate through each row in the DataFrame
    for _, row in data.iterrows():

        table_name = row['Table Name']
        dq_issues = row['DQ Issues']
        
        # Split the 'DQ Issues' by new line if it's not NaN
        if pd.notna(dq_issues):
            split_issues = dq_issues.split('\n')
        else:
            split_issues = [dq_issues]  # Keep NaN as is
        
        # Append each part as a new row with the same 'Table Name'
        for issue in split_issues:
            processed_rows.append({'Table Name': table_name, 'DQ Issues': issue})
    
    # Create a new DataFrame from the processed rows
    processed_df = pd.DataFrame(processed_rows)
    return processed_df


# Apply the function to the loaded data
processed_data = split_text_blocks(data)

# Save the processed data to a new CSV file
output_file_path = 'processed_file.csv'  # Replace with the desired output file path
processed_data.to_csv(output_file_path, index=False)

# Print a message indicating the process is complete
print(f"Processed data saved to {output_file_path}")
