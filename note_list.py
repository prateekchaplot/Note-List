import os


def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')


def help():
    print("* Enter Q exit *")
    print("* Enter S to show list *")


def show():
    clear_screen()

    print("Note List:")
    print("-"*10)

    for index in range(len(user_list)):
        print("{}. {}".format(index+1, user_list[index]))


clear_screen()
print("\n ** Welcome to Note List **", end="")
input()
user_list = []

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

    user_list.append(item)

show()