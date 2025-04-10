from book import Book
Books = []
with open("books.txt") as file:
        for line in file:
            ln=line.strip().split(",")
            Books.append(Book(ln[0], ln[1], ln[2]))
print(Books[0].get_title())
print(Books[0].get_author())
print(Books[0].get_genre())
print(Books[0].is_checked_out())
Books[0].check_out()
print(Books[0])
Books[0].return_book()
print(Books[0])