import sqlite3
import uuid
from abc import ABC, abstractmethod


def generate_uuid():
    return str(uuid.uuid4())


class Table(ABC):
    def __init__(self):
        pass

    def connect_db(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        return conn, cursor

    def disconnect_db(self, conn):
        conn.close()

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def remove_table(self):
        pass


class UsersTable(Table):
    def __init__(self):
        super().__init__()

    def create_table(self):
        # 테이블 생성
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT
            )
            ''')

        # 변경 사항을 저장합니다.
        conn.commit()

    def remove_table(self):
        # 테이블 삭제
        cursor.execute('DROP TABLE IF EXISTS users')

        # 변경 사항을 저장합니다.
        conn.commit()

    def add_data(self, name):
        user_id = generate_uuid()

        # 데이터 삽입
        cursor.execute('''
        INSERT INTO users (user_id, name) VALUES (?, ?)
        ''', (user_id, name))

        # 변경 사항을 저장합니다.
        conn.commit()

        return user_id

    def remove_data(self, user_id):
        # 데이터 삭제
        cursor.execute('''
            DELETE FROM users WHERE user_id = ?
            ''', (user_id,))

        # 변경 사항을 저장합니다.
        conn.commit()

    def show_data(self):
        # 데이터 조회
        cursor.execute('SELECT * FROM users')

        # 결과를 가져옵니다.
        rows = cursor.fetchall()

        # 가져온 데이터를 출력합니다.
        print(f"found data: {len(rows)}")
        for row in rows:
            print(row)


class PlansTable(Table):
    def __init__(self):
        super().__init__()

        self.init_plan_name = "the name"
        self.init_plan_goal = "the goal"
        self.init_plan_description = "the description"

    def create_table(self):
        conn, cursor = self.connect_db()
        
        # 테이블 생성
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS plans (
            plan_id TEXT PRIMARY KEY,
            user_id TEXT,
            name TEXT,
            goal TEXT,
            description TEXT
        )
        ''')

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

    def remove_table(self):
        conn, cursor = self.connect_db()

        # 테이블 삭제
        cursor.execute('DROP TABLE IF EXISTS plans')

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

    def add_data(self, user_id):
        conn, cursor = self.connect_db()

        plan_id = generate_uuid()

        # 데이터 삽입
        cursor.execute('''
        INSERT INTO plans (plan_id, user_id, name, goal, description) VALUES (?, ?, ?, ?, ?)
        ''', (plan_id, user_id, self.init_plan_name, self.init_plan_goal, self.init_plan_description))

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

        return plan_id

    def remove_data(self, plan_id):
        conn, cursor = self.connect_db()

        # 데이터 삭제
        cursor.execute('''
            DELETE FROM plans WHERE plan_id = ?
            ''', (plan_id,))

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

    def remove_data_by_user_id(self, user_id):
        conn, cursor = self.connect_db()

        # 데이터 삭제
        cursor.execute('''
                    DELETE FROM plans WHERE user_id = ?
                    ''', (user_id,))

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

    def show_data(self, user_id):
        conn, cursor = self.connect_db()

        # 데이터 조회
        cursor.execute('SELECT * FROM plans WHERE user_id = ?', (user_id, ))

        # 결과를 가져옵니다.
        rows = cursor.fetchall()

        # 가져온 데이터를 출력합니다.
        # print(f"found data: {len(rows)}")
        # for row in rows:
        #     print(row)

        self.disconnect_db(conn)

        return rows

    def get_data(self, plan_id):
        conn, cursor = self.connect_db()

        # 데이터 조회
        cursor.execute('SELECT * FROM plans WHERE plan_id = ?', (plan_id,))

        # 결과를 가져옵니다.
        rows = cursor.fetchall()

        self.disconnect_db(conn)

        return rows[0]

    def update_data(self, plan_id, name, goal, description):
        conn, cursor = self.connect_db()

        # 데이터 업데이트
        cursor.execute('''
        UPDATE plans SET name = ?, goal = ?, description = ? WHERE plan_id = ?
        ''', (name, goal, description, plan_id))

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)


class TasksTable(Table):
    def __init__(self):
        super().__init__()

    def create_table(self):
        conn, cursor = self.connect_db()

        # 테이블 생성
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id TEXT PRIMARY KEY,
            plan_id TEXT,
            type TEXT,
            name TEXT,
            description TEXT,
            trigger_time TEXT,
            start_time TEXT,
            end_time TEXT,
            time_list TEXT
        )
        ''')

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

    def remove_table(self):
        conn, cursor = self.connect_db()

        # 테이블 삭제
        cursor.execute('DROP TABLE IF EXISTS tasks')

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

    def add_data(self, task_id, plan_id, task_type, name, description, trigger_time, start_time, end_time, time_list):
        conn, cursor = self.connect_db()

        # 데이터 삽입
        cursor.execute('''
        INSERT INTO tasks (task_id, plan_id, type, name, description, trigger_time, start_time, end_time, time_list) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (task_id, plan_id, task_type, name, description, trigger_time, start_time, end_time, time_list))

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

        return task_id

    def update_data(self, task_id, task_type, name, description, trigger_time, start_time, end_time, time_list):
        conn, cursor = self.connect_db()

        # 데이터 업데이트
        cursor.execute('''
        UPDATE tasks SET type = ?, name = ?, description = ?, trigger_time = ?, start_time = ?, end_time = ?, time_list = ? WHERE task_id = ?
        ''', (task_type, name, description, trigger_time, start_time, end_time, time_list, task_id))

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

    def remove_data(self, task_id):
        conn, cursor = self.connect_db()

        # 데이터 삭제
        cursor.execute('''
            DELETE FROM tasks WHERE task_id = ?
            ''', (task_id,))

        # 변경 사항을 저장합니다.
        conn.commit()

        self.disconnect_db(conn)

    def get_tasks(self, plan_id):
        conn, cursor = self.connect_db()

        # 데이터 조회
        cursor.execute('SELECT * FROM tasks WHERE plan_id = ?', (plan_id, ))

        # 결과를 가져옵니다.
        rows = cursor.fetchall()

        self.disconnect_db(conn)

        return rows

    def get_task(self, task_id):
        conn, cursor = self.connect_db()

        # 데이터 조회
        cursor.execute('SELECT * FROM tasks WHERE task_id = ?', (task_id,))

        # 결과를 가져옵니다.
        rows = cursor.fetchall()

        self.disconnect_db(conn)

        return rows[0]
