from classes import Status
from classes import TaskManager

def main():

    manager = TaskManager()
    manager.create_task(1, 'Nova Task')
    manager.list_tasks()

if __name__ == '__main__':
    main()