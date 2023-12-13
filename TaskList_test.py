import unittest
from datetime import datetime
from ToDoList_Final import Task, TaskList

class TestTaskList(unittest.TestCase):
    def setUp(self):
        self.task_list = TaskList()

    def test_mark_task_complete(self):
        #create task and add to task list
        task_title = "Test Task"
        task_due_date = datetime.now()
        task_description = "Test Description"
        task_category = "Test Category"
        task = Task(task_title, task_due_date, task_description, task_category)
        self.task_list.add_task(task)

        #mark task complete
        self.task_list.mark_task_complete(task_title)

        #check if it is correctly maked complete
        for tasks in self.task_list.categories.values():
            for task in tasks:
                if task.title == task_title:
                    self.assertTrue(task.completed, f"Task '{task_title}' should be marked as complete")
                    return

        #if input title is not found, test should fail
        self.fail(f"Task '{task_title}' not found in the task list")



if __name__ == '__main__':
    unittest.main()
