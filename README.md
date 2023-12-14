Requirements to run code and Tests:
In order to run the program first you need to download MatPlotLib as graphs are used as a part of the Complex feature requirement for extra credit.
Additionally, Datetime is used in the main file, and for testing, Unittest is used as well as unittest.mock for the test for the interactive program class.

Limitations:
There is an issue with the special projects aspect of the interactive application. When you add a task to a special project and then you go back to the task
menu and edit the category, the category does not update in the special project. Also, when creating a task, you can simply put an empty space as the title,
description, and category. Finally, when you use the view completion percentage method, it will open a graph of the completion percentage. If you want to 
continue to use the program while the graph is open, this is not possible. If you want to continue to use the program after you open the graph, you must close
the graph. After this, the usual screen of choices will appear and you can continue to use the program. 

How to use the program:
First, when you run the program it will prompt you with three choices. First is to go into the task menu where you can create tasks, edit tasks, mark a task complete,
view all tasks, view the completion rate of the tasks, delete tasks, and finally go back to the main menu. The other choice is to go into the special projects menu
where you can add a task to a special project from the tasklist created from the first menu, view tasks in a specific special project, and mark tasks complete in the 
project which will make them complete in the project as well as the tasklist, remove a task from the special project, create a special project, delete a special 
project which will not delete any tasks within, and finally go back to the main menu. The final option of the main menu is to quit.

Here I will go over the intricacies of the task menu. First, when selecting an option from the task menu, if you input an invalid number for an option then it will tell you
that it is invalid and reask for a valid input. If you want to select an option, type the number with no spaces and press enter. The input cannot be the word one. 
When you select the add task portion by typing 1 and pressing enter, it will prompt you with a task title. Any alphanumeric symbols work for the title. 
Two tasks cannot have the same title. Next, it will ask you for the due date in the form of day/month/year in that order with no spaces and a "/" required in between them. 
If it is input incorrectly then it will ask for the due date again. Additionally, the due date cannot be in the past. If you input a past due date then it will ask for 
the due date again and give an error statement. Then it will ask for a task description. This acts under the same constraints as the title, except two tasks can have the 
same description. Then it will prompt for a category. This is the same as the description, where two tasks can have the same category. After this, the program will tell you
that the task has been successfully added. Next, you can edit tasks by entering 2. It will first prompt you for the task title. You need to enter the task title with correct
spelling, spacing, and capitalization for it to work otherwise it will say the task does not exist. If you enter the title correctly, then the program will prompt whether you
want to change the title or not. You respond by typing lowercase n (no) or y (yes) with no spaces. If you say yes then the title constraints are the same as before, and
no two tasks can have the same title. Then it will prompt 3 aspects to edit, with another fourth option to edit them all. You select the different aspects by typing their
corresponding number and separating them by commas. Spaces do not cause errors as long as they are separated correctly by commas. If you input an incorrect value then it will
ask again for the aspects to edit. The new aspects have the same constraints as when creating the task. Next, in the main menu, you can mark a task complete by typing 3. Then,
it will ask you for the task title to be marked. This input is the same as before, where spacing, capitalization, and spelling matter. If the task does not exist then
it will throw an error and open the task menu again. If the input is valid, it will say that the task has been marked complete and open the menu again. You can view all tasks by 
typing 4 and pressing enter. This will show all tasks, organized by their category. It will show their title, due date, description, category, and completion status. Next, from
the main menu, you can view the completion rate of the tasks. If you try to view to completion rate with no tasks it will throw an error and tell you that there are no tasks. If
a task does exist, then it will calculate the overall completion rate of all tasks and display it in text form as well as graphical form. The graph x-axis is the number of iterations,
basically meaning how many times you open the completion rate graph. So every time you open the completion rate it will show you the completion rates of the last times you opened
it along with the completion percentage of the current tasks. The y-axis is the completion percentage of the tasks. As described in the limitation portion, you cannot continue
with the program while the graph is still open. You need to close it to continue with the menu. Next from the menu, you can delete a task. The input of the task title is the 
same as before, where spacing and capitalization matter.

Special Projects Menu:
When you select the special options menu, it is used mainly for organizing tasks into projects, so you should already have one or two tasks made at this point to utilize them.
First, you should create a special project by entering 5. This will ask for a title, which works the exact same way as the title for a task. If you put a title already used
it will tell you and ask for a valid title. If the title is valid, then it will create a special project. Next, you can add a task to a special project by typing 1 and pressing enter.
Keep in mind that the inputs work the same as the task menu. Once you select 1, it will prompt for a task title that you want to add to a special project. If either input is invalid or the task or project doesn't exist then it will throw an error and reopen the menu. Once the input is valid for both, it will add the task to the project. Then, you can view the tasks in the special projects by selecting the corresponding number. This will open a screen with all of the special projects, numbered. Then by typing the corresponding number of the special project you want to select, it will display all of the tasks within the project, with their title, due date, due date, description, category, and completion status. If there are no tasks in the project, then it will say that there are no tasks in the project and open the menu again. Next, you can mark a task complete in the special project. This is done just like adding a task to a project, where the task title to be marked complete needs to be input, and then the corresponding project title. If the input is not valid, then it will say whether the task does not exist in the project of the project does not exist. If the input is valid, then it will mark the task complete in both the special project menu and the task menu, which can be viewed by viewing all tasks in the tasklist or special project. Then, a task can be removed from the special project, once again done by entering the name of the title of the task followed by the special project name. If the input is invalid then it will say why it is invalid just like when marking a task complete. If the input is valid then it will remove the task from the project, but it won't delete it completely. The task still exists on the tasklist, it just won't exist in the project anymore. Finally, you can delete a special project by entering in the number 6 and pressing enter. It will ask for the title of the project to be deleted. If the input is invalid then it will throw an error and open the menu again. If the title is valid then it will delete the project from the project list. Note, if a project is deleted with tasks in it, the tasks still exist on the task list, only the project is deleted. Final Note, if you close the program at any time, it will delete all previous tasks and special projects so be careful.


Thank you for the great semester!!! I learned alot.
