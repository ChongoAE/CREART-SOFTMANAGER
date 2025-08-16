# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1347, 678)
        MainWindow.setStyleSheet(u"\n"
"/* ====== Fundo geral ====== */\n"
"QWidget {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f1c2e, stop:1 #182c47\n"
"    );\n"
"    color: #FFFFFF;\n"
"    font-family: 'Segoe UI', Roboto, sans-serif;\n"
"}\n"
"\n"
"/* ====== Labels ====== */\n"
"QLabel {\n"
"    font-size: 20pt;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* ====== Bot\u00f5es principais (QPushButton) ====== */\n"
"QPushButton {\n"
"    background-color: #1e3a5f;\n"
"    border-radius: 12px;\n"
"    padding: 14px;\n"
"    font-size: 15pt;\n"
"    font-weight: 500;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #284c75;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #162a44;\n"
"}\n"
"\n"
"/* ====== Bot\u00f5es de navega\u00e7\u00e3o (QToolButton) ====== */\n"
"QToolButton {\n"
"    background-color: #1e3a5f;\n"
"    border-radius: 12px;\n"
"    padding: 10px;\n"
"    font-size: 13pt;\n"
""
                        "    color: #FFFFFF;\n"
"    text-align: left;\n"
"    border: none;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: #284c75;\n"
"}\n"
"QToolButton:checked {\n"
"    background-color: #3b82f6;\n"
"    color: white;\n"
"}\n"
"QToolButton:checked:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"/* ====== Campos de texto ====== */\n"
"QLineEdit {\n"
"    background-color: #1e293b;\n"
"    border: 2px solid #334155;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 13pt;\n"
"    color: white;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3b82f6;\n"
"}\n"
"\n"
"/* ====== Barra de rolagem ====== */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #64748b;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #94a3b8;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(70)
        self.vendas = QPushButton(self.page)
        self.vendas.setObjectName(u"vendas")

        self.gridLayout.addWidget(self.vendas, 0, 0, 1, 1)

        self.compras = QPushButton(self.page)
        self.compras.setObjectName(u"compras")

        self.gridLayout.addWidget(self.compras, 0, 1, 1, 1)

        self.Relatorio = QPushButton(self.page)
        self.Relatorio.setObjectName(u"Relatorio")

        self.gridLayout.addWidget(self.Relatorio, 0, 2, 1, 1)

        self.Itens = QPushButton(self.page)
        self.Itens.setObjectName(u"Itens")

        self.gridLayout.addWidget(self.Itens, 0, 3, 1, 1)

        self.mesas = QPushButton(self.page)
        self.mesas.setObjectName(u"mesas")

        self.gridLayout.addWidget(self.mesas, 0, 4, 1, 1)

        self.marketing = QPushButton(self.page)
        self.marketing.setObjectName(u"marketing")

        self.gridLayout.addWidget(self.marketing, 1, 0, 1, 1)

        self.Documentos = QPushButton(self.page)
        self.Documentos.setObjectName(u"Documentos")

        self.gridLayout.addWidget(self.Documentos, 1, 1, 1, 1)

        self.delivery = QPushButton(self.page)
        self.delivery.setObjectName(u"delivery")

        self.gridLayout.addWidget(self.delivery, 1, 2, 1, 1)

        self.Documentos_2 = QPushButton(self.page)
        self.Documentos_2.setObjectName(u"Documentos_2")

        self.gridLayout.addWidget(self.Documentos_2, 1, 3, 1, 1)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.page_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_5.addWidget(self.label_2)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pdv = QToolButton(self.frame)
        self.pdv.setObjectName(u"pdv")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pdv.sizePolicy().hasHeightForWidth())
        self.pdv.setSizePolicy(sizePolicy1)
        self.pdv.setMinimumSize(QSize(100, 35))
        self.pdv.setCheckable(True)
        self.pdv.setChecked(True)
        self.pdv.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pdv)

        self.clientes = QToolButton(self.frame)
        self.clientes.setObjectName(u"clientes")
        sizePolicy1.setHeightForWidth(self.clientes.sizePolicy().hasHeightForWidth())
        self.clientes.setSizePolicy(sizePolicy1)
        self.clientes.setMinimumSize(QSize(100, 35))
        self.clientes.setCheckable(True)
        self.clientes.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.clientes)

        self.estimativas = QToolButton(self.frame)
        self.estimativas.setObjectName(u"estimativas")
        sizePolicy1.setHeightForWidth(self.estimativas.sizePolicy().hasHeightForWidth())
        self.estimativas.setSizePolicy(sizePolicy1)
        self.estimativas.setMinimumSize(QSize(100, 35))
        self.estimativas.setCheckable(True)
        self.estimativas.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.estimativas)

        self.facturas = QToolButton(self.frame)
        self.facturas.setObjectName(u"facturas")
        sizePolicy1.setHeightForWidth(self.facturas.sizePolicy().hasHeightForWidth())
        self.facturas.setSizePolicy(sizePolicy1)
        self.facturas.setMinimumSize(QSize(100, 35))
        self.facturas.setCheckable(True)
        self.facturas.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.facturas)

        self.recibos = QToolButton(self.frame)
        self.recibos.setObjectName(u"recibos")
        sizePolicy1.setHeightForWidth(self.recibos.sizePolicy().hasHeightForWidth())
        self.recibos.setSizePolicy(sizePolicy1)
        self.recibos.setMinimumSize(QSize(100, 35))
        self.recibos.setCheckable(True)
        self.recibos.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.recibos)

        self.pagamentos = QToolButton(self.frame)
        self.pagamentos.setObjectName(u"pagamentos")
        sizePolicy1.setHeightForWidth(self.pagamentos.sizePolicy().hasHeightForWidth())
        self.pagamentos.setSizePolicy(sizePolicy1)
        self.pagamentos.setMinimumSize(QSize(100, 35))
        self.pagamentos.setCheckable(True)
        self.pagamentos.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pagamentos)

        self.notas = QToolButton(self.frame)
        self.notas.setObjectName(u"notas")
        sizePolicy1.setHeightForWidth(self.notas.sizePolicy().hasHeightForWidth())
        self.notas.setSizePolicy(sizePolicy1)
        self.notas.setMinimumSize(QSize(100, 35))
        self.notas.setCheckable(True)
        self.notas.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.notas)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.frame)

        self.splitter.addWidget(self.layoutWidget)
        self.stackedWidget_2 = QStackedWidget(self.splitter)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_8 = QVBoxLayout(self.page_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.frame_3 = QFrame(self.page_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignRight)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton = QToolButton(self.page_4)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy2)
        self.toolButton.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.page_4)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy1.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy1)
        self.toolButton_2.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.page_4)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy1.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy1)
        self.toolButton_3.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.toolButton_3)

        self.toolButton_4 = QToolButton(self.page_4)
        self.toolButton_4.setObjectName(u"toolButton_4")
        sizePolicy1.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy1)
        self.toolButton_4.setMinimumSize(QSize(0, 35))
        self.toolButton_4.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.toolButton_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.stackedWidget_2.addWidget(self.page_4)
        self.splitter.addWidget(self.stackedWidget_2)

        self.verticalLayout_6.addWidget(self.splitter)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CREART SoftManager", None))
