from PyQt5 import QtCore, QtGui, QtWidgets


class Estoque(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 859)
        MainWindow.setStyleSheet("*{\n"
"    margin:0px;\n"
"    border: 0px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    margin:0px;\n"
"    border: 0px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_animado = QtWidgets.QFrame(self.centralwidget)
        self.menu_animado.setMinimumSize(QtCore.QSize(0, 0))
        self.menu_animado.setMaximumSize(QtCore.QSize(0, 16777215))
        self.menu_animado.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(37, 77, 122);\n"
"    border-radius: 15px;\n"
"}")
        self.menu_animado.setObjectName("menu_animado")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_animado)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(16, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_estoque = QtWidgets.QPushButton(self.menu_animado)
        self.btn_estoque.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_estoque.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_estoque.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_estoque.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(37, 77, 122);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgba(35, 85, 141, 0.86);\n"
"    border-radius: 16px;\n"
"    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"    backdrop-filter: blur(5px);\n"
"    -webkit-backdrop-filter: blur(5px);\n"
"    border: 1px solid rgba(62, 110, 164, 0.4);\n"
"}")
        self.btn_estoque.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Nova pasta/Produtos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_estoque.setIcon(icon)
        self.btn_estoque.setIconSize(QtCore.QSize(58, 65))
        self.btn_estoque.setFlat(True)
        self.btn_estoque.setObjectName("btn_estoque")
        self.verticalLayout_2.addWidget(self.btn_estoque)
        self.bnt_add_cliente = QtWidgets.QPushButton(self.menu_animado)
        self.bnt_add_cliente.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bnt_add_cliente.sizePolicy().hasHeightForWidth())
        self.bnt_add_cliente.setSizePolicy(sizePolicy)
        self.bnt_add_cliente.setMinimumSize(QtCore.QSize(0, 50))
        self.bnt_add_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bnt_add_cliente.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(37, 77, 122);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgba(35, 85, 141, 0.86);\n"
"    border-radius: 16px;\n"
"    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"    backdrop-filter: blur(5px);\n"
"    -webkit-backdrop-filter: blur(5px);\n"
"    border: 1px solid rgba(62, 110, 164, 0.4);\n"
"}")
        self.bnt_add_cliente.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Nova pasta/add_users.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bnt_add_cliente.setIcon(icon1)
        self.bnt_add_cliente.setIconSize(QtCore.QSize(70, 46))
        self.bnt_add_cliente.setFlat(True)
        self.bnt_add_cliente.setObjectName("bnt_add_cliente")
        self.verticalLayout_2.addWidget(self.bnt_add_cliente)
        self.btn_pix = QtWidgets.QPushButton(self.menu_animado)
        self.btn_pix.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_pix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pix.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(37, 77, 122);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgba(35, 85, 141, 0.86);\n"
"    border-radius: 16px;\n"
"    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"    backdrop-filter: blur(5px);\n"
"    -webkit-backdrop-filter: blur(5px);\n"
"    border: 1px solid rgba(62, 110, 164, 0.4);\n"
"}")
        self.btn_pix.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/Nova pasta/logo-pix-png-954x339.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pix.setIcon(icon2)
        self.btn_pix.setIconSize(QtCore.QSize(97, 43))
        self.btn_pix.setFlat(True)
        self.btn_pix.setObjectName("btn_pix")
        self.verticalLayout_2.addWidget(self.btn_pix)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.engrenagem = QtWidgets.QPushButton(self.menu_animado)
        self.engrenagem.setMinimumSize(QtCore.QSize(0, 50))
        self.engrenagem.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(37, 77, 122);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgba(35, 85, 141, 0.86);\n"
