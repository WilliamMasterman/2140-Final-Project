import matplotlib.pyplot as plt
from datetime import datetime

class Task:
    def __init__(self, title, due_date, description, category, completed=False):
        """
        This represents an individual task

        Returns: None

        Arguments:
            title (str): Title of the task.
            due_date (datetime): Due date of the task
            description (str): Description of the task
            category (str): Category of the task
        """
        self.title = title
        self.due_date = due_date
        self.description = description
        self.category = category
        self.completed = completed
        
class TaskList:
    def __init__(self):
        """
        Initializes category object for class

        Returns: None

        Arguments: None
        """
        self.categories = {}

    
    def add_task(self, task):
        """
        This adds a task to the corresponding category

        Returns: None

        Arguments: Task (task): task object to be added
        """
        if task.category not in self.categories:
            self.categories[task.category] = []
        self.categories[task.category].append(task)


    def delete_task(self, title: str):
        """
        Deletes a task based on its title

        Returns: None
        
        Arguments: title (str): The title of the task
        """
        if not isinstance(title, str):
            raise TypeError("Invalid input type")
        
        for category, tasks in self.categories.items():
            for task in tasks:
                if task.title == title:
                    tasks.remove(task)
                    print(f"Task '{title}' deleted")

                    #if the category doesnt have anything in it, remove the category
                    #Keeps the category around until its not useful anymore
                    if not tasks:
                        del self.categories[category]
                        print(f"Category '{category}' removed")

                    return

        #if the title isnt found, tell user
        print(f"Task '{title}' not found")


    def view_tasks(self):
        """
        Creates formatted str for all aspects of task

        Returns: A string containing information about each task for each defining category

        Arguments: None
        """
        tasks_str = ""
        for category, tasks in self.categories.items():
            tasks_str += f"\n===== Category: {category} =====\n"
            #Displaying the information given via user input
            for task in tasks:
                tasks_str += f"Title: {task.title}\n"
                tasks_str += f"Due Date: {task.due_date}\n"
                tasks_str += f"Description: {task.description}\n"
                tasks_str += f"Category: {task.category}\n"
                tasks_str += f"Completed: {'Yes' if task.completed else 'No'}\n\n"
        return tasks_str


    def edit_task(self, title, new_title, new_due_date, new_description, new_category):
        """
        Edits a task with new information

        Returns: None

        Arguments:
            title (str): title of the task to be edited
            new_title (str): New title of the task
            new_due_date (datetime): New due date of the task
            new_description (str): New description of the task
            new_category (str): New category of the task
        """
        for tasks in self.categories.values():
            for task in tasks:
                # goes through and checks to see if the edited values are correct
                if task.title == title:
                    task.title = new_title
                    task.due_date = new_due_date
                    task.description = new_description
                    task.category = new_category
                    print(f"Task '{title}' edited")
                    return

        #if the title is not found print an error and restart the menu
        print(f"Task '{title}' not found")


    def mark_task_complete(self, title):
        """
        Marks a task as complete

        Returns: None
        prints a message about whether the task was marked complete
        
        Arguments: title (str): the title of the task that is to be completed
        """
        for tasks in self.categories.values():
            # goes through the value pair of the dict and changes task.completed to be true
            for task in tasks:
                if task.title == title:
                    task.completed = True
                    print(f"Task '{title}' marked as complete")
                    return

        #if input title is not found throw error
        print(f"Task '{title}' not found")

