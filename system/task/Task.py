from abc import ABC


def create_task(task_id, plan_id, task_type, name, description, trigger_time, start_time, end_time, time_list):
    if task_type == "trigger":
        return TriggerTask(task_id, plan_id, name, description, trigger_time)
    elif task_type == "temporal":
        return TemporalTask(task_id, plan_id, name, description, start_time, end_time)
    elif task_type == "periodic":
        return PeriodicTask(task_id, plan_id, name, description, start_time, end_time, time_list)
    else:
        print("Wrong type")
        return None


class BaseTask(ABC):
    def __init__(self, task_id, plan_id, task_type, name, description):
        self.task_id = task_id
        self.plan_id = plan_id
        self.task_type = task_type
        self.name = name
        self.description = description


class TriggerTask(BaseTask):
    def __init__(self, task_id, plan_id, name, description, trigger_time):
        super().__init__(task_id, plan_id, "trigger", name, description)
        self.trigger_time = trigger_time


class TemporalTask(BaseTask):
    def __init__(self, task_id, plan_id, name, description, start_time, end_time):
        super().__init__(task_id, plan_id, "temporal", name, description)
        self.start_time = start_time
        self.end_time = end_time


class PeriodicTask(BaseTask):
    def __init__(self, task_id, plan_id, name, description, start_time, end_time, time_list):
        super().__init__(task_id, plan_id, "periodic", name, description)
        self.start_time = start_time
        self.end_time = end_time
        self.time_list = time_list


