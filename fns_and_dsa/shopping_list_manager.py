shopping_list = []


def add(item):
    global shopping_list
    shopping_list.append(item)


def remove(item):
    global shopping_list
    shopping_list.remove(item)


def view():
    print(shopping_list)


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add(input("Enter the item to add: "))
            pass
        elif choice == 2:
            remove(input("Enter the item to remove: "))
            pass
        elif choice == 3:
            view()
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
