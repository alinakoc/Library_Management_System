class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        print("Library opened.")

    def __del__(self):
        self.file.close()
        print("Library closed.")

    def list_books(self):
        print("Books in the Library:")
        self.file.seek(0)
        book_lines = self.file.readlines()
        for line in book_lines:
            book_info = line.strip().split(",")
            book_name, author = book_info[0], book_info[1]
            print(f"- {book_name} - {author}")
    
    def add_book(self):
        book_name = input("Please enter the book name: ")
        author = input("Please enter the author: ")
        release_year = input("Please enter the release year: ")
        num_pages = input("Please enter the number of pages: ")

        book_info = f"{book_name}, {author}, {release_year}, {num_pages}\n"

        self.file.seek(0, 2)  # Dosyanın sonuna git
        self.file.write(book_info)
        print("Book successfully uploaded")



    def remove_book(self):
        Rbook_name = input("Please enter which book you want to remove from the list: ")
        book_lines = self.file.readlines() 
        self.file.seek(0) 
        self.file.truncate() 
        for line in book_lines:
            if Rbook_name not in line: 
                self.file.write(line)
        self.file.seek(0)     # Dosyanın başına dön
    
        print(f"{Rbook_name} successfully removed from the library.")



    def search_book(self):
        search_term = input("Please enter the book name or author to search: ")
        found_books = []
        self.file.seek(0)
        for line in self.file:
            if search_term.lower() in line.lower():
                found_books.append(line.strip())
        if found_books:
            print("Matching books found:")
            for book in found_books:
                print(book)
        else:
            print("No matching books found.")

    def display_menu(self):
        while True:
            print("*** MENU ***")
            print("1) List Books")
            print("2) Add Book")
            print("3) Remove Book")
            print("4) Search Book")
            print("5) Exit")
            choice = input("Please enter your choice: ")
            if choice == "1":
                self.list_books()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.remove_book()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                print("Exiting the program...")
                break
            else:
                print("Please choose a number between 1 and 5.")
lib = Library()
lib.display_menu()
