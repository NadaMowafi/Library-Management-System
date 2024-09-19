import load_data
import book_cat_funcs
import members_mang_funcs
import reporting
from book_cat_funcs import add_book, update_book, remove_book,borrow_book,return_book
from reporting import list_borrowed_books,list_overdue_books,most_popular_books
from members_mang_funcs import register_member, update_member, remove_member, show_members


def user_menu():
    while True:
     print("Select member management menu by pressing m or book management menu by pressing b or e to exit")
     mode=input()
     if mode=='m' or mode=='M':
         member_menu()
     elif mode=='b' or mode=='B':
         book_menu()
     elif mode=='e' or mode=='E':
         break
     else:
         print("Invalid input, please try again!!")

def member_menu():
    while True:
        print("Member Management Menu:")
        print("1.Register a new member")
        print("2.Update an existing member's info.")
        print("3.Delete a member")
        print("4.Show all members")
        print("5.Return to main menu")
        choice_member = int(input())
        if choice_member == 1:
            print("Enter the member ID")
            member_id = input()
            print("Enter the member name:")
            name = input()
            print("List all borrowed books and separate them by commas")
            borrowed_books = input().split(',')
            register_member(member_id, name, borrowed_books)
        elif choice_member == 2:
            print("Enter the ID of the member you wish to update")
            member_id = input()
            print("Enter new name or leave it blank to keep the same")
            name = input()
            print("Enter new borrowed books (comma-separated, or leave it blank to keep the same)")
            borrowed_books = input()
            update_member(member_id, name if name else None, borrowed_books if borrowed_books else None)
        elif choice_member == 3:
            print("Enter the ID of the member you wish to delete")
            member_id = input()
            remove_member(member_id)
        elif choice_member == 4:
            show_members()
        elif choice_member == 5:
            return
        else:
            print("Invalid input, please try again!!")


def book_menu():
    while True:
        print("Book Management Menu:")
        print("1.Add a new book")
        print("2.Update an existing book's info.")
        print("3.Delete a book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. List Borrowed Books")
        print("7. List Overdue Books")
        print("8. Most Popular Books")
        print("9.Return to main menu")
        print(load_data.books)
        choice_books = int(input())
        if choice_books == 1:
            print("Enter the ID of the book")
            book_id = input()
            print("Enter the title of the book")
            title = input()
            print("Enter the name of the author")
            author = input()
            print("Enter the Genre of the book")
            genre = input()
            add_book(book_id, title, author, genre)
        elif choice_books == 2:
            print("Enter the ID of the book you wish to update")
            book_id = input()
            print("Enter new title or leave it blank to keep the same")
            title = input()
            print("Enter new author or leave it blank to keep the same")
            author = input()
            print("Enter new genre or leave it blank to keep the same")
            genre = input()
            update_book(book_id, title if title else None, author if author else None, genre if genre else None)
        elif choice_books == 3:
            print("Enter the ID of the book you wish to delete")
            book_id = input()
            remove_book(book_id)
        elif choice_books == 4:
            book_id = input("Enter Book ID to borrow: ")
            member_id = input("Enter Member ID: ")
            borrow_book(book_id, member_id)
        elif choice_books == 5:
            book_id = input("Enter Book ID to return: ")
            member_id = input("Enter Member ID: ")
            return_book(book_id, member_id)
        elif choice_books == 6:
            list_borrowed_books()
        elif choice_books == 7:
            list_overdue_books()
        elif choice_books == 8:
            most_popular_books()
        elif choice_books == 9:
            return
        else:
            print("Invalid input, please try again!!")



user_menu()