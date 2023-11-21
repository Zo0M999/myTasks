import mysql.connector


class MyTasks:
    def __init__(self):
        self.db = mysql.connector.connect(
                host="localhost",
                user="mysql",
                password="mysql",
            )
        self.cursor = self.db.cursor()
        self.setup_database()

    def setup_database(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS mytasks_db')
        self.cursor.execute('USE mytasks_db')
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mytasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task_name VARCHAR(255) NOT NULL,
                task_description TEXT,
                completed BOOLEAN DEFAULT 0
            )
        """)
        self.db.commit()

    def show_tasks(self):
        self.cursor.execute('SELECT * FROM mytasks')
        return self.cursor.fetchall()

    def add_task(self, task_name, task_description=''):
        sql = 'INSERT INTO mytasks (task_name, task_description) VALUES (%s, %s)'
        self.cursor.execute(sql, (task_name, task_description))
        self.db.commit()

    def completed_task(self, task_name):
        sql = 'UPDATE mytasks SET completed = 1 WHERE task_name = %s'
        self.cursor.execute(sql, (task_name,))
        self.db.commit()

    def del_task(self):
        sql = 'DELETE FROM mytasks WHERE completed = 1'
        self.cursor.execute(sql)
        self.db.commit()
