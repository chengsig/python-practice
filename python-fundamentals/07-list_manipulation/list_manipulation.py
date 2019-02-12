def list_manipulation(li, command, location, fourth=None):
    """given a list, command = 'remove/add', location = 'beginning/end', with fourth value optional only when the command is add"""
    if command == 'remove':
        if location == 'end':
            return li.pop()
        elif location == 'beginning':
            return li.pop(0)
    elif command == 'add':
        if location == 'beginning':
            li.insert(0, fourth)
            return li
        elif location == 'end':
            li.append(fourth)
            return li