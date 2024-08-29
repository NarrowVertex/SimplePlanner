import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()



def create_table():
    # 테이블 생성
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS plan (
        id INTEGER PRIMARY KEY,
        name TEXT,
        goal TEXT,
        description TEXT,
        mission_id TEXT,
        history_id TEXT 
    )
    ''')

    # 변경 사항을 저장합니다.
    conn.commit()


def remove_table():
    # 테이블 삭제
    cursor.execute('DROP TABLE IF EXISTS plan')

    # 변경 사항을 저장합니다.
    conn.commit()


def insert_data():
    # 데이터 삽입
    cursor.execute('''
    INSERT INTO plan (name, goal, description) VALUES (?, ?, ?)
    ''', ('John Doe', 'the goal', 'the description'))

    # 변경 사항을 저장합니다.
    conn.commit()


def remove_data():
    # 데이터 삭제
    cursor.execute('''
    DELETE FROM plan WHERE name = ?
    ''', ('John Doe',))

    # 변경 사항을 저장합니다.
    conn.commit()


def show_data():
    # 데이터 조회
    cursor.execute('SELECT * FROM plan')

    # 결과를 가져옵니다.
    rows = cursor.fetchall()

    # 가져온 데이터를 출력합니다.
    print(f"found data: {len(rows)}")
    for row in rows:
        print(row)


def update_data():
    # 데이터 업데이트
    cursor.execute('''
    UPDATE plan SET goal = ? WHERE name = ?
    ''', ('the second goal', 'John Doe'))

    # 변경 사항을 저장합니다.
    conn.commit()


create_table()
# remove_table()

insert_data()
update_data()
# remove_data()
show_data()

# 연결 종료
conn.close()
