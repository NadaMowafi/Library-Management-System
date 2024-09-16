books = {}  # dic for books
members = {} # dic for members 

# This function loads information about books and members from the txt file
def load_data():
    global books, members
    # Load books
    try:
        with open("C:\summer 2024\Library-Management-System\books.txt", 'r') as f:
           for line in f:
                book_id, title, author, genre, availability_status = line.strip().split('|')
                books[book_id] = {
                    'title': title,
                    'author': author,
                    'genre': genre,
                    'availability_status': availability_status
                }
    except FileNotFoundError:
        books = {}
    
    # Load members
    try:
        with open("C:\summer 2024\Library-Management-System\members.txt", 'r') as f:
            for line in f:
                member_id, name, borrowed_books = line.strip().split('|')
                if borrowed_books == "None":
                    borrowed_books = []
                else:
                    borrowed_books = borrowed_books.split(',')
                members[member_id] = {
                    'name': name,
                    'borrowed_books': borrowed_books
                }
    except FileNotFoundError:
        members = {}

def save_data():
    # Save books
    with open("C:\summer 2024\Library-Management-System\books.txt", 'w') as f:
         for book_id, details in books.items():
            f.write(f"{book_id}|{details['title']}|{details['author']}|{details['genre']}|{details['availability_status']}\n")
    
    # Save members
    with open('"C:\summer 2024\Library-Management-System\members.txt"', 'w') as f:
        for member_id, details in members.items():
            borrowed_books = ','.join(details['borrowed_books']) if details['borrowed_books'] else 'None'
            f.write(f"{member_id}|{details['name']}|{borrowed_books}\n")