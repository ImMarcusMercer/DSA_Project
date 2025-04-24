import csv
import os
from datetime import datetime

class CSVManager:
    ENROLLMENT_FILE = "enrollments.csv"
    FIELDS = ["First Name", "Last Name", "Age", "Email", "Course", "Enrollment Date"]

    @staticmethod
    def addValue(value):
        """Receive value (user input) and store into CSV file."""
        try:
            file_exists = os.path.isfile(CSVManager.ENROLLMENT_FILE)
            with open(CSVManager.ENROLLMENT_FILE, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=CSVManager.FIELDS)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(value)
            print("Value successfully added to CSV.")
        except Exception as e:
            print(f"Error saving value: {str(e)}")

    @staticmethod
    def showAll():
        """Show all values in storage in a numbered format."""
        try:
            if not os.path.isfile(CSVManager.ENROLLMENT_FILE):
                print("No records found.")
                return

            with open(CSVManager.ENROLLMENT_FILE, 'r') as file:
                reader = csv.DictReader(file)
                records = list(reader)

                if not records:
                    print("No records found.")
                    return

                print(f"{'No.':<5} {'First Name':<15} {'Last Name':<15} {'Age':<5} {'Email':<25} {'Course':<15} {'Enrollment Date':<20}")
                print("-" * 100)
                for idx, record in enumerate(records, 1):
                    print(f"{idx:<5} {record.get('First Name', 'N/A'):<15} {record.get('Last Name', 'N/A'):<15} {record.get('Age', 'N/A'):<5} {record.get('Email', 'N/A'):<25} {record.get('Course', 'N/A'):<15} {record.get('Enrollment Date', 'N/A'):<20}")
        except Exception as e:
            print(f"Error reading records: {str(e)}")

if __name__ == "__main__":
    manager = CSVManager()

    while True:
        print("\n1. Add Value")
        print("2. Show All Values")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Collect user input for a new record
            value = {
                "First Name": input("First Name: ").strip().title(),
                "Last Name": input("Last Name: ").strip().title(),
                "Age": input("Age: ").strip(),
                "Email": input("Email: ").strip().lower(),
                "Course": input("Course: ").strip().title(),
                "Enrollment Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Automatically set the current date and time
            }
            manager.addValue(value)
        elif choice == '2':
            manager.showAll()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
