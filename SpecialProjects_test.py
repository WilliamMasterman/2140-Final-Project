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

    def test_add_task_to_project(self):
        task_title = "Test Task"
        task_due_date = datetime(2023, 1, 1)
        task_description = "Test Description"
        task_category = "Test Category"
        task = Task(task_title, task_due_date, task_description, task_category)

        project_name = "Test Project"
        self.special_project.categories[project_name] = []
        self.special_project.add_task_to_project(task, project_name)

        self.assertIn(task, self.special_project.categories[project_name])

    def test_view_tasks_in_project(self):
        task_title = "Test Task"
        task_due_date = datetime(2023, 1, 1)
        task_description = "Test Description"


if __name__ == '__main__':
    unittest.main()
