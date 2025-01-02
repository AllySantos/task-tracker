from classes import Status
from classes import Task
from classes import Persistence

def main():

    task = Task()
    task.create(1, 'Nova Task', Status.TO_DO)
    task.print()

    task.update(Status.DONE)
    task.print()

    Persistence().save_task(task)

if __name__ == '__main__':
    main()