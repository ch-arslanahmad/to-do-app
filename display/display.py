def get_options():
    options = ["Add", "Remove", "Update", "Display", "Update Status"]
    return options


def getMenu(tasks):
    options = get_options()  # get all options

    if not tasks:
        for i in ["Remove", "Update", "Display", "Update Status"]:
            options.remove(i)
    n = 1
    for i in options:
        print(f"{n}. " + i)
        n = n + 1
    return n


def show_tasks(tasks):
    print("\n")
    n = 0
    for i in tasks:
        print(f"{n+1}. {i[0]}\t | {i[1]}")
        n = n + 1
    print("\n")
