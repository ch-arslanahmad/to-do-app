import input # another file for input

# tasks
tasks = []


# show function
def Showtask():
    n = 1
    if tasks:
        for i in tasks:
            print(f"{n}. {i}")
            n = n + 1
    print("_" * 15)


# add-task function
def Addtask():
    ntask = input("Enter Task: ")
    tasks.append(ntask)
    print("task added.")
    # calling show function
    Showtask()


# remove-task function
def Removetask():
    if not tasks:
        print("No Task available to remove.")
    else:
        try:
            i = int(input("which position to remove: "))
            tasks.pop(i - 1)
            print("task removed.")
            # calling show function
            Showtask()
        except (ValueError, IndexError):
            print("The value is out of range.")


def getOptions():
    options = ["Add", "Remove", "Update", "Display"]
    return options


def getMenu():
    if not tasks:
        options = getOptions()
        for i in ["Remove", "Update", "Display"]:
            options.remove(i)
    for i in options:
        n = 1
        print(f"{n}. " + "options")
    return n


# Infinite Loop
while True:
    # if conditional: continue if choice is smaller than 4.
    choice = input.get_Val(getMenu())
    match choice:
        case 0:
            # keyword to stop the loop.
            break
        case 1:
            # calling add-task
            Addtask()
        case 2:
            # calling remove-task
            Removetask()
        case 3:
            # calling show-task
            Showtask()
        # default case
