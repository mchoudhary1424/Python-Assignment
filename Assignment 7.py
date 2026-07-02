import csv
import os

# --- 1. Create text file with session topics ---
topics = ["File Handling", "CSV Module", "List Operations", "Menu-Driven Programs"]
with open("session_topics.txt", "w") as txt_file:
    for topic in topics:
        txt_file.write(topic + "\n")


# --- 2. Address Book Program ---
CSV_FILE = "address_book.csv"

# Initialize CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Mobile", "Email"])

while True:
    print("\n--- ADDRESS BOOK MENU ---")
    print("1. Add Contact Details")
    print("2. View Contacts")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ").strip()
    
    if choice == "1":
        name = input("Enter Name: ").strip()
        mobile = input("Enter Mobile: ").strip()
        email = input("Enter Email: ").strip()
        
        contact_data = [name, mobile, email]
        
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(contact_data)
        print("Contact added successfully!")
        
    elif choice == "2":
        print("\n--- Saved Contacts ---")
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, "r") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                
                contacts = list(reader)
                if not contacts:
                    print("No contacts found.")
                else:
                    for row in contacts:
                        print(f"Name: {row[0]} | Mobile: {row[1]} | Email: {row[2]}")
        else:
            print("No contacts found.")
            
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
