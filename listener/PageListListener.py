from listener.BaseListener import BaseListener


class PageListListener(BaseListener):
    def __init__(self):
        super().__init__()
        self.temp_user_id = "test_id"

    def add_plan(self, name, goal, description):
        db_manager = self.system.db_manager
        plans_table = db_manager.plans_table

        plan_id = plans_table.add_data(self.temp_user_id)
        plans_table.update_data(plan_id, name, goal, description)

    def get_plans(self):
        db_manager = self.system.db_manager
        plans_table = db_manager.plans_table

        return plans_table.show_data(self.temp_user_id)

    def remove_all_plans(self):
        db_manager = self.system.db_manager
        plans_table = db_manager.plans_table

        plans_table.remove_data_by_user_id(self.temp_user_id)
