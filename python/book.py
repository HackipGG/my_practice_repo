class Book:
    def __init__(self, title, author, genre, checked_out = False):
        self.title=title
        self.author=author
        self.genre=genre
        self.checked_out=checked_out
    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}):{self.checked_out} "
    def check_out(self):
        if self.checked_out == True:
            return "this book is already checked out."
        else:
            self.checked_out = True
    def return_book(self):
        if self.checked_out == False:
            return "this book is not currently checked out."
        else:
            self.checked_out = False
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_genre(self):
        return self.genre
    def is_checked_out(self):
        return self.checked_out


