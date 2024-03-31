from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from analizador_lexico import analisis
from analizador_sintactico import prueba

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()

        loadUi('vista.ui', self)

        self.pushButton.clicked.connect(self.verificar)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Token", "Lexema", "Posición"])

        self.tableWidget.setColumnWidth(0, 200)  
        self.tableWidget.setColumnWidth(1, 200)  
        self.tableWidget.setColumnWidth(2, 200)  

    def verificar(self):
        texto = self.textEdit.toPlainText()
        success_lexical, resultados_lexico = analisis(texto)
        self.tableWidget.setRowCount(0)

        for resultado in resultados_lexico:
            token, lexema, posicion = resultado.split(maxsplit=2)

            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(token))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(lexema))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(posicion))

        resultado_sintactico = prueba(texto)

        self.textBrowser.clear()
        if success_lexical and 'TOKEN_INVALIDO' not in ''.join(resultados_lexico):
            if resultado_sintactico is not None:
                self.textBrowser.append(f"El análisis sintáctico tuvo éxito y válido:\n{resultado_sintactico}")
            else:
                self.textBrowser.append("El análisis sintáctico no tuvo éxito.")
        else:
            self.textBrowser.append("El análisis léxico encontró TOKEN_INVALIDO.\nNo se mostrarán resultados sintácticos.")

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()

