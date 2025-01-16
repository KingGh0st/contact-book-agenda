import functions as fns
contacts = {}

if __name__ == "__main__":
    while True:
        fns.show_menu()
        opt = input("Choose an option (1-5): ")
        match int(opt):
            case 1:
                fns.add_contact(contacts)
            case 2:
                fns.search_contact(contacts)
            case 3:
                fns.edit_contact(contacts)
            case 4:
                fns.delete_contact(contacts)
            case 5:
                fns.show_all(contacts)
            case 0:
                break
            case _:
                print("Invalid option.")