import datetime
import time
import os
import json


class Status:
    TO_DO = 0
    IN_PROGRESS = 1
    DONE = 2

    def get_name(self, status):
        match status:
            case self.TO_DO:
                return 'TO-DO'
            case self.IN_PROGRESS:
                return 'IN_PROGRESS'
            case _:
                return 'DONE'

    def get_number(self, status):
        match status:
            case 'TO-DO':
                return self.TO_DO
            case 'IN_PROGRESS':
                return self.IN_PROGRESS
            case _:
                return self.DONE


class Task:

    DATETIME_FORMAT = '%d/%m/%Y-%H:%M:%S'

    def __init__(self, identification=None, description=None, status=None, created_at=None, updated_at=None):
        self.identification = identification
        self.description = description
        self.status = status or Status.TO_DO
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or '-'

    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            identification=task_dict['identification'],
            description=task_dict['description'],
            status=task_dict['status'],
            created_at=cls.string_to_datetime(task_dict['created_at']),
            updated_at=cls.string_to_datetime(task_dict['updated_at']),
        )

    def to_dict(self):
        return {
            "identification": self.identification,
            "description": self.description,
            "status": self.status,
            "created_at": self.datetime_to_string(self.created_at),
            "updated_at": self.datetime_to_string(self.updated_at),
        }

    def to_string(self):
        return (
            f"ID: {self.identification} | "
            f"DESCRIPTION: {self.description} | "
            f"STATUS: {Status().get_name(self.status)} | "
            f"CREATED AT: {self.datetime_to_string(self.created_at)} | "
            f"UPDATED AT: {self.datetime_to_string(self.updated_at)}"
        )

    @staticmethod
    def datetime_to_string(date):
        if isinstance(date, datetime.datetime):
            return date.strftime(Task.DATETIME_FORMAT)
        return date

    @staticmethod
    def string_to_datetime(date_str):
        if date_str == '-' or not date_str:
            return None
        return datetime.datetime.strptime(date_str, Task.DATETIME_FORMAT)

class Persistence:

    def __init__(self):
        self.file_path = fr'{os.getcwd()}\data\database.json'

    def save_task(self, task):
        task_dict = task.to_dict()

        file = open(file=self.file_path,mode='a', encoding='utf-8')
        file.write(str(task_dict).replace("\'", "\""))
        file.write("\n")
        file.close()

    def update_task(self, task):
        tasks = self.load_task()

        for idx, item_task in enumerate(tasks):
            if item_task.identification == task.identification:
                tasks[idx] = task
                break
        self.save_all_tasks(tasks)

    def delete_task(self, delete_task):
        tasks = self.load_task()
        new_tasks = [task for task in tasks if task.identification != delete_task.identification ]
        self.save_all_tasks(new_tasks)

    def save_all_tasks(self, tasks):
        self.clean_file()
        for task in tasks:
            self.save_task(task)

    def clean_file(self):
        file = open(file=self.file_path,mode='w', encoding='utf-8')
        file.close()

    def load_task(self):
        file = open(file=self.file_path,mode='r', encoding='utf-8')
        file_data = file.readlines()
        tasks = []

        for line in file_data:
            task = json.loads(line)
            task = self.json_to_task(task)
            tasks.append(task)
        return tasks

    def filter_task_by_status(self, status):
        tasks = self.load_task()
        filtered_list = [item for item in tasks if item.status == status]
        return filtered_list

    def get_task_by_id(self, identification):
        tasks = self.load_task()
        task = next((task for task in tasks if task.identification == identification), None)
        return task

    @staticmethod
    def json_to_task(json_object):
        task = Task(json_object['identification'], json_object['description'], json_object['status'], json_object['created_at'], json_object['updated_at'])
        return task

class TaskManager:

    def __init__(self):
        self.persistence = Persistence()

    def generate_task_id(self):
        tasks = self.persistence.load_task()

        if len(tasks) > 0:
            last_task = tasks[-1]
            new_id = int(last_task.identification) + 1
        else:
            new_id = 1
        return new_id

    def create_task(self,description):
        identification = self.generate_task_id()
        task = Task(identification=identification, description=description)
        self.persistence.save_task(task)

    def list_tasks(self):
        tasks = self.persistence.load_task()
        for task in tasks:
            print(task.to_string())

    def update_task_status(self, identification, new_status):
        task_updated = self.persistence.get_task_by_id(identification)

        if task_updated:
            task_updated.status = new_status
            task_updated.updated_at = datetime.datetime.now()
            self.persistence.update_task(task_updated)
        else:
            print(f'Task with ID {identification} was not found')

    def update_task_description(self, identification, description):
        task_updated = self.persistence.get_task_by_id(identification)

        if task_updated:
            task_updated.description = description
            task_updated.updated_at = datetime.datetime.now()
            self.persistence.update_task(task_updated)
        else:
            print(f'Task with ID {identification} was not found')

    def delete_task(self, identification):
        task_deleted = self.persistence.get_task_by_id(identification)
        if task_deleted:
            self.persistence.delete_task(task_deleted)
        else:
            print(f'Task with ID {identification} was not found')

    def filter_task_by_status(self, status):
        status = Status().get_number(status)
        filtered_list = self.persistence.filter_task_by_status(status)

        for item in filtered_list:
            print(item.to_string())







