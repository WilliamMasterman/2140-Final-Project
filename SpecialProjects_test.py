import unittest
from datetime import datetime
from ToDoList_Final import Task, TaskList, SpecialProjects

class TestSpecialProjects(unittest.TestCase):
    def setUp(self):
        self.special_project = SpecialProjects()

    def test_add_special_project(self):
        #tests the creation of a special project
        project_name = "Test Project"
        self.special_project.categories[project_name] = []
        self.assertIn(project_name, self.special_project.categories)

    def test_delete_special_project(self):
        #tests deleting a special project
        project_name = "Test Project"
        self.special_project.categories[project_name] = []
        self.special_project.delete_special_project(project_name)
        self.assertNotIn(project_name, self.special_project.categories)



if __name__ == '__main__':
    unittest.main()
