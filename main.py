import input  # another file for input
import database  # for database queries
import map  # for mapping IDs
import display  # Get Display


def main():
    tasks = database.get_tasks()
    tasks = [task[0] for task in tasks]
    # Infinite Loop
    while True:
        count = database.count_tasks()
        choice = input.get_Val(display.getMenu(tasks) - 1)
        match choice:
            case 0:  # stop the loop.
                print(f"Count: {count}")
                break
            case 1:  # calling add
                database.add_task(
                    input.get_str(
                        "task",
                    )
                )
                display.show_tasks(database.get_tasks())
                count = database.count_tasks()
            case 2:  # remove task
                display.show_tasks(database.get_tasks())
                db_id = map.get_mapped_db_id(input.get_Val(count))
                if db_id is None:  # as 0 is also treated as False
                    print("ID is invalid.")
                    break
                database.remove_task(db_id)
                count = database.count_tasks()
            case 3:  # update task
                display.show_tasks(database.get_tasks())

                db_id = map.get_mapped_db_id(input.get_Val(count))

                if db_id is None:  # as 0 is also treated as False
                    print("ID is invalid.")
                    break

                database.update_task(db_id, input.get_str("Enter updated Task"))
            case 4:  # calling show
                display.show_tasks(database.get_tasks())

            case 5:  # updating status
                display.show_tasks(database.get_tasks())
                db_id = map.get_mapped_db_id(input.get_Val(count))
                if db_id is None:  # as 0 is also treated as False
                    print("ID is invalid.")
                    break
                while True:
                    status = input.get_str("Status")
                    if status == "0":
                        break
                    elif status not in ["todo", "pending", "done"]:
                        print("Invalid Status")
                        continue
                    else:
                        database.update_task_status(db_id, status)  # update task status
                        display.show_tasks(database.get_tasks())
                        break


if __name__ == "__main__":
    main()
