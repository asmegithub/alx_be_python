shopping_list = []


def add(item):
    global shopping_list
    shopping_list.append(item)


def remove(item):
    global shopping_list
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found")


def view():
    print(shopping_list)


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add(input("Enter an item: "))
        pass
    elif choice == "2":
        remove(input("Enter an item: "))
        pass
    elif choice == "3":
        view()
        pass
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
