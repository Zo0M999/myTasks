import mysql.connector


class MyTasks:
    def __init__(self):
        self._db = mysql.connector.connect(
                host="localhost",
                user="mysql",
                password="mysql",
            )
        self._cursor = self._db.cursor()
        self.__setup_database()

    def __setup_database(self):
        self._cursor.execute('CREATE DATABASE IF NOT EXISTS mytasks_db')
        self._cursor.execute('USE mytasks_db')
        self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS mytasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task_name VARCHAR(255) NOT NULL,
                task_description TEXT,
                completed BOOLEAN DEFAULT 0
            )
        """)
        self._db.commit()

    def show_tasks(self):
        self._cursor.execute('SELECT * FROM mytasks')
        return self._cursor.fetchall()

    def add_task(self, task_name, task_description=''):
        sql = 'INSERT INTO mytasks (task_name, task_description) VALUES (%s, %s)'
        self._cursor.execute(sql, (task_name, task_description))
        self._db.commit()

    def completed_task(self, task_name):
        sql = 'UPDATE mytasks SET completed = 1 WHERE task_name = %s'
        self._cursor.execute(sql, (task_name,))
        self._db.commit()

    def del_task(self):
        sql = 'DELETE FROM mytasks WHERE completed = 1'
        self._cursor.execute(sql)
        self._db.commit()

    def __del__(self):
        self._db.close()
