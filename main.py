import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from src.Ui_main import Ui_MainWindow

class Janela_Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       

        self.ui.vendas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pdv.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.clientes.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.estimativas.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.facturas.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(3))
        self.ui.recibos.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(4))
        self.ui.pagamentos.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(5))
        self.ui.notas.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(6))

        self.ui.marketing.setDisabled(True)
        self.ui.delivery.setDisabled(True)
        self.ui.Documentos.setDisabled(True)


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela_Principal()
    janela.show()
    sys.exit(app.exec())

