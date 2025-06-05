import pandas as pd
import os

# Validate file paths
file1_path = r"ExamResult_Simulated.xlsx"
file2_path = r"StudentInfo_Simulated.xlsx"

# Check if files exist
if not os.path.exists(file1_path) or not os.path.exists(file2_path):
    raise FileNotFoundError("One or both Excel files not found")

# Read the Excel files with validation
try:
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)
    
    # Validate required columns exist
    required_cols_df1 = ['Login', 'Mark(10)']
    required_cols_df2 = ['RollNumber']
    
    if not all(col in df1.columns for col in required_cols_df1):
        raise ValueError(f"Missing required columns in ExamResult file: {required_cols_df1}")
    if not all(col in df2.columns for col in required_cols_df2):
        raise ValueError(f"Missing required columns in StudentInfo file: {required_cols_df2}")
        
    # Check if Mark column already exists in df2
    if 'Mark' in df2.columns:
        print("Warning: Mark column already exists in StudentInfo file. Skipping mapping.")
    else:
        # Add Mark column directly to df2
        df2['Mark'] = df2['RollNumber'].map(df1.set_index('Login')['Mark(10)'])
        # Save the updated df2 back to Excel
        df2.to_excel(file2_path, index=False)
        print("Update completed successfully")
    
except Exception as e:
    print(f"Error occurred: {str(e)}")