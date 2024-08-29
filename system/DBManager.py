from system.db.Table import PlansTable


class DBManager:
    def __init__(self):
        self.plans_table = PlansTable()
        self.plans_table.create_table()

    def create_table(self):
        self.plans_table.create_table()

    def add_plan(self, user_id):
        self.plans_table.add_data(user_id)

    def update_plan(self, plan_id, name, goal, description):
        self.plans_table.update_data(plan_id, name, goal, description)

    def remove_plan(self, plan_id):
        self.plans_table.remove_data(plan_id)

    def show_plans(self, user_id):
        self.plans_table.show_data(user_id)

