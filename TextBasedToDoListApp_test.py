import unittest
from unittest.mock import patch
from ToDoList_Final import TextBasedToDoListApp

class TestTextBasedToDoListApp(unittest.TestCase):
    def setUp(self):
        self.app = TextBasedToDoListApp()

    @patch('builtins.input', side_effect=['Special Project 1'])
    def test_delete_special_project(self, mock_input):
        with patch.object(self.app.special_project, 'delete_special_project') as mock_delete_special_project:
            self.app.delete_special_project()

            #ensures delete_special_project method is called with correct arguments
            mock_delete_special_project.assert_called_once_with('Special Project 1')

    @patch('builtins.input', side_effect=['Special Project 1', 'Task Title 1'])
    def test_delete_task_in_project_special_project(self, mock_input):
        with patch.object(self.app.special_project, 'delete_task_in_project') as mock_delete_task_in_project:
            self.app.delete_task_in_project_special_project()

            #ensures delete_task_in_project method is called with correct arguments
            mock_delete_task_in_project.assert_called_once_with('Special Project 1', 'Task Title 1')

    @patch('builtins.input', side_effect=['Test Project', 'Test Task'])
    def test_delete_task_in_project(self, mock_input):
        with patch.object(self.app.special_project, 'delete_task_in_project') as mock_delete_task_in_project:
            self.app.delete_task_in_project_special_project()
            mock_delete_task_in_project.assert_called_once_with('Test Project', 'Test Task')

    @patch('builtins.input', side_effect=['Special Project 1'])
    def test_add_special_project(self, mock_input):
        with patch.object(self.app, 'add_special_project') as mock_add_special_project:
            self.app.add_special_project()

            #ensures that add_special_project method is called
            mock_add_special_project.assert_called_once()

    @patch('builtins.input', side_effect=['Special Project 1', 'Task Title 1'])
    def test_delete_task_in_project(self, mock_input):
        with patch.object(self.app, 'delete_task_in_project') as mock_delete_task_in_project:
            #call method that interacts with input
            self.app.delete_task_in_project('Special Project 1', 'Task Title 1')

            #ensures that method is called
            mock_delete_task_in_project.assert_called_once()

    @patch('ToDoList_Final.TextBasedToDoListApp.view_all_tasks')
    def test_view_all_tasks(self, mock_view_all_tasks):
        with patch('builtins.print') as mock_print:
            self.app.view_all_tasks()

            #ensures that method is called
            mock_view_all_tasks.assert_called_once()


if __name__ == '__main__':
    unittest.main()
