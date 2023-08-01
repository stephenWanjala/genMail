import csv

class Student:
    def __init__(self, full_name, year):
        self.full_name = full_name
        self.year = year

def generate_unique_emails(student_list, corporate_domain):
    email_map = {}
    unique_emails = []
    duplicate_emails = []

    for student in student_list:
        names = student.full_name.split()
        first_name = names[0].lower()
        last_name = names[-1].lower()
        middle_name = names[1].lower() if len(names) > 2 else ""

        if len(middle_name) > 1:
            email = f"{middle_name}{first_name}{student.year}@{corporate_domain}"
        elif middle_name:
            email = f"{middle_name}{last_name}{student.year}@{corporate_domain}"
        else:
            email = f"{first_name}{last_name}{student.year}@{corporate_domain}"

        count = email_map.get(email, 0)
        while email in unique_emails:
            count += 1
            email = f"{email[:-2]}{count}@{corporate_domain}"

        email_map[email] = count
        if email in unique_emails:
            duplicate_emails.append(email)
        else:
            unique_emails.append(email)

    return unique_emails, duplicate_emails

def main():
    csv_file = "students.csv"
    student_list = []

    try:
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                full_name = row["StudentName"].strip()
                year = 23
                student_list.append(Student(full_name, year))

        corporate_domain = "kibu.ac.ke"
        unique_emails, duplicate_emails = generate_unique_emails(student_list, corporate_domain)

        with open("unique_emails.txt", "w") as unique_file:
            for email in unique_emails:
                unique_file.write(f"{email}\n")

        with open("duplicate_emails.txt", "w") as duplicate_file:
            for email in duplicate_emails:
                duplicate_file.write(f"{email}\n")

        print("Valid emails written to unique_emails.txt")
        print("Duplicate emails written to duplicate_emails.txt")

    except Exception as e:
        print(f"Error reading CSV file: {e}")

if __name__ == "__main__":
    main()
