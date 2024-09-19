import load_data
from datetime import datetime, timedelta

# Reporting Functions
def list_borrowed_books():
    borrowed_books = {book_id: details for book_id, details in load_data.books.items() if not details['available']}
    if borrowed_books:
        print("Borrowed Books:")
        for book_id, details in borrowed_books.items():
            print(f"{book_id}: {details['title']} - Borrowed by Member ID {details['borrowed_by']} (Due on {details['due_date']})")
    else:
        print("No books are currently borrowed.")

def list_overdue_books():
    overdue_books = {book_id: details for book_id, details in load_data.books.items()
                     if not details['available'] and datetime.strptime(details['due_date'], '%Y-%m-%d') < datetime.now()}
    if overdue_books:
        print("Overdue Books:")
        for book_id, details in overdue_books.items():
            print(f"{book_id}: {details['title']} - Borrowed by Member ID {details['borrowed_by']} (Due on {details['due_date']})")
    else:
        print("No books are overdue.")

def most_popular_books():
    popularity = {book_id: 0 for book_id in load_data.books}
    for member in load_data.members.values():
        for book_id in member['borrowed_books']:
            popularity[book_id] += 1
    popular_books = sorted(popularity.items(), key=lambda x: x[1], reverse=True)[:5]
    if popular_books:
        print("Most Popular Books:")
        for book_id, count in popular_books:
            print(f"{book_id}: {load_data.books[book_id]['title']} - Borrowed {count} times")
    else:
        print("No popular books found.")
