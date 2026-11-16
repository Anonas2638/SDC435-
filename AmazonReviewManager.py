
# Name: Anosha Naseri
# Assignment: 2.5 Performance Assessment
# Date: November 16, 2026
# Title: Python Application Accessing a Document Database
# Purpose: Manage Amazon reviews using MongoDB CRUD operations.

import pymongo
import re

# Connect to the local MongoDB database
client = pymongo.MongoClient(
    "mongodb://localhost:27017/",
    serverSelectionTimeoutMS=5000
)
db = client["Amazon"]
collection = db["ReviewData"]


# CREATE: Add a new review document
def add_review():
    print("\n--- Add New Document ---")

    fields = [
        "review_id", "product_id", "reviewer_id",
        "stars", "review_body", "review_title",
        "language", "product_category"
    ]

    review = {}
    for field in fields:
        review[field] = input(f"Enter {field}: ").strip()

    collection.insert_one(review)
    print("Document added successfully!")


# READ: Retrieve one document using find_one()
def view_one():
    print("\n--- Retrieve One Document ---")
    review = collection.find_one()

    if review:
        print(review)
    else:
        print("No documents found.")


# READ: Search documents using find()
def search_reviews():
    while True:
        print("\n--- Query Documents ---")
        print("1. Filter for number of stars and greater")
        print("2. Filter for less than a number of stars")
        print("3. Filter for a word in the title")
        print("4. Filter for a word in the review body")
        print("5. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "5":
            break

        if choice in ("1", "2"):
            stars = input("Enter number of stars: ").strip()

            if not stars.isdigit():
                print("Please enter a valid number.")
                continue

            operator = "$gte" if choice == "1" else "$lt"

            # Imported dataset stores stars as strings
            query = {"stars": {operator: stars}}

        elif choice in ("3", "4"):
            word = input("Enter a word to search: ").strip()

            if not word:
                print("Please enter a search word.")
                continue

            field = (
                "review_title" if choice == "3"
                else "review_body"
            )

            query = {
                field: {
                    "$regex": re.escape(word),
                    "$options": "i"
                }
            }

        else:
            print("Invalid option.")
            continue

        results = collection.find(query).limit(5)
        found = False

        for review in results:
            print(review)
            found = True

        if not found:
            print("No matching reviews found.")


# UPDATE: Update a selected field in a review
def update_review():
    print("\n--- Update Document ---")

    review_id = input("Enter review_id to update: ").strip()
    review = collection.find_one({"review_id": review_id})

    if not review:
        print("Document not found.")
        return

    print("Current document:")
    print(review)

    allowed_fields = [
        "review_id", "product_id", "reviewer_id",
        "stars", "review_body", "review_title",
        "language", "product_category"
    ]

    field = input("Enter field to update: ").strip()

    if field not in allowed_fields:
        print("Invalid field name.")
        return

    value = input("Enter new value: ").strip()

    collection.update_one(
        {"_id": review["_id"]},
        {"$set": {field: value}}
    )

    print("Document updated successfully!")
    print(collection.find_one({"_id": review["_id"]}))


# DELETE: Remove a specific document by review_id
def delete_review():
    print("\n--- Delete Document ---")

    review_id = input("Enter review_id to delete: ").strip()
    result = collection.delete_one({"review_id": review_id})

    if result.deleted_count:
        print("Document deleted successfully!")
    else:
        print("Document not found.")


# DELETE: Remove all documents
def delete_all():
    print("\n--- Delete All Documents ---")
    confirm = input(
        "Type DELETE ALL to confirm: "
    )

    if confirm == "DELETE ALL":
        result = collection.delete_many({})
        print(result.deleted_count, "documents deleted.")
    else:
        print("Operation cancelled.")


# DELETE: Remove the entire collection
def delete_collection():
    print("\n--- Delete Collection ---")
    confirm = input(
        "Type DELETE COLLECTION to confirm: "
    )

    if confirm == "DELETE COLLECTION":
        collection.drop()
        print("Collection deleted successfully!")
    else:
        print("Operation cancelled.")


# MAIN MENU: Allow users to choose CRUD operations
def main():
    try:
        client.admin.command("ping")
        print("Connected to local MongoDB database!")
    except pymongo.errors.PyMongoError as error:
        print("MongoDB connection error:", error)
        return

    while True:
        print("\n--- AMAZON REVIEW MANAGER ---")
        print("1. Add a new document")
        print("2. Retrieve one document")
        print("3. Query documents")
        print("4. Update a document")
        print("5. Delete a document")
        print("6. Delete all documents from collection")
        print("7. Delete the collection")
        print("8. Exit program")

        choice = input("Choose an option (1-8): ").strip()

        try:
            if choice == "1":
                add_review()
            elif choice == "2":
                view_one()
            elif choice == "3":
                search_reviews()
            elif choice == "4":
                update_review()
            elif choice == "5":
                delete_review()
            elif choice == "6":
                delete_all()
            elif choice == "7":
                delete_collection()
            elif choice == "8":
                print("Program has ended!")
                break
            else:
                print("Invalid option. Try again.")
        except pymongo.errors.PyMongoError as error:
            print("Database error:", error)

    client.close()


if __name__ == "__main__":
    main()
