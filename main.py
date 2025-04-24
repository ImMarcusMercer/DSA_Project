import csv

class CSVManager:
    """Complete this class"""
    def __init__(self, filename='storage.csv'):
        self.filename = filename

    def addValue(self, value):
        """Complete this method
        Receive value(user input) and store into csv file"""
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([value])

    def showAll(self):
        """Complete this method
        Show all values in storage in a numbered format"""
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)
                if not data:
                    print("No data found.")
                    return
                for idx, row in enumerate(data, start=1):
                    print(f"{idx}. {row[0]}")
        except FileNotFoundError:
            print("No data found.")
            return

if __name__=="__main__":
    manager= CSVManager()
    while True:
        print("\nOptions:")
        print("1. Add a value")
        print("2. Show all values")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            value = input("Enter a value to store: ")
            manager.addValue(value)
            print("Value added.")
        elif choice == '2':
            print("Stored values:")
            manager.showAll()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
