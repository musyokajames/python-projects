class Task:
    def __init__(self,task_details,completed = False):
        self.task_details = task_details
        self.completed = completed

    def __str__(self):
        return self.task_details