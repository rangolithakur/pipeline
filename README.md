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

The following are the tasks that need to be accomplished 

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

