import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        impMenu = QMenu('open', self)
        impAct = QAction('open file', self)
        impAct2 = QMenu('exit', self)
        impMenu.addAction(impAct)
        
        newAct = QAction('New', self)        
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addMenu(impAct2)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
