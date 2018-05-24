import os


def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')


def help():
    print("* Enter Q to exit *")
    print("* Enter S to show list *")
    print("* Enter R to remove item from list *")
    print("* Enter U to update item in list *")


def show():
    clear_screen()

    print("Note List:")
    print("-"*10)

    for index in range(len(user_list)):
        print("{}. {}".format(index + 1, user_list[index]))


def remove():
    show()
    print("\n* Enter index of the item to remove that item *")
    print("* Press ENTER if you don't want to delete any item *\n")
    
    try:
        index = int(input("> ")) - 1
    except ValueError:
        print("List Unchanged!")
    else:
        if index in range(len(user_list)):
            print("Removed:", user_list[index])
            del user_list[index]
        else:
            print("* Invalid index selected... *")
    

def update():
    show()
    print("\n* Enter index of the item to be updated *")
    print("* Press Enter if you don't want to update any item *\n")

    try:
        index = int(input("> ")) - 1
    except ValueError:
        print("List Unchanged!")
    else:
        if index in range(len(user_list)):
            clear_screen()
            user_list[index] = input("Enter value for {}\n> ".format(user_list[index]))
            print("Updated to:", user_list[index])
        else:
            print("* Invalid index selected... *")


def save_file():
    try:
        if not file_exists:
            f = open("note_list.txt", "a")
        else:
            f = open("note_list.txt", "w")
    except Exception:
        print("Problem encountered while saving!")
    else:
        size = len(user_list)
        for index in range(size):
            if index != size - 1:
                f.write("{}\n".format(user_list[index]))
            else:
                f.write("{}".format(user_list[index]))

        # for item in user_list:
        #     f.write("{}\n".format(item))

        f.close()

        print("\n** Items saved! **")


def read_file(file_exists, user_list):
    try:
        f = open("note_list.txt", "r")
    except Exception:
        file_exists = False
        print(" * No existing file found! *")
    else:
        user_list = f.read().split("\n")``
        f.close()
        print(" ** Existing file loaded! **")
    
    return (file_exists, user_list)


clear_screen()

file_exists = True
user_list = []

print("\n ** Welcome to Note List **")
file_exists, user_list= read_file(file_exists, user_list)
input()

while True:
    clear_screen()
    help()
    
    item = input("> ")
    
    if item.lower() == 'q':
        break
    elif item.lower() == 's':
        show()
        input("Press return to continue...")
        continue
    elif item.lower() == 'r':
        remove()
        input("Press return to continue...")
        continue
    elif item.lower() == 'u':
        update()
        input("Press return to continue...")
        continue

    user_list.append(item)

show()
save_file()
input("Press Enter to exit...")