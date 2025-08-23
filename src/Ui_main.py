# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAppaiQcTq.ui'
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
import img.img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2072, 815)
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
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setStyleSheet(u"background-color:transparent;")
        self.label_8.setPixmap(QPixmap(u":/img/perfil.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"/* ====== Labels ====== */\n"
"QLabel {\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"background-color:transparent;\n"
"}")

        self.verticalLayout.addWidget(self.label_4)

        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setStyleSheet(u"/* ====== Labels ====== */\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"background-color:transparent;\n"
"}")

        self.verticalLayout.addWidget(self.label_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(70)
        self.GestaodeRH = QPushButton(self.page)
        self.GestaodeRH.setObjectName(u"GestaodeRH")
        icon = QIcon()
        icon.addFile(u":/img/Gestao de RH.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.GestaodeRH.setIcon(icon)
        self.GestaodeRH.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.GestaodeRH, 0, 6, 1, 1)

        self.vendas = QPushButton(self.page)
        self.vendas.setObjectName(u"vendas")
        icon1 = QIcon()
        icon1.addFile(u":/img/vendas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vendas.setIcon(icon1)
        self.vendas.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.vendas, 0, 0, 1, 1)

        self.Itens = QPushButton(self.page)
        self.Itens.setObjectName(u"Itens")
        icon2 = QIcon()
        icon2.addFile(u":/img/Itens.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Itens.setIcon(icon2)
        self.Itens.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Itens, 0, 4, 1, 1)

        self.Restaurante = QPushButton(self.page)
        self.Restaurante.setObjectName(u"Restaurante")
        icon3 = QIcon()
        icon3.addFile(u":/img/restaurante.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Restaurante.setIcon(icon3)
        self.Restaurante.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Restaurante, 0, 1, 1, 1)

        self.Logout = QPushButton(self.page)
        self.Logout.setObjectName(u"Logout")
        icon4 = QIcon()
        icon4.addFile(u":/img/Logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Logout.setIcon(icon4)
        self.Logout.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Logout, 2, 6, 1, 1)

        self.Despesas = QPushButton(self.page)
        self.Despesas.setObjectName(u"Despesas")
        self.Despesas.setMinimumSize(QSize(269, 0))
        icon5 = QIcon()
        icon5.addFile(u":/img/Despesas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Despesas.setIcon(icon5)
        self.Despesas.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Despesas, 0, 5, 1, 1)

        self.Hotelaria = QPushButton(self.page)
        self.Hotelaria.setObjectName(u"Hotelaria")
        icon6 = QIcon()
        icon6.addFile(u":/img/Hotelaria.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Hotelaria.setIcon(icon6)
        self.Hotelaria.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Hotelaria, 0, 2, 1, 1)

        self.historico = QPushButton(self.page)
        self.historico.setObjectName(u"historico")
        icon7 = QIcon()
        icon7.addFile(u":/img/Historico.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.historico.setIcon(icon7)
        self.historico.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.historico, 2, 4, 1, 1)

        self.Arquivos = QPushButton(self.page)
        self.Arquivos.setObjectName(u"Arquivos")
        icon8 = QIcon()
        icon8.addFile(u":/img/Arquivos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Arquivos.setIcon(icon8)
        self.Arquivos.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Arquivos, 1, 6, 1, 1)

        self.marketing = QPushButton(self.page)
        self.marketing.setObjectName(u"marketing")
        icon9 = QIcon()
        icon9.addFile(u":/img/marketing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.marketing.setIcon(icon9)
        self.marketing.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.marketing, 1, 0, 1, 1)

        self.BackUp = QPushButton(self.page)
        self.BackUp.setObjectName(u"BackUp")
        icon10 = QIcon()
        icon10.addFile(u":/img/BackUp.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BackUp.setIcon(icon10)
        self.BackUp.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.BackUp, 2, 5, 1, 1)

        self.Configuracoes = QPushButton(self.page)
        self.Configuracoes.setObjectName(u"Configuracoes")
        icon11 = QIcon()
        icon11.addFile(u":/img/Configuracoes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Configuracoes.setIcon(icon11)
        self.Configuracoes.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Configuracoes, 2, 0, 1, 1)

        self.Relatorio = QPushButton(self.page)
        self.Relatorio.setObjectName(u"Relatorio")
        icon12 = QIcon()
        icon12.addFile(u":/img/relatorio.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Relatorio.setIcon(icon12)
        self.Relatorio.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Relatorio, 1, 4, 1, 1)

        self.PainelEstrategico = QPushButton(self.page)
        self.PainelEstrategico.setObjectName(u"PainelEstrategico")
        icon13 = QIcon()
        icon13.addFile(u":/img/painel estrategico.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PainelEstrategico.setIcon(icon13)
        self.PainelEstrategico.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.PainelEstrategico, 1, 5, 1, 1)

        self.Restaurante_3 = QPushButton(self.page)
        self.Restaurante_3.setObjectName(u"Restaurante_3")
        icon14 = QIcon()
        icon14.addFile(u"../img/Portagem.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Restaurante_3.setIcon(icon14)
        self.Restaurante_3.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.Restaurante_3, 0, 3, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page)
        self.Vendas = QWidget()
        self.Vendas.setObjectName(u"Vendas")
        self.verticalLayout_6 = QVBoxLayout(self.Vendas)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.Vendas)
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
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pesquisar_clientes = QLineEdit(self.page_3)
        self.pesquisar_clientes.setObjectName(u"pesquisar_clientes")

        self.verticalLayout_9.addWidget(self.pesquisar_clientes)

        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(80, 70, 865, 40))

        self.verticalLayout_9.addWidget(self.frame_2)

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
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
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

        self.stackedWidget.addWidget(self.Vendas)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CREART SOFTMANAGEMENT", None))
        self.label_8.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"12:00", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" 01/01/2025", None))
