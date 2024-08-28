import tkinter as tk
from tkinter import messagebox

contacts = {}


def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "":
        messagebox.showerror("Error", "Please enter a name.")
        return

    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }

    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

    clear_entries()


def view_contact_list():
    if len(contacts) == 0:
        messagebox.showinfo("No Contacts", "No contacts found.")
        return

    contact_list = ""

    for name, details in contacts.items():
        contact_list += f"Name: {name}\n"
        contact_list += f"Phone Number: {details['phone_number']}\n"
        contact_list += f"Email: {details['email']}\n"
        contact_list += f"Address: {details['address']}\n\n"

    messagebox.showinfo("Contact List", contact_list)


def search_contact():
    query = search_entry.get().lower()

    results = []

    for name, details in contacts.items():
        if query in name.lower() or query in details['phone_number']:
            results.append((name, details))

    if len(results) == 0:
        messagebox.showinfo("No Results", "No matching contacts found.")
        return

    search_results = ""

    for result in results:
        name, details = result
        search_results += f"Name: {name}\n"
        search_results += f"Phone Number: {details['phone_number']}\n"
        search_results += f"Email: {details['email']}\n"
        search_results += f"Address: {details['address']}\n\n"

    messagebox.showinfo("Search Results", search_results)


def update_contact():
    name = update_name_entry.get()

    if name == "":
        messagebox.showerror("Error", "Please enter a name.")
        return

    if name not in contacts:
        messagebox.showerror("Error", "Contact not found.")
        return

    phone_number = update_phone_entry.get()
    email = update_email_entry.get()
    address = update_address_entry.get()

    if phone_number:
        contacts[name]['phone_number'] = phone_number
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")

    clear_update_entries()


def delete_contact():
    name = delete_name_entry.get()

    if name == "":
        messagebox.showerror("Error", "Please enter a name.")
        return

    if name not in contacts:
        messagebox.showerror("Error", "Contact not found.")
        return

    del contacts[name]

    messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")

    clear_delete_entries()


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def clear_update_entries():
    update_name_entry.delete(0, tk.END)
    update_phone_entry.delete(0, tk.END)
    update_email_entry.delete(0, tk.END)
    update_address_entry.delete(0, tk.END)


def clear_delete_entries():
    delete_name_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Management System")

# Add Contact
add_frame = tk.LabelFrame(root, text="Add Contact")
add_frame.pack(padx=10, pady=10)

name_label = tk.Label(add_frame, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(add_frame)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(add_frame, text="Phone Number:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(add_frame)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(add_frame, text="Email:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(add_frame)
email_entry.grid(row=2, column=1)

address_label = tk.Label(add_frame, text="Address:")
address_label.grid(row=3, column=0)
address_entry = tk.Entry(add_frame)
address_entry.grid(row=3, column=1)

add_button = tk.Button(add_frame, text="Add", command=add_contact)
add_button.grid(row=4, columnspan=2)

# View Contact List
view_button = tk.Button(root, text="View Contact List", command=view_contact_list)
view_button.pack(pady=(10, 5))

# Search Contact
search_frame = tk.LabelFrame(root, text="Search Contact")
search_frame.pack(padx=10)

search_label = tk.Label(search_frame, text="Search by Name or Phone Number:")
search_label.grid(row=0, columnspan=2)
search_entry = tk.Entry(search_frame)
search_entry.grid(row=1, columnspan=2)

search_button = tk.Button(search_frame, text="Search", command=search_contact)
search_button.grid(row=2, columnspan=2)

# Update Contact
update_frame = tk.LabelFrame(root, text="Update Contact")
update_frame.pack(padx=10, pady=10)

update_name_label = tk.Label(update_frame, text="Name:")
update_name_label.grid(row=0, column=0)
update_name_entry = tk.Entry(update_frame)
update_name_entry.grid(row=0, column=1)

update_phone_label = tk.Label(update_frame, text="Phone Number:")
update_phone_label.grid(row=1, column=0)
update_phone_entry = tk.Entry(update_frame)
update_phone_entry.grid(row=1, column=1)

update_email_label = tk.Label(update_frame, text="Email:")
update_email_label.grid(row=2, column=0)
update_email_entry = tk.Entry(update_frame)
update_email_entry.grid(row=2, column=1)

update_address_label = tk.Label(update_frame, text="Address:")
update_address_label.grid(row=3, column=0)
update_address_entry = tk.Entry(update_frame)
update_address_entry.grid(row=3, column=1)

update_button = tk.Button(update_frame, text="Update", command=update_contact)
update_button.grid(row=4, columnspan=2)

# Delete Contact
delete_frame = tk.LabelFrame(root, text="Delete Contact")
delete_frame.pack(padx=(10), pady=(5))

delete_name_label = tk.Label(delete_frame, text="Name:")
delete_name_label.pack(side=tk.LEFT)
delete_name_entry = tk.Entry(delete_frame)
delete_name_entry.pack(side=tk.LEFT)

delete_button = tk.Button(delete_frame, text="Delete", command=delete_contact)
delete_button.pack(side=tk.LEFT)

root.mainloop()