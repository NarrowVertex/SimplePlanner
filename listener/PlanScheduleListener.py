from listener.BaseListener import BaseListener


class PlanScheduleListener(BaseListener):
    def __init__(self):
        super().__init__()

    def get_tasks(self, plan_id):
        db_manager = self.system.db_manager
        return db_manager.get_tasks(plan_id)

    def add_task(self, task):
        db_manager = self.system.db_manager
        db_manager.add_task(task)