"    border-radius: 16px;\n"
"    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"    backdrop-filter: blur(5px);\n"
"    -webkit-backdrop-filter: blur(5px);\n"
"    border: 1px solid rgba(62, 110, 164, 0.4);\n"
"}")
        self.engrenagem.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/Nova pasta/engrenagem_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.engrenagem.setIcon(icon3)
        self.engrenagem.setIconSize(QtCore.QSize(80, 44))
        self.engrenagem.setFlat(True)
        self.engrenagem.setObjectName("engrenagem")
        self.verticalLayout_2.addWidget(self.engrenagem)
        self.horizontalLayout.addWidget(self.menu_animado)
        self.conteudo = QtWidgets.QWidget(self.centralwidget)
        self.conteudo.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.conteudo.setObjectName("conteudo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.conteudo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_superior = QtWidgets.QWidget(self.conteudo)
        self.menu_superior.setMinimumSize(QtCore.QSize(0, 77))
        self.menu_superior.setStyleSheet("QWidget{\n"
"    background-color: rgb(37, 77, 122);\n"
"    border-radius: 17px;\n"
"}")
        self.menu_superior.setObjectName("menu_superior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menu_superior)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_menu = QtWidgets.QPushButton(self.menu_superior)
        self.btn_menu.setMaximumSize(QtCore.QSize(60, 80))
        self.btn_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet("background-color:  rgb(37, 77, 122);")
        self.btn_menu.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/Nova pasta/menu_barra.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menu.setIcon(icon4)
        self.btn_menu.setIconSize(QtCore.QSize(50, 55))
        self.btn_menu.setFlat(True)
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_2.addWidget(self.btn_menu)
        self.txt_bem_vindo = QtWidgets.QLineEdit(self.menu_superior)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.txt_bem_vindo.setFont(font)
        self.txt_bem_vindo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txt_bem_vindo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txt_bem_vindo.setStyleSheet("    color: white;\n"
"    background-color: rgb(37, 77, 122);\n"
"    border: none;")
        self.txt_bem_vindo.setObjectName("txt_bem_vindo")
        self.horizontalLayout_2.addWidget(self.txt_bem_vindo)
        self.btn_sair = QtWidgets.QPushButton(self.menu_superior)
        self.btn_sair.setMaximumSize(QtCore.QSize(60, 80))
        self.btn_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sair.setStyleSheet("background-color:  rgb(37, 77, 122);")
        self.btn_sair.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/Nova pasta/sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sair.setIcon(icon5)
        self.btn_sair.setIconSize(QtCore.QSize(79, 59))
        self.btn_sair.setFlat(True)
        self.btn_sair.setObjectName("btn_sair")
        self.horizontalLayout_2.addWidget(self.btn_sair)
        self.verticalLayout.addWidget(self.menu_superior)
        self.stackedWidget = QtWidgets.QStackedWidget(self.conteudo)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 43))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_clientes = QtWidgets.QWidget()
        self.page_clientes.setObjectName("page_clientes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_clientes)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.page_clientes)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setContentsMargins(8, -1, -1, -1)
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txt_cadastrar = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_cadastrar.sizePolicy().hasHeightForWidth())
        self.txt_cadastrar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.txt_cadastrar.setFont(font)
        self.txt_cadastrar.setStyleSheet("QLabel{\n"
"    color: rgb(37, 77, 122) ; \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.txt_cadastrar.setObjectName("txt_cadastrar")
        self.verticalLayout_4.addWidget(self.txt_cadastrar)
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 61))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(0, 10, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.img_lupa_2 = QtWidgets.QLabel(self.widget_7)
        self.img_lupa_2.setMinimumSize(QtCore.QSize(51, 43))
        self.img_lupa_2.setMaximumSize(QtCore.QSize(51, 16777215))
        self.img_lupa_2.setStyleSheet("QLabel{\n"
"    border: 3px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(37, 77, 122)\n"
"}")
        self.img_lupa_2.setText("")
        self.img_lupa_2.setPixmap(QtGui.QPixmap(":/img/Nova pasta/lupa.png"))
        self.img_lupa_2.setScaledContents(True)
        self.img_lupa_2.setWordWrap(False)
        self.img_lupa_2.setIndent(1)
        self.img_lupa_2.setObjectName("img_lupa_2")
        self.horizontalLayout_4.addWidget(self.img_lupa_2)
        self.pesquisar_2 = QtWidgets.QLineEdit(self.widget_7)
        self.pesquisar_2.setMinimumSize(QtCore.QSize(0, 43))
        self.pesquisar_2.setMaximumSize(QtCore.QSize(282, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pesquisar_2.setFont(font)
        self.pesquisar_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"")
        self.pesquisar_2.setObjectName("pesquisar_2")
        self.horizontalLayout_4.addWidget(self.pesquisar_2)
        spacerItem2 = QtWidgets.QSpacerItem(422, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.date_cliente = QtWidgets.QLineEdit(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_cliente.sizePolicy().hasHeightForWidth())
        self.date_cliente.setSizePolicy(sizePolicy)
        self.date_cliente.setMaximumSize(QtCore.QSize(135, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.date_cliente.setFont(font)
        self.date_cliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.date_cliente.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date_cliente.setStyleSheet("color:rgb(37, 77, 122);")
        self.date_cliente.setFrame(True)
        self.date_cliente.setAlignment(QtCore.Qt.AlignCenter)
        self.date_cliente.setObjectName("date_cliente")
        self.horizontalLayout_4.addWidget(self.date_cliente)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.widget_4 = QtWidgets.QWidget(self.widget_6)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.insert_nome = QtWidgets.QLineEdit(self.widget_4)
        self.insert_nome.setMinimumSize(QtCore.QSize(199, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.insert_nome.setFont(font)
        self.insert_nome.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.insert_nome.setObjectName("insert_nome")
        self.horizontalLayout_3.addWidget(self.insert_nome)
        self.insert_carro = QtWidgets.QLineEdit(self.widget_4)
        self.insert_carro.setMinimumSize(QtCore.QSize(199, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.insert_carro.setFont(font)
        self.insert_carro.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.insert_carro.setObjectName("insert_carro")
        self.horizontalLayout_3.addWidget(self.insert_carro)
        self.insert_numero = QtWidgets.QLineEdit(self.widget_4)
        self.insert_numero.setMinimumSize(QtCore.QSize(199, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.insert_numero.setFont(font)
        self.insert_numero.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.insert_numero.setObjectName("insert_numero")
        self.horizontalLayout_3.addWidget(self.insert_numero)
        self.insert_placa = QtWidgets.QLineEdit(self.widget_4)
        self.insert_placa.setMinimumSize(QtCore.QSize(199, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.insert_placa.setFont(font)
        self.insert_placa.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.insert_placa.setObjectName("insert_placa")
        self.horizontalLayout_3.addWidget(self.insert_placa)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_9 = QtWidgets.QWidget(self.widget_6)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.table_cliente = QtWidgets.QTableWidget(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_cliente.setFont(font)
        self.table_cliente.setStyleSheet("QTableWidget {\n"
"    gridline-color: rgb(37, 77, 122);\n"
"    background-color: transparent;\n"
"    outline: 0;\n"
"    border: 1px solid rgb(37, 77, 122);\n"
"    border-top: 0px\n"
"    \n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(87, 135, 189);\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(37, 77, 122);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(37, 77, 122);\n"
"    background-color: transparent;\n"
"    border-left: 0px;\n"
"    color: black;\n"
"\n"
"}\n"
"")
        self.table_cliente.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_cliente.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table_cliente.setShowGrid(True)
        self.table_cliente.setObjectName("table_cliente")
        self.table_cliente.setColumnCount(5)
        self.table_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.table_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.table_cliente.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table_cliente.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table_cliente.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.table_cliente.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.table_cliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.table_cliente.setHorizontalHeaderItem(4, item)
        self.table_cliente.horizontalHeader().setVisible(True)
        self.table_cliente.horizontalHeader().setHighlightSections(False)
        self.table_cliente.horizontalHeader().setSortIndicatorShown(False)
        self.table_cliente.horizontalHeader().setStretchLastSection(False)
        self.table_cliente.verticalHeader().setVisible(False)
        self.table_cliente.verticalHeader().setCascadingSectionResizes(False)
        self.table_cliente.verticalHeader().setHighlightSections(False)
        self.table_cliente.verticalHeader().setMinimumSectionSize(20)
        self.table_cliente.verticalHeader().setSortIndicatorShown(False)
        self.table_cliente.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_8.addWidget(self.table_cliente)
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_cadastrar_cliente = QtWidgets.QPushButton(self.widget_10)
        self.btn_cadastrar_cliente.setMinimumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_cadastrar_cliente.setFont(font)
        self.btn_cadastrar_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cadastrar_cliente.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(37, 77, 122);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid black;\n"
"    font-size: 17px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    font-size: 15px;\n"
"    boder: 3px solid black;\n"
"}")
        self.btn_cadastrar_cliente.setObjectName("btn_cadastrar_cliente")
        self.verticalLayout_8.addWidget(self.btn_cadastrar_cliente)
        spacerItem4 = QtWidgets.QSpacerItem(18, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.btn_alterar_cliente = QtWidgets.QPushButton(self.widget_10)
        self.btn_alterar_cliente.setMinimumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_alterar_cliente.setFont(font)
        self.btn_alterar_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_alterar_cliente.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(37, 77, 122);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid black;\n"
"    font-size: 17px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    font-size: 15px;\n"
"    boder: 3px solid black;\n"
"}")
        self.btn_alterar_cliente.setObjectName("btn_alterar_cliente")
        self.verticalLayout_8.addWidget(self.btn_alterar_cliente)
        spacerItem5 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.btn_registration_4 = QtWidgets.QPushButton(self.widget_10)
        self.btn_registration_4.setMinimumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_registration_4.setFont(font)
        self.btn_registration_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_registration_4.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(37, 77, 122);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid black;\n"
"    font-size: 17px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    font-size: 15px;\n"
"    boder: 3px solid black;\n"
"}")
        self.btn_registration_4.setObjectName("btn_registration_4")
        self.verticalLayout_8.addWidget(self.btn_registration_4)
        self.horizontalLayout_8.addWidget(self.widget_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.widget_9)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.stackedWidget.addWidget(self.page_clientes)
        self.page_estoque = QtWidgets.QWidget()
        self.page_estoque.setObjectName("page_estoque")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_estoque)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.page_estoque)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(16)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.txt_sistema_estoque = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.txt_sistema_estoque.setFont(font)
        self.txt_sistema_estoque.setStyleSheet("QLabel{\n"
"    color: rgb(37, 77, 122) ; \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.txt_sistema_estoque.setObjectName("txt_sistema_estoque")
        self.verticalLayout_6.addWidget(self.txt_sistema_estoque)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.img_lupa = QtWidgets.QLabel(self.widget_2)
        self.img_lupa.setMinimumSize(QtCore.QSize(51, 43))
        self.img_lupa.setMaximumSize(QtCore.QSize(51, 16777215))
        self.img_lupa.setStyleSheet("QLabel{\n"
"\n"
"    background-color: rgb(37, 77, 122)\n"
"}")
        self.img_lupa.setText("")
        self.img_lupa.setPixmap(QtGui.QPixmap(":/img/Nova pasta/lupa.png"))
        self.img_lupa.setScaledContents(True)
        self.img_lupa.setWordWrap(False)
        self.img_lupa.setIndent(1)
        self.img_lupa.setObjectName("img_lupa")
        self.horizontalLayout_5.addWidget(self.img_lupa)
        self.pesquisar = QtWidgets.QLineEdit(self.widget_2)
        self.pesquisar.setMinimumSize(QtCore.QSize(0, 43))
        self.pesquisar.setMaximumSize(QtCore.QSize(282, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pesquisar.setFont(font)
        self.pesquisar.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"")
        self.pesquisar.setObjectName("pesquisar")
        self.horizontalLayout_5.addWidget(self.pesquisar)
        spacerItem6 = QtWidgets.QSpacerItem(406, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.date_estoque = QtWidgets.QLineEdit(self.widget_2)
        self.date_estoque.setMaximumSize(QtCore.QSize(135, 16777215))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.date_estoque.setFont(font)
        self.date_estoque.setFocusPolicy(QtCore.Qt.NoFocus)
        self.date_estoque.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.date_estoque.setStyleSheet("color:rgb(37, 77, 122);")
        self.date_estoque.setObjectName("date_estoque")
        self.horizontalLayout_5.addWidget(self.date_estoque)
        self.verticalLayout_6.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.insert_product = QtWidgets.QLineEdit(self.widget_3)
        self.insert_product.setMinimumSize(QtCore.QSize(259, 61))
        self.insert_product.setMaximumSize(QtCore.QSize(320, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.insert_product.setFont(font)
        self.insert_product.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.insert_product.setObjectName("insert_product")
        self.horizontalLayout_6.addWidget(self.insert_product)
        self.insert_quantidade = QtWidgets.QLineEdit(self.widget_3)
        self.insert_quantidade.setMinimumSize(QtCore.QSize(259, 61))
        self.insert_quantidade.setMaximumSize(QtCore.QSize(320, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.insert_quantidade.setFont(font)
        self.insert_quantidade.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(19, 79, 110) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.insert_quantidade.setObjectName("insert_quantidade")
        self.horizontalLayout_6.addWidget(self.insert_quantidade)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_6.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.table_estoque = QtWidgets.QTableWidget(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_estoque.setFont(font)
        self.table_estoque.setStyleSheet("QTableWidget {\n"
"    gridline-color: rgb(37, 77, 122);\n"
"    background-color: transparent;\n"
"    outline: 0;\n"
"    border: 1px solid rgb(37, 77, 122);\n"
"    border-top: 0px\n"
"    \n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(87, 135, 189);\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(37, 77, 122);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(37, 77, 122);\n"
"    background-color: transparent;\n"
"    border-left: 0px;\n"
"    color: black;\n"
"\n"
"}\n"
"")

        self.table_estoque.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_estoque.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table_estoque.setShowGrid(True)
        self.table_estoque.setObjectName("table_estoque")
        self.table_estoque.setColumnCount(3)
        self.table_estoque.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.table_estoque.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_estoque.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.table_estoque.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table_estoque.setHorizontalHeaderItem(2, item)
        self.table_estoque.horizontalHeader().setVisible(True)
        self.table_estoque.horizontalHeader().setHighlightSections(False)
        self.table_estoque.horizontalHeader().setSortIndicatorShown(False)
        self.table_estoque.horizontalHeader().setStretchLastSection(False)
        self.table_estoque.verticalHeader().setVisible(False)
        self.table_estoque.verticalHeader().setCascadingSectionResizes(False)
        self.table_estoque.verticalHeader().setHighlightSections(False)
        self.table_estoque.verticalHeader().setMinimumSectionSize(20)
        self.table_estoque.verticalHeader().setSortIndicatorShown(False)
        self.table_estoque.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_7.addWidget(self.table_estoque)
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_cadastrar_estoque = QtWidgets.QPushButton(self.widget_8)
        self.btn_cadastrar_estoque.setMinimumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_cadastrar_estoque.setFont(font)
        self.btn_cadastrar_estoque.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cadastrar_estoque.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(37, 77, 122);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid black;\n"
"    font-size: 17px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    font-size: 15px;\n"
"    boder: 3px solid black;\n"
"}")
        self.btn_cadastrar_estoque.setObjectName("btn_cadastrar_estoque")
        self.verticalLayout_7.addWidget(self.btn_cadastrar_estoque)
        spacerItem8 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.btn_alterar_estoque = QtWidgets.QPushButton(self.widget_8)
        self.btn_alterar_estoque.setMinimumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_alterar_estoque.setFont(font)
        self.btn_alterar_estoque.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_alterar_estoque.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(37, 77, 122);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid black;\n"
"    font-size: 17px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    font-size: 15px;\n"
"    boder: 3px solid black;\n"
"}")
        self.btn_alterar_estoque.setObjectName("btn_alterar_estoque")
        self.verticalLayout_7.addWidget(self.btn_alterar_estoque)
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.btn_excluir_estoque = QtWidgets.QPushButton(self.widget_8)
        self.btn_excluir_estoque.setMinimumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_excluir_estoque.setFont(font)
        self.btn_excluir_estoque.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_excluir_estoque.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(37, 77, 122);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid black;\n"
"    font-size: 17px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    font-size: 15px;\n"
"    boder: 3px solid black;\n"
"}")
        self.btn_excluir_estoque.setObjectName("btn_excluir_estoque")
        self.verticalLayout_7.addWidget(self.btn_excluir_estoque)
        self.horizontalLayout_7.addWidget(self.widget_8, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.widget_5)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page_estoque)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.conteudo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txt_bem_vindo.setText(_translate("MainWindow", "bem vindo"))
        self.txt_cadastrar.setText(_translate("MainWindow", "CADASTRAR CLIENTE"))
        self.pesquisar_2.setPlaceholderText(_translate("MainWindow", "Pesquisar"))
        self.date_cliente.setText(_translate("MainWindow", "12:12:12"))
        self.insert_nome.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.insert_carro.setPlaceholderText(_translate("MainWindow", "Carro"))
        self.insert_numero.setPlaceholderText(_translate("MainWindow", "Numero"))
        self.insert_placa.setPlaceholderText(_translate("MainWindow", "Placa"))
        item = self.table_cliente.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "cod"))
        item = self.table_cliente.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.table_cliente.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Carro"))
        item = self.table_cliente.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Placa"))
        item = self.table_cliente.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Numero"))
        self.btn_cadastrar_cliente.setText(_translate("MainWindow", "cadastrar"))
        self.btn_alterar_cliente.setText(_translate("MainWindow", "Alterar"))
        self.btn_registration_4.setText(_translate("MainWindow", "Excluir"))
        self.txt_sistema_estoque.setText(_translate("MainWindow", "SISTEMA DE ESTOQUE"))
        self.pesquisar.setPlaceholderText(_translate("MainWindow", "Pesquisar"))
        self.date_estoque.setText(_translate("MainWindow", "12:12:12"))
        self.insert_product.setPlaceholderText(_translate("MainWindow", "Produto"))
        self.insert_quantidade.setPlaceholderText(_translate("MainWindow", "Quantidade"))
        item = self.table_estoque.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cod"))
        item = self.table_estoque.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Produto"))
        item = self.table_estoque.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantidade"))
        self.btn_cadastrar_estoque.setText(_translate("MainWindow", "cadastrar"))
        self.btn_alterar_estoque.setText(_translate("MainWindow", "Alterar"))
        self.btn_excluir_estoque.setText(_translate("MainWindow", "Excluir"))

import files_rc.img_rc as img_rc