#if QT_CONFIG(tooltip)
        self.vendas.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de vendas", None))
#endif // QT_CONFIG(tooltip)
        self.vendas.setText(QCoreApplication.translate("MainWindow", u"Vendas", None))
#if QT_CONFIG(tooltip)
        self.compras.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de compras", None))
#endif // QT_CONFIG(tooltip)
        self.compras.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
#if QT_CONFIG(tooltip)
        self.Relatorio.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de Relatorios", None))
#endif // QT_CONFIG(tooltip)
        self.Relatorio.setText(QCoreApplication.translate("MainWindow", u"Relatorio", None))
#if QT_CONFIG(tooltip)
        self.Itens.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de itens", None))
#endif // QT_CONFIG(tooltip)
        self.Itens.setText(QCoreApplication.translate("MainWindow", u"Itens", None))
#if QT_CONFIG(tooltip)
        self.mesas.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de Mesas", None))
#endif // QT_CONFIG(tooltip)
        self.mesas.setText(QCoreApplication.translate("MainWindow", u"Mesas", None))
#if QT_CONFIG(tooltip)
        self.marketing.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de Marketing", None))
#endif // QT_CONFIG(tooltip)
        self.marketing.setText(QCoreApplication.translate("MainWindow", u"Marketing", None))
#if QT_CONFIG(tooltip)
        self.Documentos.setToolTip(QCoreApplication.translate("MainWindow", u"Acesse Documentos", None))
#endif // QT_CONFIG(tooltip)
        self.Documentos.setText(QCoreApplication.translate("MainWindow", u"Documentos", None))
#if QT_CONFIG(tooltip)
        self.delivery.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de delivery", None))
#endif // QT_CONFIG(tooltip)
        self.delivery.setText(QCoreApplication.translate("MainWindow", u"Delivery", None))
#if QT_CONFIG(tooltip)
        self.Documentos_2.setToolTip(QCoreApplication.translate("MainWindow", u"Acesse Configuracoes", None))
#endif // QT_CONFIG(tooltip)
        self.Documentos_2.setText(QCoreApplication.translate("MainWindow", u"Configuracoes", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para fazer logout", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.pdv.setText(QCoreApplication.translate("MainWindow", u"PDV", None))
        self.clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.estimativas.setText(QCoreApplication.translate("MainWindow", u"Estimativas", None))
        self.facturas.setText(QCoreApplication.translate("MainWindow", u"Facturas", None))
        self.recibos.setText(QCoreApplication.translate("MainWindow", u"Recibos", None))
        self.pagamentos.setText(QCoreApplication.translate("MainWindow", u"Pagamentos", None))
        self.notas.setText(QCoreApplication.translate("MainWindow", u"Notas de Credito", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar Item", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adicionar Cliente", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Custo", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SubTotal", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_6.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Pagar", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u" 2 Via", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

