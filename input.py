def get_Val(n):
    try:
        while True:
            val = int(input(f"Enter value(0-{n}): "))
            if val > n:
                print(f"Enter value between 0-{n}. 0 for exit.")
            else:
                return val
    except ValueError:
        print("Enter a integer!")


def get_str():
    return input("Enter: ")