#if QT_CONFIG(tooltip)
        self.GestaodeRH.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de compras", None))
#endif // QT_CONFIG(tooltip)
        self.GestaodeRH.setText(QCoreApplication.translate("MainWindow", u"Gest\u00e3o de R. H.", None))
#if QT_CONFIG(tooltip)
        self.vendas.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de vendas", None))
#endif // QT_CONFIG(tooltip)
        self.vendas.setText(QCoreApplication.translate("MainWindow", u" Vendas/Loja", None))
#if QT_CONFIG(tooltip)
        self.Itens.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de itens", None))
#endif // QT_CONFIG(tooltip)
        self.Itens.setText(QCoreApplication.translate("MainWindow", u"Itens/Estoque", None))
#if QT_CONFIG(tooltip)
        self.Restaurante.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de vendas", None))
#endif // QT_CONFIG(tooltip)
        self.Restaurante.setText(QCoreApplication.translate("MainWindow", u"Restaurante", None))
#if QT_CONFIG(tooltip)
        self.Logout.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para fazer logout", None))
#endif // QT_CONFIG(tooltip)
        self.Logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
#if QT_CONFIG(tooltip)
        self.Despesas.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de compras", None))
#endif // QT_CONFIG(tooltip)
        self.Despesas.setText(QCoreApplication.translate("MainWindow", u"Despesas", None))
#if QT_CONFIG(tooltip)
        self.Hotelaria.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de vendas", None))
#endif // QT_CONFIG(tooltip)
        self.Hotelaria.setText(QCoreApplication.translate("MainWindow", u"Hotelaria", None))
#if QT_CONFIG(tooltip)
        self.historico.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de Relatorios", None))
#endif // QT_CONFIG(tooltip)
        self.historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
#if QT_CONFIG(tooltip)
        self.Arquivos.setToolTip(QCoreApplication.translate("MainWindow", u"Acesse Documentos", None))
#endif // QT_CONFIG(tooltip)
        self.Arquivos.setText(QCoreApplication.translate("MainWindow", u"Arquivos", None))
#if QT_CONFIG(tooltip)
        self.marketing.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de Marketing", None))
#endif // QT_CONFIG(tooltip)
        self.marketing.setText(QCoreApplication.translate("MainWindow", u"Marketing", None))
#if QT_CONFIG(tooltip)
        self.BackUp.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de Relatorios", None))
#endif // QT_CONFIG(tooltip)
        self.BackUp.setText(QCoreApplication.translate("MainWindow", u"BackUp", None))
#if QT_CONFIG(tooltip)
        self.Configuracoes.setToolTip(QCoreApplication.translate("MainWindow", u"Acesse Configuracoes", None))
#endif // QT_CONFIG(tooltip)
        self.Configuracoes.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
#if QT_CONFIG(tooltip)
        self.Relatorio.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de Relatorios", None))
#endif // QT_CONFIG(tooltip)
        self.Relatorio.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
#if QT_CONFIG(tooltip)
        self.PainelEstrategico.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de delivery", None))
#endif // QT_CONFIG(tooltip)
        self.PainelEstrategico.setText(QCoreApplication.translate("MainWindow", u"Painel Estrat\u00e9gico", None))
#if QT_CONFIG(tooltip)
        self.Restaurante_3.setToolTip(QCoreApplication.translate("MainWindow", u"Clique para entrar no painel de vendas", None))
#endif // QT_CONFIG(tooltip)
        self.Restaurante_3.setText(QCoreApplication.translate("MainWindow", u"Portagem", None))
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
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Custo S/IVA", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"IVA (16%)", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SubTotal", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_6.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Pagar", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"2\u00aa Via", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