class SpecialProjects(TaskList):

    def add_task_to_project(self, task, project_name):
        """
        Adds a task to a specific project

        Returns: None

        Arguments:
            task (Task): the task to be added to the project
            project_name (str): the name of the project to which the task will be added
        """
        #this checks to see if the project name is in the categories dict
        #if not it creates an emoty list
        # if it is then it appends a task
        if project_name not in self.categories:
            self.categories[project_name] = []
        self.categories[project_name].append(task)

    def view_completion_rate(self):
        """
        Calculates and returns the completion rate of tasks that are not overdue

        Returns: str - a string indicating the completion rate

        Arguments: None
        """
        total_tasks = 0
        completed_tasks = 0

        #iterates through all tasks and adds one to the total task counter
        for tasks in self.categories.values():
            for task in tasks:
                total_tasks += 1
                #checks to see if the task was completed before the due date,
                #if yes then it adds one to the completed task counter
                if datetime.now() <= task.due_date and task.completed:
                    completed_tasks += 1

        #calculates the completion rate
        if total_tasks == 0:
            completion_rate = 0
        else:
            completion_rate = (completed_tasks / total_tasks) * 100

        #returns the completion rate to 2 decimal points
        return f"Completion Rate: {completion_rate:.2f}%"
    
    def view_tasks_in_project(self, project_name):
        """
        find and format information about tasks in a specific project

        Returns:
            str: a formatted string containing information about tasks in the specified project

        Arguments: project_name (str): The name of the desired project to view
        """
        tasks_str = ""
        if project_name in self.categories:
            #iterates through project in categories dict and then concatenates
            #to tasks str. Very similar to view task method.
            for task in self.categories[project_name]:
                tasks_str += f"Title: {task.title}\n"
                tasks_str += f"Due Date: {task.due_date}\n"
                tasks_str += f"Description: {task.description}\n"
                tasks_str += f"Category: {task.category}\n"
                tasks_str += f"Completed: {'Yes' if task.completed else 'No'}\n\n"
        else:
            tasks_str = f"No tasks found in project '{project_name}'"

        return tasks_str
    
    def edit_task_in_project(self, project_name, title, new_title, new_due_date, new_description, new_category):
        """
        edits a task within a specific project

        Returns: None

        Args:
            project_name (str): name of the project containing the task
            title (str): title of the task to be edited
            new_title (str): new title fortask
            new_due_date (datetime): new due date for task
            new_description (str): new description for task
            new_category (str): new category for task
        """
        if project_name in self.categories:
            for task in self.categories[project_name]:
                if task.title == title:
                    task.title = new_title
                    task.due_date = new_due_date
                    task.description = new_description
                    task.category = new_category
                    print(f"Task '{title}' in project '{project_name}' edited")
                    return

            print(f"Task '{title}' in project '{project_name}' not found")
        else:
            print(f"Project '{project_name}' not found")

    def mark_task_complete_in_project(self, project_name, title):
        """
        Mark a task within a specific project as complete

        Returns: None

        Args:
            project_name (str): name of the project containing the task
            title (str): title of the task to be marked as complete
        """
        if project_name in self.categories:
            for task in self.categories[project_name]:
                if task.title == title:
                    task.completed = True
                    print(f"Task '{title}' in project '{project_name}' marked as complete")
                    return

            print(f"Task '{title}' in project '{project_name}' not found")
        else:
            print(f"Project '{project_name}' not found")

