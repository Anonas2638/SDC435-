
# Name: Anosha Naseri
# Date: 11/12/2026
# Course: SDC435
# Assignment: 1.8 Performance Assessment
# Title: Python Application Accessing a Key-Value Database
# Purpose: Manage Redis sets using an interactive CRUD menu.

import redis

# Connect to the local Redis database
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# CREATE: Add a new set to the database
def create_set():
    key = input("Enter the key you wish to add: ")
    count = int(input("Enter how many members this set will have: "))

    for i in range(count):
        member = input("Enter the next member value: ")
        r.sadd(key, member)

    print("Set created successfully!")

# READ: Retrieve members of a specific set
def read_set():
    key = input("Enter the key of the set: ")
    members = r.smembers(key)

    print("Set members:", members)
    print("Cardinality:", r.scard(key))

# UPDATE: Add, remove, or remove all members
def update_set():
    key = input("Enter the key of the set you wish to update: ")

    print("1. Add new member")
    print("2. Remove member")
    print("3. Remove all members")
    print("4. Exit Update Menu")

    choice = input("Choose an option: ")

    if choice == "1":
        member = input("Enter the new member: ")
        r.sadd(key, member)
        print("Member added!")

    elif choice == "2":
        member = input("Enter the member to remove: ")
        r.srem(key, member)
        print("Member removed!")

    elif choice == "3":
        print("Removing all set members...")
        while r.scard(key) > 0:
            member = r.spop(key)
            print("Removing Member:", member)

        print("The cardinality of the set is now:", r.scard(key))

    elif choice == "4":
        return

    else:
        print("Invalid option!")

# DELETE: Remove a specific set
def delete_set():
    key = input("Enter the key of the set to delete: ")
    r.delete(key)
    print("Set deleted!")

# DELETE: Remove all database records
def delete_all():
    confirm = input("Delete all database data? (yes/no): ")

    if confirm.lower() == "yes":
        r.flushdb()
        print("All data removed!")
    else:
        print("Operation canceled.")

# Display the interactive application menu
def main():
    while True:
        print("\nType in a number and press enter to execute the menu option.")
        print("1. Query for set members")
        print("2. Add a new set")
        print("3. Update members of a set")
        print("4. Delete a set")
        print("5. Delete all data from the database")
        print("6. Exit the program")

        choice = input("Enter your choice: ")

        if choice == "1":
            read_set()
        elif choice == "2":
            create_set()
        elif choice == "3":
            update_set()
        elif choice == "4":
            delete_set()
        elif choice == "5":
            delete_all()
        elif choice == "6":
            print("Program has ended!")
            break
        else:
            print("Invalid option. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
