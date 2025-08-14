file = open("tasks.txt", "r")
tasks = file.read().split("\n")

# get each task in list of tasks
for task in tasks:
    to_do = (f"{tasks.index(task) + 1}. {task}")
    print(to_do)

