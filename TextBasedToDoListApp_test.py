import unittest
from datetime import datetime, timedelta
from unittest.mock import patch
from io import StringIO
from ToDoList_Final import TextBasedToDoListApp, Task, TaskList, SpecialProjects

class TestTextBasedToDoListApp(unittest.TestCase):

    def setUp(self):
        self.app = TextBasedToDoListApp()

    def test_add_task(self):
        with patch('builtins.input', side_effect=['Test Task', '01/01/23', 'Test Description', 'Test Category']):
            self.app.add_task()

        task_list = self.app.task_list
        self.assertIn('Test Category', task_list.categories)
        tasks_in_category = task_list.categories['Test Category']
        self.assertEqual(len(tasks_in_category), 1)
        task = tasks_in_category[0]
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.due_date, datetime(2023, 1, 1))
        self.assertEqual(task.description, 'Test Description')
        self.assertEqual(task.completed, False)

    def test_delete_task(self):
        task = Task('Test Task', datetime(2023, 1, 1), 'Test Description', 'Test Category')
        self.app.task_list.add_task(task)

        with patch('builtins.input', return_value='Test Task'):
            self.app.delete_task()

        tasks_in_category = self.app.task_list.categories.get('Test Category', [])
        self.assertEqual(len(tasks_in_category), 0)

    def test_edit_task(self):
        task = Task('Old Title', datetime(2023, 1, 1), 'Old Description', 'Old Category')
        self.app.task_list.add_task(task)

        with patch('builtins.input', side_effect=['Old Title', 'New Title', '02/02/23', 'New Description', 'New Category', '4']):
            self.app.edit_task()

        tasks_in_old_category = self.app.task_list.categories.get('Old Category', [])
        self.assertEqual(len(tasks_in_old_category), 0)

        tasks_in_new_category = self.app.task_list.categories.get('New Category', [])
        self.assertEqual(len(tasks_in_new_category), 1)
        new_task = tasks_in_new_category[0]
        self.assertEqual(new_task.title, 'New Title')
        self.assertEqual(new_task.due_date, datetime(2023, 2, 2))
        self.assertEqual(new_task.description, 'New Description')
        self.assertEqual(new_task.completed, False)

if __name__ == '__main__':
    unittest.main()
