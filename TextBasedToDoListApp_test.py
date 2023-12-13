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



if __name__ == '__main__':
    unittest.main()
