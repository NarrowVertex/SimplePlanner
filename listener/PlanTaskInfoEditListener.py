from listener.BaseListener import BaseListener


class PlanTaskInfoEditListener(BaseListener):
    def __init__(self):
        super().__init__()

    def change_task_info(self, new_task):
        db_manager = self.system.db_manager
        db_manager.update_task(new_task)

    def get_task(self, task_id):
        db_manager = self.system.db_manager
        return db_manager.get_task(task_id)

    def remove_task(self, task_id):
        db_manager = self.system.db_manager
        db_manager.remove_task(task_id)
