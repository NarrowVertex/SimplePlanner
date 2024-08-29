import sqlite3
import uuid
from abc import ABC, abstractmethod


def generate_uuid():
    return str(uuid.uuid4())


class Table(ABC):
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()

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
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT
            )
            ''')

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def remove_table(self):
        # 테이블 삭제
        self.cursor.execute('DROP TABLE IF EXISTS users')

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def add_data(self, name):
        user_id = generate_uuid()

        # 데이터 삽입
        self.cursor.execute('''
        INSERT INTO users (user_id, name) VALUES (?, ?)
        ''', (user_id, name))

        # 변경 사항을 저장합니다.
        self.conn.commit()

        return user_id

    def remove_data(self, user_id):
        # 데이터 삭제
        self.cursor.execute('''
            DELETE FROM users WHERE user_id = ?
            ''', (user_id,))

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def show_data(self):
        # 데이터 조회
        self.cursor.execute('SELECT * FROM users')

        # 결과를 가져옵니다.
        rows = self.cursor.fetchall()

        # 가져온 데이터를 출력합니다.
        print(f"found data: {len(rows)}")
        for row in rows:
            print(row)


class SchedulesTable(Table):
    def __init__(self):
        super().__init__()

    def create_table(self):
        # 테이블 생성
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS schedules (
            schedule_id TEXT PRIMARY KEY,
            user_id TEXT,
            name TEXT,
            goal TEXT,
            description TEXT
        )
        ''')

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def remove_table(self):
        # 테이블 삭제
        self.cursor.execute('DROP TABLE IF EXISTS schedules')

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def add_data(self, user_id, name, goal, description):
        schedule_id = generate_uuid()

        # 데이터 삽입
        self.cursor.execute('''
        INSERT INTO plans (schedule_id, user_id, name, goal, description) VALUES (?, ?, ?, ?, ?)
        ''', (schedule_id, user_id, name, goal, description))

        # 변경 사항을 저장합니다.
        self.conn.commit()

        return schedule_id

    def remove_data(self, schedule_id):
        # 데이터 삭제
        self.cursor.execute('''
            DELETE FROM plans WHERE schedule_id = ?
            ''', (schedule_id,))

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def show_data(self):
        # 데이터 조회
        self.cursor.execute('SELECT * FROM schedules')

        # 결과를 가져옵니다.
        rows = self.cursor.fetchall()

        # 가져온 데이터를 출력합니다.
        print(f"found data: {len(rows)}")
        for row in rows:
            print(row)


class TasksTable(Table):
    def __init__(self):
        super().__init__()

    def create_table(self):
        # 테이블 생성
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id TEXT PRIMARY KEY,
            schedule_id TEXT,
            name TEXT,
            start_date TEXT,
            end_date TEXT
        )
        ''')

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def remove_table(self):
        # 테이블 삭제
        self.cursor.execute('DROP TABLE IF EXISTS tasks')

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def add_data(self, schedule_id, name, start_date, end_date):
        task_id = generate_uuid()

        # 데이터 삽입
        self.cursor.execute('''
        INSERT INTO tasks (task_id, schedule_id, name, start_date, end_date) VALUES (?, ?, ?, ?, ?)
        ''', (task_id, schedule_id, name, start_date, end_date))

        # 변경 사항을 저장합니다.
        self.conn.commit()

        return task_id

    def remove_data(self, task_id):
        # 데이터 삭제
        self.cursor.execute('''
            DELETE FROM tasks WHERE task_id = ?
            ''', (task_id,))

        # 변경 사항을 저장합니다.
        self.conn.commit()

    def show_data(self):
        # 데이터 조회
        self.cursor.execute('SELECT * FROM tasks')

        # 결과를 가져옵니다.
        rows = self.cursor.fetchall()

        # 가져온 데이터를 출력합니다.
        print(f"found data: {len(rows)}")
        for row in rows:
            print(row)
