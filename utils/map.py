import database


"""
... REASONING
So this variable creates a mapping that both an interface (CLI or GUI) or Databse Queries can use:
- Interface - getting (index + task + status)
    - Best for display (text or GUI)
- Database - getting (user-index, tuple of task in DB)
    - Execute indexed queries from user input (text/UI) by matching pre-selected user indices with indices of database table for intuitive, efficient querying instead of processing full task descriptions.
"""

"""
... How it Works (LOGIC)
For `mapping`:
1. Key -   An index + 1, so user input starts with 1, more intiuitive,
2. Value -  extracts ID from tuple
3. Loops - loops the variables over the list of tasks (tuples)

Syntax:
... {key : value for loop}

"""


def get_user_mapping():
    tasks = database.get_tasks_with_id()
    # {n /user, d /database}
    mapping = {index + 1: task[0] for index, task in enumerate(tasks)}
    return mapping


def get_db_mapping():
    tasks = database.get_tasks_with_id()
    mapping = {task[0]: index + 1 for index, task in enumerate(tasks)}
    # {d /database, n /user}
    return mapping


def get_mapped_db_id(user_id):
    mapping = get_user_mapping()
    max_id = max(mapping.keys()) if mapping else 0
    if user_id > max_id:
        return
    else:
        return mapping.get(user_id)
