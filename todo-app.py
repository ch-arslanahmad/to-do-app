tasks= []
n=1
#tasks
if tasks:
    for i in tasks:
        print(f"{n}. {i}")
        n=n+1
    
    print("_" * 15)


def addtask():
    ntask = input("Enter Task: ")
    tasks.append(ntask)
    print("task added.")
    for i in range(len(tasks)):
        print(f"{i+1} = {tasks[i]}")

def removetask():
    if not tasks:
        print("No Task available to remove.")
    else:
        try:
            i = int(input("which position to remove: "))
            tasks.pop(i-1)
            print("task removed.")
            for i in range(len(tasks)):
                print(f"{i+1} = {tasks[i]}")
        except (ValueError, IndexError):
            print("The value is out of range.")

while True:
    try:
        choice = int(input("1.Add Task\n2.Remove Task\n Enter your choice: "))
        if(choice == 1):
            addtask()
        elif(choice ==2):
            removetask()
        else:
            break
    except ValueError:
        print("Enter a integer!")
