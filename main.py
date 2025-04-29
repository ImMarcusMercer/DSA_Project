import csv

filename = "storage.csv"

class CSVManager:
    """Complete this class"""
    def addValue(self,name):
        """Complete this method
        Receive value(user input) and store into csv file"""
        file = open(filename, 'a', newline='')
        writer = csv.writer(file)
        writer.writerow([name])
        file.close()

    def showAll(self):
        """Complete this method
        Show all values in storage in a numbered format"""
        try:
            file = open(filename, 'r')
            reader = csv.reader(file)
            print("\nStored Names:")
            for i, row in enumerate(reader, start=1):
                print(f"{i}. {row[0]}")
            file.close()
        except FileNotFoundError:
            print("No data found. Please add names first.")

if __name__=="__main__":
    manager= CSVManager()
    while True:
        print("\n1. Add Value\n2. Show All\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            val = input("Enter value to add: ")
            manager.addValue(val)

        elif choice == '2':
            manager.showAll()

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
