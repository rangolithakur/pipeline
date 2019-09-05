import os as _os
import functools as _functools

from PySide2 import QtWidgets, QtCore
from PyQt5 import uic, QtGui

from app import constants as cnt
from app import jsondata as jsn

class MainWindow(QtWidgets.QDialog):
    """Asset Gather Dialog """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedHeight(200)
        
        entityTypeW = ListWidget(widType=cnt.ENTITYTYPE)
        tasksW = ListWidget(widType=cnt.TASKS)
        entityNameW = ListWidget(widType=cnt.ENTITYNAME)
        projNameW = ListWidget(widType=cnt.PROJNAME)
        taskAsigneeW = ListWidget(widType=cnt.TASKASIGNEE)
        #self.listWidget.installEventFilter(self)
        
        self.setWindowTitle("Asset Gather Tool")
        vlayout = QtWidgets.QVBoxLayout(self)
        hboxW = QtWidgets.QHBoxLayout(self)
        hboxT = QtWidgets.QHBoxLayout(self)
    
        hboxT.addWidget(entityTypeW.lbl)
        hboxT.addWidget(tasksW.lbl)
        hboxT.addWidget(entityNameW.lbl)
        hboxT.addWidget(projNameW.lbl)
        hboxT.addWidget(taskAsigneeW.lbl)
        
        hboxW.addWidget(entityTypeW)    
        hboxW.addWidget(tasksW)
        hboxW.addWidget(entityNameW)
        hboxW.addWidget(projNameW)
        hboxW.addWidget(taskAsigneeW)

        vlayout.addLayout(hboxT)
        vlayout.addLayout(hboxW)
        self.setLayout(vlayout)
        #entityTypeW.itemClicked.connect(entityTypeW._onentityClicked)
        #tasksW.itemClicked.connect(tasksW._ontaskClicked)
        #entityNameW.itemClicked.connect(entityNameW._onentNameClicked)
        #projNameW.itemClicked.connect(projNameW._onprojClicked)
        
        
class ListWidget(QtWidgets.QListWidget):
    def __init__(self, widType=None):
        super(ListWidget, self).__init__()
        self.lbl = QtWidgets.QLabel()
        self.lbl.setText(widType)
        self.lbl.setAlignment(QtCore.Qt.AlignTop)
        
        #layout = QtWidgets.QVBoxLayout(self)
        #layout.addWidget(lbl)
        print('widType',widType)
        self.selection = None
        #self.listWidget = QtWidgets.QListWidget()
        self.setFixedSize(171, 151)
        self.addItems('One Two Three'.split()) #To be replaced with fetched data
        self.itemClicked.connect(_functools.partial(self._onitemClick,widType))
        
        #call data layer to fetch the data and display
        #call context manager to display data on selection

    def _onitemClick(self, widType, item):
        """
        helper method , Called when item
        is selected from list
        args : selected item(QListWidgetItem)
        return : None
        """
        print('onitemClick',widType)
        print(item,type(item), str(item.text()))
        self.selection = str(item.text())
        #Emit context signal to display related data

##    def _ontaskClicked(self, item):
##        """
##        helper method , Called when any task
##        is selected from the task list
##        args : selected item(QListWidgetItem)
##        return : None
##        """
##        print('ontaskcliced')
##        print(item,type(item), str(item.text()))
##        self.selection = str(item.text())
##        #Emit context signal to display related data
##
##    def _onentNameClicked(self, item):
##        """
##        helper method , Called when entity name
##        is selected from the list
##        args : selected item(QListWidgetItem)
##        return : None
##        """
##        print('onentNameClicked')
##        print(item,type(item), str(item.text()))
##        self.selection = str(item.text())
##        #Emit context signal to display related data
##
##    def _onprojClicked(self, item):
##        """
##        helper method , Called when project
##        is selected from the task list
##        args : selected item(QListWidgetItem)
##        return : None
##        """
##        print('onprojClicked')
##        print(item,type(item), str(item.text()))
##        self.selection = str(item.text())
##        #Emit context signal to display related data
##
##   
