import datetime
import time
import os


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

    datetime_format = '%d/%m/%Y-%H:%M:%S'

    def __init__(self):
        self.identification = self.description = self.status = self.created_at = self.updated_at = None

    def create(self, identification, description, status):
        self.identification = identification
        self.description = description
        self.status = Status.TO_DO
        self.created_at = datetime.datetime.now()
        self.updated_at = '-'

        return self

    def update(self, status):
        time.sleep(1)
        self.status = status
        self.updated_at = datetime.datetime.now()

        return self

    def print(self):
        status = Status().get_name(self.status)

        created_at = datetime.datetime.strftime(self.created_at, self.datetime_format)

        updated_at = self.updated_at
        if type(updated_at) != str:
            updated_at = datetime.datetime.strftime(self.updated_at, self.datetime_format)

        print(f"TASK\nID: {self.identification}\tDESCRIPTION: {self.description}\tSTATUS: {status}\tCREATED AT: {created_at}\tUPDATED AT: {updated_at}")

    def to_dict(self):
        task_dict = {'identification': self.identification,
                     'description': self.description,
                     'status': self.status,
                     'created_at': self.status,
                     'updated_at':self.updated_at}
        return task_dict


class Persistence():

    file_path = fr'{os.getcwd()}\data\database.json'

    def __init__(self):
        pass


    def save_task(self, task):
        task_dict = task.to_dict()

        file = open(file=self.file_path,mode='a', encoding='utf-8')
        file.write(task_dict)
        file.close()






