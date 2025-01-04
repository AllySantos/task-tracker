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

    def __init__(self):
        self.identification = self.description = self.status = self.created_at = self.updated_at = None

    def create(self, identification, description):
        self.identification = identification
        self.description = description
        self.status = Status.TO_DO
        self.created_at = datetime.datetime.now()
        self.updated_at = '-'

        return self

    def set(self, identification, description, status, created_at, updated_at):
        self.identification = identification
        self.description = description
        self.status = status
        self.created_at = self.datetime_to_string(created_at)
        self.updated_at = self.datetime_to_string(updated_at)

        return self

    def to_string(self):
        status = Status().get_name(self.status)

        created_at = self.datetime_to_string(self.created_at)
        updated_at = self.datetime_to_string(self.updated_at)

        return f"ID: {self.identification}\t|\tDESCRIPTION: {self.description}\t|\tSTATUS: {status}\t|\tCREATED AT: {created_at}\t|\tUPDATED AT: {updated_at}"

    def to_dict(self):
        created_at = self.datetime_to_string(self.created_at)
        updated_at = self.datetime_to_string(self.updated_at)

        task_dict = {"identification": self.identification,
                     "description": self.description,
                     "status": self.status,
                     "created_at": created_at,
                     "updated_at":updated_at}
        return task_dict

    def datetime_to_string(self, date):
        datetime_format = '%d/%m/%Y-%H:%M:%S'
        if type(date) != str and type(date) is not None:
            return datetime.datetime.strftime(date, datetime_format)
        else:
            return date

class Persistence:

    def __init__(self):
        self.file_path = fr'{os.getcwd()}\data\database.json'

    def save_task(self, task):
        task_dict = task.to_dict()

        file = open(file=self.file_path,mode='a', encoding='utf-8')

        task_dict = str(task_dict).replace("\'", "\"")
        file.write(task_dict)
        file.write("\n")
        file.close()

    def update_task(self, task):
        tasks = self.load_task()
        new_tasks = []

        for item_task in tasks:
            if item_task['identification'] == task.identification:
                new_tasks.append(task)
            else:
                item_task = self.json_to_task(item_task)
                new_tasks.append(item_task)

        self.save_all_tasks(new_tasks)

    def delete_task(self, task):
        tasks = self.load_task()
        new_tasks = []

        for item_task in tasks:
            if item_task['identification'] != task.identification:
                item_task = self.json_to_task(item_task)
                new_tasks.append(item_task)

        self.save_all_tasks(new_tasks)

    def save_all_tasks(self, tasks):
        file_text = ''
        for task in tasks:
            task_dict = str(task.to_dict()).replace("\'", "\"")

            if file_text == '':
                file_text = task_dict + '\n'
            else:
                file_text = file_text + task_dict + '\n'

        self.clean_file()
        self.write_all_file(file_text)


    def clean_file(self):
        file = open(file=self.file_path,mode='w', encoding='utf-8')
        file.close()

    def write_all_file(self, text):
        file = open(file=self.file_path,mode='w', encoding='utf-8')
        file.write(text)
        file.close()

    def load_task(self):
        file = open(file=self.file_path,mode='r', encoding='utf-8')
        file_data = file.readlines()

        tasks = []

        for line in file_data:
            task = json.loads(line)
            tasks.append(task)
        return tasks

    def filter_task_by_status(self, status):
        tasks = self.load_task()
        filtered_list = [self.json_to_task(item) for item in tasks if item['status'] == status]
        return filtered_list

    def json_to_task(self, json):
        task = Task().set(json['identification'], json['description'], json['status'], json['created_at'], json['updated_at'])
        return task

    def get_task_by_id(self, identification):

        tasks = self.load_task()
        for item_task in tasks:
            item_task = self.json_to_task(item_task)
            if item_task.identification == identification:
                return item_task

        return None

class TaskManager:

    def __init__(self):
        self.persistence = Persistence()

    def create_task(self,description):
        task = Task()
        identification = self.generate_task_id()

        task.create(identification, description)

        self.persistence.save_task(task)

    def generate_task_id(self):
        tasks = self.persistence.load_task()

        if len(tasks) > 0:
            last_task = tasks[-1]
            new_id = int(last_task['identification']) + 1
        else:
            new_id = 1
        return new_id

    def list_tasks(self):
        tasks = self.persistence.load_task()
        for task in tasks:
            task = Task().set(task['identification'], task['description'], task['status'], task['created_at'], task['updated_at'])
            print(task.to_string())


    def update_task_status(self, identification, new_status):

        task_updated = self.persistence.get_task_by_id(identification)

        if task_updated is None:
            print(f'Task with ID {identification} was not found')
        else:
            task_updated.status = new_status
            task_updated.updated_at = datetime.datetime.now()

            self.persistence.update_task(task_updated)

    def update_task_description(self, identification, description):
        task_updated = self.persistence.get_task_by_id(identification)

        if task_updated is None:
            print(f'Task with ID {identification} was not found')
        else:
            task_updated.description = description
            task_updated.updated_at = datetime.datetime.now()

            self.persistence.update_task(task_updated)

    def delete_task(self, identification):

        task_deleted = self.persistence.get_task_by_id(identification)
        if task_deleted is None:
            print(f'Task with ID {identification} was not found')
        else:
            self.persistence.delete_task(task_deleted)

    def filter_task_by_status(self, status):

        status = Status().get_number(status)

        filtered_list = self.persistence.filter_task_by_status(status)
        for item in filtered_list:
            print(item.to_string())







