from abc import ABC


class BaseTask(ABC):
    def __init__(self, task_type, plan_id, name, description):
        self.task_type = task_type
        self.plan_id = plan_id
        self.name = name
        self.description = description


class TriggerTask(BaseTask):
    def __init__(self, plan_id, name, description, trigger_time):
        super().__init__("trigger", plan_id, name, description)
        self.trigger_time = trigger_time


class TemporalTask(BaseTask):
    def __init__(self, plan_id, name, description, start_time, end_time):
        super().__init__("temporal", plan_id, name, description)
        self.start_time = start_time
        self.end_time = end_time


class PeriodicTask(BaseTask):
    def __init__(self, plan_id, name, description, start_time, end_time, time_list):
        super().__init__("periodic", plan_id, name, description)
        self.start_time = start_time
        self.end_time = end_time
        self.time_list = time_list


