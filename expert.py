# Expert System for Information Management

database = {}

def add_record():
    name = input("Enter Name: ")
    info = input("Enter Information: ")

    database[name] = info

    print("Record added successfully!")

def search_record():
    name = input("Enter Name to Search: ")

    if name in database:
        print("Information:", database[name])
    else:
        print("Record not found!")

def display_records():

    if len(database) == 0:
        print("No records available.")

    else:
        print("\nStored Records:")

        for name, info in database.items():
            print(name, ":", info)

while True:

    print("\n====== Information Management Expert System ======")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Display All Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_record()

    elif choice == '2':
        search_record()

    elif choice == '3':
        display_records()

    elif choice == '4':
        print("Exiting System...")
        break

    else:
        print("Invalid Choice!")