# Corporate Email Generator

The Corporate Email Generator is a Python script that reads student data from a CSV file, creates unique corporate email addresses based on the student registration numbers, and saves the valid and duplicate email addresses to separate CSV files.

# Requirements
    Python 3.x

Usage
Clone the repository to your local machine:

Install the required dependencies:
    pip install csv


Prepare the CSV file with student data:

The CSV file should have the following columns: "Student Name," "Year," and "Reg No."
Each row in the CSV file should contain the student's full name, year, and registration number.
Example CSV format:


    StudentName,Year,Regno
    John Doe,2023,SMA/0001/23
    Jane Smith,2022,SMB/0002/22
    Run the Python script:

```bash
python corporate_email_generator.py
```

The script will generate unique corporate email addresses based on the student data and save them to two separate CSV files:

`unique_emails.csv`: Contains the unique corporate email addresses.
`duplicate_emails.csv`: Contains the duplicate corporate email addresses.
You can find the generated CSV files in the same directory as the Python script.


# Customization

By default, the script sets the year to `23` for each student if the "Year" field is not provided in the CSV file. You can modify this behavior by updating the default value in the Student class constructor.

The script removes the slashes from the "Reg No" field to create the email addresses. If your registration numbers have a different format, you can modify the email generation logic in the generate_unique_emails function.
