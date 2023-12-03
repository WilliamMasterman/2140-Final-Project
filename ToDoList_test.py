import unittest
from datetime import datetime
from ToDoList_Final import Task

class TestTaskClass(unittest.TestCase):
    def setUp(self):
        # Initialize common data for tests
        self.task_title = "Sample Task"
        self.task_due_date = datetime(2023, 1, 1)
        self.task_description = "This is a sample task description."
        self.task_category = "Sample Category"