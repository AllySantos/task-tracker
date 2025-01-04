from classes import Status
from classes import TaskManager

def main():

    manager = TaskManager()
    # manager.create_task('Nova Task')
    manager.list_tasks()
    manager.update_task_status(1, 2)
    # manager.delete_task(4)
    # manager.filter_task_by_status('TO-DO')
if __name__ == '__main__':
    main()