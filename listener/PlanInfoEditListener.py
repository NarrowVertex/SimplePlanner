from listener.BaseListener import BaseListener


class PlanInfoEditListener(BaseListener):
    def __init__(self):
        super().__init__()

    def change_plan_info(self, plan_id, new_name, new_goal, new_description):
        db_manager = self.system.db_manager
        plans_table = db_manager.plans_table

        plans_table.update_data(plan_id, new_name, new_goal, new_description)

    def get_plan(self, plan_id):
        db_manager = self.system.db_manager
        plans_table = db_manager.plans_table

        return plans_table.get_data(plan_id)
