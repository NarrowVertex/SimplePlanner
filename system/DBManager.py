from system.db.Table import PlansTable, TasksTable
from system.task.Task import BaseTask, TriggerTask, TemporalTask, PeriodicTask


class DBManager:
    def __init__(self):
        self.plans_table = PlansTable()
        self.tasks_table = TasksTable()

        self.create_table()

    def create_table(self):
        self.plans_table.create_table()
        self.tasks_table.create_table()

    def add_plan(self, user_id):
        self.plans_table.add_data(user_id)

    def update_plan(self, plan_id, name, goal, description):
        self.plans_table.update_data(plan_id, name, goal, description)

    def remove_plan(self, plan_id):
        self.plans_table.remove_data(plan_id)

    def show_plans(self, user_id):
        self.plans_table.show_data(user_id)

    def add_task(self, task):
        if isinstance(task, TriggerTask):
            self.tasks_table.add_data(task.plan_id, task.name, task.description,
                                      task.trigger_time, "", "", "")
        elif isinstance(task, TemporalTask):
            self.tasks_table.add_data(task.plan_id, task.name, task.description,
                                      "", task.start_time, task.end_time, "")
        elif isinstance(task, PeriodicTask):
            self.tasks_table.add_data(task.plan_id, task.name, task.description,
                                      "", task.start_time, task.end_time, task.time_list)
        else:
            print("Wrong task type!")
            return

    def get_tasks(self, plan_id):
        return self.tasks_table.get_data(plan_id)

