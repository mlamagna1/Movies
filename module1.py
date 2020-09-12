import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QPushButton, QMainWindow, QGridLayout, QDesktopWidget, QLabel, QLayout
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from Movies import Responses
from pprint import PrettyPrinter
#from Movies import getResponse

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'IMDB Search'
        self.left = 10
        self.top = 10
        self.width = 1280
        self.height = 500
        self.initUI()
        self.flay = QtWidgets.QFormLayout(self)
        self.newSearch = Responses()
        
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #centers window to screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,20)
        

        self.setButton1()
        self.show()

    def getMovieName(self):
        return str(self.textbox.text())

    def setButton1(self):
        button = QPushButton('Search', self)
        button.setToolTip('IMDB Search for Exact Movie Title')
        button.move(160,45)
        
        button.clicked.connect(lambda:self.searchClick())
        button.show()

    def searchClick(self):
        self.newSearch.getMovieAttr(self.getMovieName())
        self.createLabels()

    def createLabels(self):

        pp = PrettyPrinter()
        texts = self.newSearch.getResponse()
        print (texts['Rated'])
        #pp.pprint(texts)
        #for text in texts:
            
        label_1 = QLabel(texts['Rated'])
        label_1.setFixedSize(120, 30)
        label_2 = QLabel(texts['BoxOffice'])
        label_2.setFixedSize(120, 30)
        self.flay.addRow(label_1, label_2)
        #self.flay.addRow(label_1)
        #self.flay.display()
            # An attribute of the class is created with setattr()
            #setattr(self, "{}_infor_label".format(text), label_2)

        # use
        #self.name_infor_label.setText("some name")
        #self.address_infor_label.setText("some address")
        #self.phone_infor_label.setText("some phone")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    ex = App()
    sys.exit(app.exec_())