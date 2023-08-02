import csv

class Student:
    def __init__(self, full_name, year=23, reg_no=""):
        self.full_name = full_name
        self.year = year
        self.reg_no = reg_no

    def generate_email(self, corporate_domain:str ="student.kibu.ac.ke")->str:
        names = self.full_name.split()
        first_name = names[0].lower()
        last_name = names[-1].lower()
        reg_no_without_slashes = self.reg_no.replace("/", "")
        email = f"{reg_no_without_slashes}{self.year}@{corporate_domain}".lower()
        return email
    def get_first_name(self):
        return self.full_name.split()[0]

    def get_last_name(self):
        return self.full_name.split()[-1]

    def get_middle_name(self):
        names = self.full_name.split()
        return names[1].lower() if len(names) > 2 else ""

def generate_unique_emails(student_list, corporate_domain):
    email_map = {}
    unique_emails = []
    duplicate_emails = []

    for student in student_list:
        email = student.generate_email(corporate_domain)

        count = email_map.get(email, 0)
        while email in unique_emails:
            count += 1
            email = f"{email[:-2]}{count}@{corporate_domain}".lower()

        email_map[email] = count
        if email in unique_emails:
            duplicate_emails.append(email)
        else:
            unique_emails.append(email)

    return unique_emails, duplicate_emails

def main():
    csv_file = "stud.csv"
    student_list = []

    try:
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                full_name = row["StudentName"].strip()
                reg_no = row.get("Regno", "").strip()
                student_list.append(Student(full_name, reg_no= reg_no))

        corporate_domain = "student.kibu.ac.ke"
        unique_emails, duplicate_emails = generate_unique_emails(student_list, corporate_domain)

        with open("unique_emails.csv", "w", newline='') as unique_file:
            writer = csv.writer(unique_file)
            writer.writerow(["Email"])
            for email in unique_emails:
                writer.writerow([email])

        with open("duplicate_emails.csv", "w", newline='') as duplicate_file:
            writer = csv.writer(duplicate_file)
            writer.writerow(["Email"])
            for email in duplicate_emails:
                writer.writerow([email])

        with open("student_details.csv", "w", newline='') as student_details_file:
            writer = csv.writer(student_details_file)
            writer.writerow(["First Name", "Middle Name", "Last Name","EMail"])
            for student in student_list:
                first_name = student.get_first_name()
                middle_name = student.get_middle_name()
                last_name = student.get_last_name()
                email = student.generate_email(corporate_domain)
                writer.writerow([first_name, middle_name, last_name,email])

        print("Valid emails written to unique_emails.csv")
        print("Duplicate emails written to duplicate_emails.csv")
        print("Student details written to student_details.csv")

    except Exception as e:
        print(f"Error reading CSV file: {e}")

if __name__ == "__main__":
    main()
