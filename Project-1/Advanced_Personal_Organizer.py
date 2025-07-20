contacts = []
tasks = []
events = []

def print_separator():
    print("-" * 40)

def check_valid_answer(inputEntered):
    if(len(inputEntered) == 1) and inputEntered.lower() == 'x':
        print("Exiting organizer. Goodbye!")
        exit()
    return inputEntered.strip()

def user_greetings():
    # Greet User and ask the name for further processing.
    username = input('Can we have your name please!: ')
    user_val = check_valid_answer(username)
    if(user_val):
        print(f"Hello! {user_val}!, Welcome")
    else:
        print("You have exited from the app.")

def get_valid_menu_choice(prompt, valid_options):
    print_separator()
    choice = input(prompt).strip().lower()
    if choice in valid_options:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return get_valid_menu_choice(prompt, valid_options)

def main_menu():
    while True:
        choice = get_valid_menu_choice("1 - Manage Contacts\n2 - Manage Tasks\n3 - Manage Events\nx - Exit\nEnter your choice: ", ['1', '2', '3', 'x']) 
        if choice == '1':
            contact_menu()
        elif choice == '2':
            task_menu()
        elif choice == '3':
            event_menu()
        elif choice == 'x':
            print("Exiting organizer. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def contact_menu():
    while True:
        choice = get_valid_menu_choice("1 - Add Contact\n2 - View Contact\n3 - Update Contact\n4 - Delete Contact\n0 - Go back to main menu\nx - Exit\nEnter your choice: ", ['1', '2', '3', '4', '0', 'x']) 
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == 'x':
            print("Exiting organizer. Goodbye!")
            exit()
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts.append({'name': name, 'phone': phone})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(f"{idx+1}. {contact['name']} - {contact['phone']}")

def update_contact():
    view_contacts()
    if not contacts:
        return
    idx = int(input("Enter contact number to update: ")) - 1
    if 0 <= idx < len(contacts):
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone: ")
        contacts[idx] = {'name': new_name, 'phone': new_phone}
        print("Contact updated.")
    else:
        print("Invalid contact number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    idx = int(input("Enter contact number to delete: ")) - 1
    if 0 <= idx < len(contacts):
        deleted = contacts.pop(idx)
        print(f"Deleted contact: {deleted['name']}")
    else:
        print("Invalid contact number.")

def event_menu():
    while True:
        choice = get_valid_menu_choice("1 - Add Event\n2 - View Events\n3 - Delete Event\n0 - Go back to main menu\nx - Exit\nEnter your choice: ", ['1', '2', '3', '0', 'x']) 
        if choice == '1':
            add_event()
        elif choice == '2':
            view_events()
        elif choice == '3':
            delete_event()
        elif choice == 'x':
            print("Exiting organizer. Goodbye!")
            exit()
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def add_event():
    title = input("Enter event title: ")
    date = input("Enter event date (e.g., 2025-07-18): ")
    events.append({'title': title, 'date': date})
    print("Event added!")

def view_events():
    if not events:
        print("No events scheduled.")
    else:
        for idx, event in enumerate(events):
            print(f"{idx+1}. {event['title']} on {event['date']}")

def delete_event():
    view_events()
    if not events:
        return
    idx = int(input("Enter event number to delete: ")) - 1
    if 0 <= idx < len(events):
        removed = events.pop(idx)
        print(f"Deleted event: {removed['title']}")
    else:
        print("Invalid event number.")

def task_menu():
    while True:
        choice = get_valid_menu_choice("1 - Add Task\n2 - View Tasks\n3 - Mark task as completed\n4 - Delete task\n0 - Go back to main menu\nx - Exit\nEnter your choice: ", ['1', '2', '3', '4', '0', 'x']) 
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == 'x':
            print("Exiting organizer. Goodbye!")
            exit()
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({'task': task_name, 'completed': False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            status = "completed" if task['completed'] else "incomplete"
            print(f"{idx+1}. {task['task']} - {status}")

def mark_task_complete():
    view_tasks()
    if not tasks:
        return
    idx = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]['completed'] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        print(f"Deleted task: {removed['task']}")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    # Show the menu options here and ask the user for input
    user_greetings()
    main_menu()