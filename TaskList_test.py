import unittest
from datetime import datetime
from ToDoList_Final import Task, TaskList

class TestTaskList(unittest.TestCase):
    def setUp(self):
        self.task_list = TaskList()


if __name__ == '__main__':
    unittest.main()
