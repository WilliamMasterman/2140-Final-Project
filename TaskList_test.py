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



if __name__ == '__main__':
    unittest.main()
