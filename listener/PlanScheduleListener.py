from listener.BaseListener import BaseListener


class PlanScheduleListener(BaseListener):
    def __init__(self):
        super().__init__()

    def get_tasks(self, plan_id):
        db_manager = self.system.db_manager
        tasks_table = db_manager.tasks_table

        return tasks_table.get_data(plan_id)
