from prettytable import PrettyTable
#Simple function to show the menu
def show_menu():
    print("\n------------ Contact Book ------------")
    print("1. Add a contact")
    print("2. Search a contact")
    print("3. Edit a contact")
    print("4. Delete a contact")
    print("5. Show all contacts")
    print("0. To exit")

#Function to add an item to a dictionary, where the item is a contact, the contact name is the key of the dict
#and the value is the mail and the phone number
def add_contact(dic):
    name = input("Enter contact name: ")
    mail = input("Enter contact mail: ")
    phone_number = input("Enter contact phone number: ")
    dic[name] = {"mail":mail,"phone_number":phone_number}
    print(f"{name} contact has been added succesfully.")

#Function to search an item in the dictionary, where the item is a contact
#If you give the name to search, the message for input a name will not be displayed
def search_contact(dic, name = ""):
    if name == "":
        name = input("Enter contact name to search: ")
    if name in dic:
        print(f"Name: {name}")
        print(f"E-mail: {dic[name]['mail']}")
        print(f"Phone number: {dic[name]['phone_number']}")
        return True
    else:
        print("Contact not found")
        return False

#Function to edit an item in the dictionary, where the item is a contact
#It uses the search_contact function to find the contact
def edit_contact(dic):
    name = input("Enter contact name to edit: ")
    if search_contact(dic, name):
        opt = input("Are you sure you want to edit this contact? Y/n: ")
        if opt == "Y" or opt == "y":
            mail = input("Enter contact new mail: ")
            phone = input("Enter contact new phone number: ")
            dic[name] = {"mail":mail, "phone_number":phone}
            print("Contact edited.")
        else:
            print("This contact will not be edited.")

#Function to delete an item in the dictionary, where the item is a contact
#It uses the search_contact function to find the contact
#It uses pop method of dictionaries
def delete_contact(dic):
    name = input("Enter contact name to delete: ")
    if search_contact(dic, name):
        opt = input("Are you sure you want to delete this contact? Y/n: ")
        if opt == "Y" or opt == "y":
            dic.pop(name)
            print("Contact deleted.")
        else:
            print("This contact will not be deleted.")

#Function to show all the items in the dictionary, where the items are contacts
#It uses a PrettyTable for display it in table shape
def show_all(dic):
    table = PrettyTable(["Name","E-mail","Phone"])
    if dic:
        print("\n---------- All contacts ----------")
        for key,item in dic.items():
            table.add_row([key, item["mail"],item["phone_number"]])
        print(table)
    else:
        print("No contacts found")