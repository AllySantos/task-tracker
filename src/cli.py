import argparse

class Cli:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='Task tracker',
            description='Manage your tasks'
        )

    def configure_arguments(self):

        subparsers = self.parser.add_subparsers(dest="command", help="Available commands")

        parser_add = subparsers.add_parser("add", help="Add a new task")
        parser_add.add_argument("description", type=str, help="Description of the task")

        parser_delete = subparsers.add_parser("delete", help="Delete a task")
        parser_delete.add_argument("id", type=int, help="Description of the task")

        parser_update = subparsers.add_parser("update", help="Update task description")
        parser_update.add_argument("id", type=int, help="ID of task")
        parser_update.add_argument("description", type=str, help="Description of the task")

        parser_list = subparsers.add_parser("list", help="List registered tasks")
        parser_list.add_argument("status", type=str, help="Status of task", nargs='?', default=None)

        parser_progress = subparsers.add_parser("mark-in-progress", help="Mark task as IN PROGRESS")
        parser_progress.add_argument("id", type=int, help="ID of task")

        parser_done = subparsers.add_parser("mark-done", help="Mark task as DONE")
        parser_done.add_argument("id", type=int, help="ID of task")

        args = self.parser.parse_args()

        return args

