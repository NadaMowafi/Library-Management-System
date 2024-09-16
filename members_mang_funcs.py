import load_data

def register_member(member_id, name):
    if member_id in load_data.members:
        print(f"Member ID {member_id} already exists.")
    else:
        load_data.members[member_id] = {
            'name': name,
            'borrowed_books': []
        }
        print(f"Member '{name}' registered successfully.")

def update_member(member_id, name=None):
    if member_id in load_data.members:
        if name:
            load_data.members[member_id]['name'] = name
        print(f"Member ID {member_id} updated successfully.")
    else:
        print(f"Member ID {member_id} not found.")

def remove_member(member_id):
    if member_id in load_data.members:
        del load_data.members[member_id]
        print(f"Member ID {member_id} removed successfully.")
    else:
        print(f"Member ID {member_id} not found.")
