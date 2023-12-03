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

    def test_task_initialization(self):
        #test making sure that the task class is initialized properly
        task = Task(
            self.task_title,
            self.task_due_date,
            self.task_description,
            self.task_category
        )
        
        self.assertEqual(task.title, self.task_title)
        self.assertEqual(task.due_date, self.task_due_date)
        self.assertEqual(task.description, self.task_description)
        self.assertEqual(task.category, self.task_category)
        self.assertFalse(task.completed)

    def test_task_completion(self):
        #test for marking a singular task complete
        task = Task(
            self.task_title,
            self.task_due_date,
            self.task_description,
            self.task_category
        )

        self.assertFalse(task.completed)
        task.completed = True
        self.assertTrue(task.completed)


if __name__ == '__main__':
    unittest.main()