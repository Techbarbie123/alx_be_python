# shopping_list_manager.py

# Initialize an empty shopping list
shopping_list = []

def display_menu():
<<<<<<< HEAD
    print(f"\n" "shopping_list manager")
=======
    """
    Displays the menu with options for the shopping list manager.
    """
    print(f"\nShopping List Manager")
>>>>>>> 4bd21f0cd27430afaf5714906da76bc3d9c27978
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit")

def add_item():
    """
    Prompts the user to add an item to the shopping list.
    """
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f'"{item}" has been added to your shopping list.')
    else:
        print(f"Invalid input. Please enter a valid item name.")

def remove_item():
    """
    Prompts the user to remove an item from the shopping list.
    """
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" has been removed from your shopping list.')
    else:
        print(f'"{item}" is not in your shopping list.')

def view_list():
    """
    Displays the current shopping list to the user.
    """
    if shopping_list:
        print(f"\nYour Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print(f"Your shopping list is empty.")

def main():
    """
    The main function that runs the shopping list manager.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item()

        elif choice == '2':
            remove_item()

        elif choice == '3':
            view_list()

        elif choice == '4':
            print(f"Goodbye!")
            break

        else:
            print(f"Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
