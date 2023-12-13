Requirements to run code and Tests:
In order to run the program first you need to download MatPlotLib as graphs are used as a part of the Complex feature requirement for extra credit.
Additionally, Datetime is used in the main file, and for testing, Unittest is used as well as unittest.mock for the test for the interactive program class.

Limitations:
There is an issue with the special projects aspect of the interactive application. When you add a task to a special project and then you go back to the task
menu and edit the category, the category does not update in the special project. Also, when creating a task, you can simply put an empty space as the title,
description, and category. Finally, when you use the view completion percentage method, it will open a graph of the completion percentage. If you want to 
continue to use the program while the graph is open, this is not possible. If you want to continue to use the program after you open the graph, you must close
the graph. After this, the usual screen of choices will appear and you can continue to use the program. 

How to use program:
First, when you run the program it will prompt you with three choices. First is to go into the task menu where you can create tasks, edit tasks, mark a task complete,
view all tasks, view the completion rate of the tasks, delete tasks, and finally go back to the main menu. The other choice is to go into the special projects menu
where you can add a task to a special project from the tasklist created from the first menu, view tasks in a specific special project, mark tasks complete in the 
project which will mak them complete in the project as well as the tasklist, remove a task from the special project, create a special project, delete a special 
project which will not delete any tasks within, and finally go back to the main menu. The final option of the main menu is to quit.

Here I will go over the intricasies of the task menu. First, when selecting an option from the task menu, if you input an invalid number for an optionthen it will tell you
that it is invalid and reask for a valid input. If you want to select and option, type the number with no spaces and press enter. The input cannot be the word one. 
When you select the add task portion by typing 1 and pressing enter, it will prompt you with a task title. Any alphanumeric symbols work for the title. 
Two tasks cannot have the same title. Next it will ask you for the due date in the form of day/month/year in that order with no spaces and a "/" required in between them. 
If it is input incorrectly then it will ask for the due date again. Additionally, the due date cannot be in the past. If you input a past due date then it will ask for 
the due date again and give and error statement. Then it will ask for a task description. This acts under the same constraints as the title, except two tasks can have the 
same description. Then it will prompt for a category. This is the same as the description, where two tasks can have the same category. After this the program will tell you
that the task has been succesfully added. Next, you can edit tasks by entering 2. It will first prompt you for the task title. You need to enter the task title with correct
spelling, spacing, and capitalization for it to work otherwise it will say the task does not exist. If you enter the title correctly, then the program will prompt whether you
want to change the title or not. You respond by typing lowercase n (no) or y (yes) with no spaces. If you say yes then the title constraints are the same as before, and
no two tasks can have the same title. Then it will prompt 3 aspects to edit, with another fourth option to edit them all. You select the different aspects by typing their
corresponding number and seperating them by commas. Spaces do not cuase errors as long as they are seperated correctly by commas. If you input an incorrect value then it will
ask again for the aspects to edit. The new aspects have the same constaints as when creating the task. Next, in the main menu, you can mark a task complete by typing 3. Then,
it will ask you for the title of the task to be marked. This input is the same as before, where spacing, capitalization, and spelling matter. If the task does not exist then
it will throw an error and open the task menu again. If the input is valid, it will say that the task has been marked complete and open the menu again. You can view all tasks by 
typing 4 and pressing enter. This will show all tasks, organized by their category. It will show their title, due date, description, category, and completion status. 
