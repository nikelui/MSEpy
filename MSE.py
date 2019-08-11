import sys
from PyQt5 import QtWidgets
from startWin import Ui_startWindow

class appWin(QtWidgets.QMainWindow):
    """This is the starting window. You can either create a new set or load an existing one by using the buttons."""
    def __init__(self):
        super(appWin,self).__init__()
        
        self.ui = Ui_startWindow() # Load the converted .ui made in Qt designer
        self.ui.setupUi(self)

    ## Define slots here
    def openFile(self): # Open set button slot
        fname, _filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Select set file', 
            '.',"set files (*.mse-set *.mse *.set);;all files (*.*)")
        print(fname) # Debug
    # TODO: look at the set file and write a function to load it
    # TODO: optionally, convert mse-set in .json format (more compatible?)
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = appWin()
    window.show()
    sys.exit(app.exec_())
