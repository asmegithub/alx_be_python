import random


tsedi = {
    "title": "The names of Christ",
    "author": "Dn Azmeraw",
    "genre": "Religious",
}
selam = {
    "title": "The names of Christ",
    "author": "Dn Azmeraw",
    "genre": "Religious",
}
fikir = {
    "title": "Digua in The holy Bible",
    "author": "M/Haddis Alemayehu",
    "genre": "Religious",
}

my_fav_books = {
    "tsedi": tsedi,
    "selam": selam,
    "fikir": fikir,
}

# print(my_fav_books.get("tsedi", "Book not found"))
random.randint(1, 10)
random_numbers = {}
for i in range(10):
    random_numbers[i] = random.randint(1, 10)

print(list(random_numbers.values()))
