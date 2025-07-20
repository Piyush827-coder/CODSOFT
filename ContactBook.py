# Simple Contact Book

contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added.\n")

def view_contacts():
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    key = input("Search name/phone: ").lower()
    for c in contacts:
        if key in c['name'].lower() or key in c['phone']:
            print(f"Found: {c['name']}, {c['phone']}, {c['email']}, {c['address']}")

def delete_contact():
    view_contacts()
    i = int(input("Enter number to delete: ")) - 1
    if 0 <= i < len(contacts):
        removed = contacts.pop(i)
        print(f"Deleted {removed['name']}.")

while True:
    print("\n1.Add  2.View  3.Search  4.Delete  5.Exit")
    ch = input("Choose: ")
    if ch == '1': add_contact()
    elif ch == '2': view_contacts()
    elif ch == '3': search_contact()
    elif ch == '4': delete_contact()
    elif ch == '5': break
    else: print("Invalid choice.")
