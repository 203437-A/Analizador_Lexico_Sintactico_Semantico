from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from analizador_lexico import analisis

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()

        loadUi('vista.ui', self)

        self.pushButton.clicked.connect(self.verificar)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Token", "Valor", "Posición"])

        self.tableWidget.setColumnWidth(0, 200)  
        self.tableWidget.setColumnWidth(1, 200)  
        self.tableWidget.setColumnWidth(2, 200)  

    def verificar(self):
        texto = self.textEdit.toPlainText()

        resultados = analisis(texto)

        self.tableWidget.setRowCount(0)

        for resultado in resultados:
            tipo, valor, posicion = resultado.split(maxsplit=2)

            rowPosition = self.tableWidget.rowCount()

            self.tableWidget.insertRow(rowPosition)

            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(tipo))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(valor))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(posicion))

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()
