from cli import Cli
from classes import TaskManager
from classes import Status

def main():

    cli = Cli()
    args = cli.configure_arguments()

    manager = TaskManager()

    match args.command:
        case 'add':
            task_desc = args.description
            manager.create_task(task_desc)
        case 'update':
            task_id = args.id
            task_desc = args.description
            manager.update_task_description(task_id, task_desc)
        case 'list':
            task_status = args.status
            if task_status is None:
                manager.list_tasks()
            else:
                manager.filter_task_by_status(task_status)
        case 'delete':
            task_id = args.id
            manager.delete_task(task_id)

        case 'mark-in-progress':
            task_id = args.id
            task_status = Status.IN_PROGRESS
            manager.update_task_status(task_id, task_status)
        case 'mark-done':
            task_id = args.id
            task_status = Status.DONE
            manager.update_task_status(task_id, task_status)

if __name__ == '__main__':
    main()