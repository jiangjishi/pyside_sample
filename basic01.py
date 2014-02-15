import os
import maya.cmds as cmds

from loaduitype import LoadUiType


_path_current_dir = os.path.dirname(__file__)
_path_ui_file = os.path.join(_path_current_dir, "basic01.ui")

# load ui file (generate window super classes)
_loaduitype = LoadUiType()
form_class, base_class = _loaduitype.build(_path_ui_file)

# window class
class MyWindow(form_class, base_class):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self._print_input_text)
        
    def _print_input_text(self):
        print self.lineEdit.text()


def show_window(): 
    global my_window

    try:           
        my_window.close()
        my_window.deleteLater()
    except:
        pass

    my_window = MyWindow()
    my_window.show()