class TextBasedToDoListApp:
    def __init__(self):
        """
        This represents an interactive task app

        Returns: None

        Arguments:
            task_list (TaskList): task list object to be used and displayed
            special_project (SpecialProjects): special projects object to be used and displayed
            completion_rates (list): Completion rate list to keep track of completion rate
        """
        self.task_list = TaskList()
        self.special_project = SpecialProjects()
        self.completion_rates = []

    def run(self):
        """
        run the text based to do List app

        Returns: None

        Args: None
        """
        while True:
            print("\n===== To-Do List =====")
            print("1. Tasks")
            print("2. Special Projects")
            print("0. Exit")

            category_choice = input("Enter your choice: ")

            if category_choice == "1":
                self.run_task_menu()
            elif category_choice == "2":
                self.run_special_project_menu()
            elif category_choice == "0":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def run_task_menu(self):
        """
        run the text based task menu

        Returns: None

        Args: None
        """
        while True:
            print("\n===== Tasks =====")
            print("1. Add Task")
            print("2. Edit Task")
            print("3. Mark Task Complete")
            print("4. View Completion Rate")
            print("5. Delete Task")
            print("0. Back to Main Menu")

            task_choice = input("Enter your choice: ")

            if task_choice == "1":
                self.add_task()
            elif task_choice == "2":
                self.edit_task()
            elif task_choice == "3":
                self.mark_task_complete()
            elif task_choice == "4":
                self.view_completion_rate()
            elif task_choice == "5":
                self.delete_task()
            elif task_choice == "0":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def run_special_project_menu(self):
        """
        run the text based special projects menu

        Returns: None

        Args: None
        """
        while True:
            print("\n===== Special Projects =====")
            print("1. View Tasks in Special Project")
            print("2. Add Task to Special Project")
            print("3. Edit Task in Special Project")
            print("4. Mark Task Complete in Special Project")
            print("5. View Completion Rate for Special Project")
            print("6. Delete Task in Special Project")
            print("7. Delete Special Project")
            print("0. Back to Main Menu")

            special_project_choice = input("Enter your choice: ")

            if special_project_choice == "1":
                self.view_tasks_in_special_project()
            elif special_project_choice == "2":
                self.add_task_to_special_project()
            elif special_project_choice == "3":
                self.edit_task_in_special_project()
            elif special_project_choice == "4":
                self.mark_task_complete_in_special_project()
            elif special_project_choice == "5":
                self.view_completion_rate_for_special_project()
            elif special_project_choice == "6":
                self.delete_task_in_special_project()
            elif special_project_choice == "7":
                self.delete_special_project()
            elif special_project_choice == "0":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def add_task(self):
        """
        Adds a new task to the task list

        Raises:
            ValueError: If there is an issue with the input
            TypeError: If there is a type mismatch in the input

        Returns: None

        Args: None
        """
        while True:
            try:
                title = input("Enter task title: ")
                due_date_str = input("Enter due date (day/month/year): ")

                #this removes extra spaces from input
                due_date_str = due_date_str.replace("'", "").replace("(", "").replace(")", "")

                due_date = datetime.strptime(due_date_str, "%d/%m/%y")
                description = input("Enter task description: ")
                category = input("Enter task category: ")

                task = Task(title, due_date, description, category)
                self.task_list.add_task(task)
                print("Task successfully added!")
                break
            except (TypeError, ValueError) as e:
                print(f"Error: {e}. Please enter valid input.")

    def delete_task(self):
        """
        Delete a task from the task list based on title

        Raises: TypeError: If there is an issue with the input type

        Returns: None

        Args: None
        """
        while True:
            try:
                title = input("Enter the title of the task to delete: ")
                self.task_list.delete_task(title)
                break
            except TypeError as e:
                print(f"Error: {e}. Please enter valid input types.")
    def add_task_to_special_project(self):
        """
        Add a task to a special project

        Raises: TypeError: If there is an issue with the input types

        Returns: None

        Args: None
        """
        while True:
            try:
                title = input("Enter the title of the task: ")
                project_name = input("Enter the name of the special project: ")

                task = None
                for tasks in self.task_list.categories.values():
                    for t in tasks:
                        if t.title == title:
                            task = t
                            break

                if task:
                    self.special_project.add_task_to_project(task, project_name)
                    print(f"Task '{title}' added to special project '{project_name}'.")
                    break
                else:
                    print(f"Task '{title}' not found.")
                    break
            except TypeError as e:
                print(f"Error: {e}. Please enter valid input types.")

    def view_tasks_in_special_project(self):
        """
        Display tasks within a selected special project
        
        Raises: ValueError: If there is an issue with the input

        Returns: None

        Args: None
        """
        while True:
            projects = list(self.special_project.categories.keys())
            
            if not projects:
                print("No special projects found.")
                return

            print("\n===== Special Projects =====")
            for idx, project in enumerate(projects, start=1):
                print(f"{idx}. {project}")

            try:
                choice = int(input("Enter the number of the project to view tasks (0 to cancel): "))
                if choice == 0:
                    return
                elif 1 <= choice <= len(projects):
                    project_name = projects[choice - 1]
                    tasks_str = self.special_project.view_tasks_in_project(project_name)
                    print(f"\n===== Tasks in Special Project '{project_name}' =====")
                    print(tasks_str)
                    return
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def view_completion_rate(self):
        """
        Retrieves and displays the completion rate of a special project

        Returns: None

        Args: None
        """
        while True:
            try:
                completion_rate_str = self.special_project.view_completion_rate()
                print("\n===== Completion Rate =====")
                print(completion_rate_str)
                self.completion_rates.append(float(completion_rate_str.split()[2][:-1]))
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter valid input types.")

        self.plot_completion_rate_graph()

    def plot_completion_rate_graph(self):
        """
        Plots completion rate as a function of time

        Returns: None

        Args: None
        """
        plt.plot(self.completion_rates)
        plt.xlabel('Time (Days)')
        plt.ylabel('Completion Rate (%)')
        plt.title('Completion Rate Over Time')
        plt.show()