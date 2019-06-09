# Introduction
Welcome to Pipeline Developer test repository.

# What's included
## Data files
The data files are included under `data` directory. 
* tasks.json - A list of tasks that are assigned to artists.
* entities.json - List of entities that the above tasks belong to.

> Tasks belong to either a Shot or an Asset entity. You will be able to find entities of type `Shot` or `Asset` inside entities.json

## PySide App boilerplate
The application boilerplate consists of:
* main.py(file) - Entry point for the app
* app(directory) - Python package that consists of a QMainWindow module

# Tasks

![Alt text](resources/PipeTest-Tasks.jpg?raw=true "Tasks Hierarchy")

The following are the tasks that need to be accomplished in order to successfully complete this test. The tasks are listed in ascending order of priority.

1. Design a wireframe to show an end user (Artist in our case) his Tasks and the information about it

2. Map the relation from Task to its Entity by reading the included data files.

3. Implement a QListView widget that can display the tasks. Up on selection, a side pane should display the entity information of the task.
Should be using MVC to implement the ListView. 

4. Implement a class generator using metaclasses that can create a Shot/Asset class and Task class for the Task schema and Asset/Shot schema. 

5. After implementing the class generator, refactor the model class for the widget to use the class generator for creating model items.

6. Write unit tests for the class generator

7. Generate Sphinx documentation of the code base

8. Write up an user documentation for the application and its behaviour 


# Setting up your developer environment
## Project requirements
* Python 3.7x
* pipenv

Once you have installed Python 3.7x and pipenv, the required dependencies can be installed by running 
`pipenv update`

## Launching the app
You should be able to see an empty window up on running the following from the repository root.
* `pipenv shell`
* `python main.py`

> Don't hesitate to get in touch with us at pipe-recruit@taufilms.com if you are not able to get the boilerplate code working.


# Coding Guidelines
DOs
* Create a new git branch for each of the tasks listed above. eg: `task1`, `task2`
* Feel free to add additional modules to better organise the code.
* Any additional modules SHOULD be added under the `app` package.
* Include .ui(Qt Designer files) even if you are using pyside2uic to generate python source for the app.
* Commit often. We understand its difficult to have uninterrupted time to complete all the tasks. Pushing daily progress helps us understand your thought process better.

DONTs
* Do not work directly on the `master` branch. Use branches as mentioned above.
* Do not change the structure of the repository. i.e. Do no move around existing files in the repository.

# Submission Guidelines
Raise a Pull Request to `master` from each of the task branches.

Drop an email to pipe-recruit@taufilms.com once your PR is ready for review.

Wishing you all the very best!
