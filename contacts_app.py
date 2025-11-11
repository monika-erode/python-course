
# ----------------------------
# GLOBAL VARIABLES
# ----------------------------
contacts = {}  # Using dictionary to store contacts (name → phone)

# ----------------------------
# FUNCTION DEFINITIONS
# ----------------------------

def display_menu():
    """Displays available options"""
    print("\n===== CONTACTS APP =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save & Exit")
    print("========================")

def add_contact():
    """Adds a new contact"""
    name = input("Enter contact name: ").strip().title()
    phone = input("Enter phone number: ").strip()

    # ✅ Example of Error Handling
    if not phone.isdigit():
        print("❌ Invalid phone number! Must contain digits only.")
        return

    # ✅ Using dictionary to store data
    contacts[name] = phone
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    """Displays all saved contacts"""
    if not contacts:
        print("📭 No contacts available.")
        return
    
    print("\n--- Contact List ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contact():
    """Search contact by name"""
    search = input("Enter name to search: ").strip().title()
    # ✅ Control structure - if/else
    if search in contacts:
        print(f"🔍 Found: {search} - {contacts[search]}")
    else:
        print("❌ Contact not found!")

def update_contact():
    """Update an existing contact"""
    name = input("Enter name to update: ").strip().title()
    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()
        if new_phone.isdigit():
            contacts[name] = new_phone
            print("✅ Contact updated successfully!")
        else:
            print("❌ Invalid phone number.")
    else:
        print("❌ Contact not found!")

def delete_contact():
    """Delete a contact"""
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"🗑️  Contact '{name}' deleted.")
    else:
        print("❌ Contact not found!")

def save_contacts():
    """Save contacts to file"""
    try:
        with open("contacts.txt", "w") as f:
            for name, phone in contacts.items():
                f.write(f"{name}:{phone}\n")
        print("💾 Contacts saved to file successfully!")
    except Exception as e:
        print(f"⚠️ Error saving contacts: {e}")

def load_contacts():
    """Load contacts from file at startup"""
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone = line.strip().split(":")
                contacts[name] = phone
    except FileNotFoundError:
        # ✅ Error handling if file doesn’t exist
        print("ℹ️ No previous contacts found, starting fresh!")

# ----------------------------
# 4️⃣ MAIN PROGRAM LOOP
# ----------------------------
def main():
    load_contacts()  # Load contacts at startup

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        # ✅ Control structures - if/elif/else
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            save_contacts()
            print("👋 Exiting Contacts App. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number from 1 to 6.")

# ----------------------------
# 5️⃣ ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    main()
