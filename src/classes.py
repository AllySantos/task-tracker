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

    def update(self, status):
        time.sleep(1)
        self.status = status
        self.updated_at = datetime.datetime.now()

        return self

    def to_string(self):
        status = Status().get_name(self.status)

        created_at = self.datetime_to_string(self.created_at)
        updated_at = self.datetime_to_string(self.updated_at)

        return f"TASK\nID: {self.identification}\tDESCRIPTION: {self.description}\tSTATUS: {status}\tCREATED AT: {created_at}\tUPDATED AT: {updated_at}"

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
            if item_task['identification'] == task['identification']:
                new_tasks.append(task)
            else:
                new_tasks.append(item_task)

        self.save_all_tasks(new_tasks)


    def save_all_tasks(self, tasks):

        tasks = str(tasks)
        print(tasks)


    def load_task(self):
        file = open(file=self.file_path,mode='r', encoding='utf-8')
        file_data = file.readlines()

        tasks = []

        for line in file_data:
            task = json.loads(line)
            tasks.append(task)
        return tasks


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
        last_task = tasks[-1]
        new_id = int(last_task['identification']) + 1
        return new_id

    def list_tasks(self):
        tasks = self.persistence.load_task()
        for task in tasks:
            task = Task().set(task['identification'], task['description'], task['status'], task['created_at'], task['updated_at'])
            print(task.to_string())

    def update_task_status(self, identification, new_status):
        task = Task()
        task.set(identification, '', new_status, '', '')
        print(task)
        self.persistence.update_task(task)







