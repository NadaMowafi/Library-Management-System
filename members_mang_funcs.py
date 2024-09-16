import load_data

def register_member(member_id,name,borrowed_books):
    if member_id in load_data.members:
        print(f"A member with ID {member_id} exists already")
    else:
        load_data.members[member_id] = {
            'name': name,
            'borrowed_books': borrowed_books
        }
        print("Student added successfully.")

def update_member(member_id,name=None,borrowed_books=None):
    if member_id in load_data.members:
        if name:
            load_data.members[member_id]['name']=name
        if borrowed_books:
            load_data.members[member_id]['borrowed_books']=borrowed_books.split(',')
        print(f"Info of member with ID {member_id} has been updated successfully")
    else:
        print(f"A member with ID {member_id} could not be found.")


def remove_member(member_id):
    if member_id in load_data.members:
        del load_data.members[member_id]
        print(f"Member with ID {member_id} has been deleted successfully.")
    else:
        print(f"A member with ID {member_id} could not be found.")


def show_members():
    if not load_data.members:
        print("No members found.")
        return
    for member_id, details in load_data.members.items():
        borrowed_books=','.join(details['borrowed_books']) #join list of books in one string
        print(f"Member ID: {member_id}, Name: {details['name']}, Borrowed books: {borrowed_books}")




