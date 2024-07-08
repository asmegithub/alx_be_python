shopping_list = []


def add(item):
    global shopping_list
    shopping_list.append(item)


def remove(item):
    global shopping_list
    shopping_list.remove(item)


def view():
    print(shopping_list)
