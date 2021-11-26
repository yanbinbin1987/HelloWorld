import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

import HelloWorld

def convert(ui):
    input = ui.lineEdit_2.text()
    result = float( input ) * 6.7
    ui.lineEdit.setText( str( result ) )

#    print( 'We finally get married!' )
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = HelloWorld.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect( partial( convert, ui ) )
#    ui.pushButton.clicked.connect( convert )
    sys.exit(app.exec_())