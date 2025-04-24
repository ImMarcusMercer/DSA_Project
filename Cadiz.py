import csv
import os

class CSVManager:
    """Manages CSV file operations like adding and displaying values."""
    FILE_NAME = 'entries.csv'

    def addValue(self, value):
        """Receive value (user input) and store it into a CSV file."""
        with open(self.FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([value])

    def showAll(self):
        """Show all values in storage in a numbered format."""
        if not os.path.exists(self.FILE_NAME):
            print("No data available.")
            return

        with open(self.FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("\nStored Values:")
            for index, row in enumerate(reader, start=1):
                print(f"{index}. {row[0]}")

if __name__ == "__main__":
    manager = CSVManager()

    while True:
        print("\n[1] Add Value")
        print("[2] Show All Values")
        print("[3] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            data = input("Enter a value to store: ")
            manager.addValue(data)
            print("Value added successfully.")
        elif choice == '2':
            manager.showAll()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")
