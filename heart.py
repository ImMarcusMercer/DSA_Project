import csv
def write_to_csv(data):
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data])

def display_data():
    try:
        with open('data.csv', mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
            if data:
                print("Stored Data:")
                for index, row in enumerate(data, start=1):
                    print(f"{index}. {row[0]}")
            else:
                print("No data found.")
    except FileNotFoundError:
        print("No data file found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Enter data")
        print("2. Display stored data")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            user_input = input("Enter some data: ")
            write_to_csv(user_input)
        elif choice == '2':
            display_data()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

