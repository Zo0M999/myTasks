import unittest
from mytasks import MyTasks


class TestMyTasks(unittest.TestCase):
    def setUp(self):
        self.task_name = 'task_1'
        self.task_description = 'task_description_1'
        self.myTasks = MyTasks()

    def tearDown(self):
        self.myTasks._cursor.execute('DROP TABLE IF EXISTS mytasks')
        self.myTasks._db.commit()
        self.myTasks.__del__()

    def test_show_tasks(self):
        self.myTasks.add_task(self.task_name, self.task_description)
        tasks = self.myTasks.show_tasks()
        self.assertEqual(len(tasks), 1)

    def test_add_task(self):
        self.myTasks.add_task(self.task_name, self.task_description)
        self.myTasks._cursor.execute('SELECT * FROM mytasks')
        tasks = self.myTasks._cursor.fetchall()
        self.assertEqual(tasks[0][1], 'task_1')

    def test_completed_task(self):
        self.myTasks.add_task(self.task_name, self.task_description)
        self.myTasks.completed_task(self.task_name)
        self.myTasks._cursor.execute('SELECT completed FROM mytasks WHERE task_name = %s', (self.task_name,))
        res = self.myTasks._cursor.fetchone()
        self.assertEqual(res[0], 1)

    def test_del_task(self):
        self.myTasks.add_task(self.task_name, self.task_description)
        self.myTasks.completed_task(self.task_name)
        self.myTasks.del_task()
        self.myTasks._cursor.execute('SELECT * FROM mytasks')
        tasks = self.myTasks._cursor.fetchall()
        self.assertEqual(len(tasks), 0)


if __name__ == '__main__':
    unittest.main()
