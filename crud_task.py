import add_function
import view_function
import update_function
import delete_function

# call functions
add_task_response = add_function.add_task("Learn")
print(add_task_response)

show_task_response = view_function.show_tasks()
print(show_task_response)

update_task_response = update_function.edit_tasks("Learn", "Sleep")
print(update_task_response)

delete_task_response = delete_function.delete_tasks("Sleep")
print(delete_task_response)


