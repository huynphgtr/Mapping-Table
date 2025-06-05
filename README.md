# Excel Mark Mapping Tool

A Python script to map examination marks from one Excel file to another based on student identifiers.

## Description

This tool takes two Excel files:
- `ExamResult_Simulated.xlsx`: Contains student login IDs and their marks
- `StudentInfo_Simulated.xlsx`: Contains student roll numbers

The script maps marks from the exam results file to the student info file using the Login/RollNumber as the matching key.

## Requirements

- Python 3.x
- Required Python packages:
  ```
  pandas
  openpyxl
  ```

## File Requirements

### ExamResult_Simulated.xlsx
Must contain these columns:
- `Login`: Student login identifiers
- `Mark(10)`: Examination marks

### StudentInfo_Simulated.xlsx
Must contain this column:
- `RollNumber`: Student roll numbers

## Usage

1. Place both Excel files in the same directory as the script
2. Run the script:
   ```bash
   python main.py
   ```

## Output

The script will:
- Add a new 'Mark' column to `StudentInfo_Simulated.xlsx`
- Map the marks from `ExamResult_Simulated.xlsx` to corresponding students
- Save the updated information back to `StudentInfo_Simulated.xlsx`

## Error Handling

The script includes validation for:
- File existence
- Required columns
- Duplicate mark columns
