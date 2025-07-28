#tasks
tasks= []

# show function
def Showtask():
    n=1
    if tasks:
        for i in tasks:
            print(f"{n}. {i}")
            n=n+1
    print("_" * 15)

# add-task function
def Addtask():
    ntask = input("Enter Task: ")
    tasks.append(ntask)
    print("task added.")
    # calling show function
    Showtask();
# remove-task function
def Removetask():
    if not tasks:
        print("No Task available to remove.")
    else:
        try:
            i = int(input("which position to remove: "))
            tasks.pop(i-1)
            print("task removed.")
            # calling show function
            Showtask();
        except (ValueError, IndexError):
            print("The value is out of range.")
# Infinite Loop
while True:
    try:
        choice = int(input("0. Exit\n1. Add Task\n2. Remove Task\n3. Display Task\nEnter your choice: "))
        # if conditional: continue if choice is smaller than 4.
        if(choice<4):
            match choice:
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
                case _:
                # keyword to stop the loop.
                    break
        else:
            print("Enter value between 0-3. 0 for exit.")
    except ValueError:
        print("Enter a integer!")
