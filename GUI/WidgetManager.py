from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class WidgetManager():
    def __init__(self, parent: QWidget or QLabel or QMainWindow = None):
        super().__init__()
        self.widgets = []
        self.parent = parent


    def addWidget(self, widget: QWidget or QLabel):
        self.widgets.append(widget)
        widget.setParent(self.parent)


    def setParent(self, parent: QWidget or QLabel or QMainWindow):
        for item in self.widgets:
            item.setParent(parent)
            self.parent = parent

    def showWidget(self, widget: QWidget or QLabel):
        if self.parent.isVisible() == False:
            self.parent.show()

        for item in self.widgets:
            if item == widget:
                widget.setParent(self.parent)
                widget.show()
            else:
                item.hide()