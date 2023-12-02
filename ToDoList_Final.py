class Task:
    def __init__(self, title, due_date, description, category):
        self.title = title
        self.due_date = due_date
        self.description = description
        self.category = category
        self.completed = False
        
    def edit_task(self, new_title, new_due_date, new_description, new_category):
        self.title = new_title
        self.due_date = new_due_date
        self.description = new_description
        self.category = new_category