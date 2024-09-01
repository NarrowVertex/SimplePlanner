import uuid
from abc import ABC
from datetime import datetime
from typing import Union


def create_empty_task():
    return create_task("", "", "trigger", "", "", "", "", "", "")


def create_task(task_id, plan_id, task_type, name, description, trigger_time, start_time, end_time, time_list):
    if task_type == "trigger":
        return TriggerTask(plan_id, name, description, trigger_time, task_id=task_id)
    elif task_type == "temporal":
        return TemporalTask(plan_id, name, description, start_time, end_time, task_id=task_id)
    elif task_type == "periodic":
        return PeriodicTask(plan_id, name, description, start_time, end_time, time_list, task_id=task_id)
    else:
        print("Wrong type")
        return None


def create_task_by_list(raw_task):
    return create_task(raw_task[0], raw_task[1], raw_task[2], raw_task[3], raw_task[4], raw_task[5], raw_task[6],
                       raw_task[7], raw_task[8])


def transform_task(task, new_task_type):
    task: Union[BaseTask, TriggerTask, TemporalTask, PeriodicTask]

    if new_task_type == "trigger":
        trigger_time = str(datetime.now())
        return TriggerTask(task.plan_id, task.name, task.description, trigger_time, task_id=task.task_id)
    elif new_task_type == "temporal":
        start_time = str(datetime.today())
        end_time = str(datetime.today())
        if hasattr(task, 'start_time'):
            start_time = task.start_time
        if hasattr(task, 'end_time'):
            end_time = task.end_time

        return TemporalTask(task.plan_id, task.name, task.description, start_time, end_time, task_id=task.task_id)
    elif new_task_type == "periodic":
        start_time = str(datetime.today())
        end_time = str(datetime.today())
        time_list = ""

        if hasattr(task, 'start_time'):
            start_time = task.start_time
        if hasattr(task, 'end_time'):
            end_time = task.end_time

        return PeriodicTask(task.plan_id, task.name, task.description, start_time, end_time, time_list,
                            task_id=task.task_id)
    else:
        print("Wrong type")
        return None

class BaseTask(ABC):
    def __init__(self, task_id, plan_id, task_type, name, description):
        if task_id is None:
            self.task_id = str(uuid.uuid4())
        else:
            self.task_id = task_id
        self.plan_id = plan_id
        self.task_type = task_type
        self.name = name
        self.description = description


class TriggerTask(BaseTask):
    def __init__(self, plan_id, name, description, trigger_time, task_id=None):
        super().__init__(task_id, plan_id, "trigger", name, description)
        self.trigger_time = trigger_time


class TemporalTask(BaseTask):
    def __init__(self, plan_id, name, description, start_time, end_time, task_id=None):
        super().__init__(task_id, plan_id, "temporal", name, description)
        self.start_time = start_time
        self.end_time = end_time


class PeriodicTask(BaseTask):
    def __init__(self, plan_id, name, description, start_time, end_time, time_list, task_id=None):
        super().__init__(task_id, plan_id, "periodic", name, description)
        self.start_time = start_time
        self.end_time = end_time
        self.time_list = time_list
