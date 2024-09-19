import load_data
from datetime import datetime, timedelta

def add_book(book_id, title, author, genre):
    if book_id in load_data.books:
        print(f"Book ID {book_id} already exists.")
    else:
        load_data.books[book_id] = {
            'title': title,
            'author': author,
            'genre': genre,
            'available': True,
            'borrowed_by': None,
            'due_date': None
        }
        print(f"Book '{title}' added successfully.")
        

def update_book(book_id, title=None, author=None, genre=None):
    if book_id in load_data.books:
        if title:
            load_data.books[book_id]['title'] = title
        if author:
            load_data.books[book_id]['author'] = author
        if genre:
            load_data.books[book_id]['genre'] = genre
        print(f"Book ID {book_id} updated successfully.")
    else:
        print(f"Book ID {book_id} not found.")

def remove_book(book_id):
    if book_id in load_data.books:
        del load_data.books[book_id]
        print(f"Book ID {book_id} removed successfully.")
    else:
        print(f"Book ID {book_id} not found.")

# Book Borrowing and Returning
def borrow_book(book_id, member_id):
    if book_id not in load_data.books:
        print(f"Book ID {book_id} not found.")
    elif not load_data.books[book_id]['available']:
        print(f"Book ID {book_id} is not available for borrowing.")
    elif member_id not in load_data.members:
        print(f"Member ID {member_id} not found.")
    else:
        load_data.books[book_id]['available'] = False
        load_data.books[book_id]['borrowed_by'] = member_id
        due_date = datetime.now() + timedelta(days=14)  # 2 weeks borrowing period
        load_data.books[book_id]['due_date'] = due_date.strftime('%Y-%m-%d')
        load_data.members[member_id]['borrowed_books'].append(book_id)
        print(f"Book ID {book_id} borrowed by Member ID {member_id}.")

def return_book(book_id, member_id):
    if book_id not in load_data.books:
        print(f"Book ID {book_id} not found.")
    elif load_data.books[book_id]['available']:
        print(f"Book ID {book_id} was not borrowed.")
    elif load_data.books[book_id]['borrowed_by'] != member_id:
        print(f"Book ID {book_id} was not borrowed by Member ID {member_id}.")
    else:
        load_data.books[book_id]['available'] = True
        load_data.books[book_id]['borrowed_by'] = None
        load_data.books[book_id]['due_date'] = None
        load_data.members[member_id]['borrowed_books'].remove(book_id)
        print(f"Book ID {book_id} returned by Member ID {member_id}.")

