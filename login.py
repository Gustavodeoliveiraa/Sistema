from PyQt5 import QtCore, QtGui, QtWidgets



class Login(object):

    def setupUi(self, MainWindow):

        #configurações da janela principal 
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.resize(819, 612)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
    
        #configuraçoes da parte esquerda
        self.blue = QtWidgets.QFrame(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(30, 40, 411, 551))
        self.blue.setStyleSheet("QFrame{\n"
        "    background: rgb(37, 77, 122);\n"
        "    border-radius: 17px;\n"
        "     border: 3px solid rgb(13, 53, 74);\n"
        "\n"
        "}")
        self.blue.setObjectName("blue")

        #logo sol e neve
        self.logo_sun = QtWidgets.QFrame(self.blue)
        self.logo_sun.setGeometry(QtCore.QRect(3, 20, 75, 80))
        self.logo_sun.setStyleSheet("background-image: url(:/newPrefix/imagens/aaaa.png);\n"
        "border: None;\n"
        "background-repeat: norepeat;\n"
        "background-position: center; ")
        self.logo_sun.setObjectName("logo_sun")

        #nome_empresa
        self.auto_ar_jr = QtWidgets.QFrame(self.blue)
        self.auto_ar_jr.setGeometry(QtCore.QRect(80, 20, 321, 80))
        self.auto_ar_jr.setStyleSheet("background-image: url(:/newPrefix/imagens/auto ar jr.png);\n"
        "border: None;\n"
        "background-repeat: norepeat;\n"
        "background-position: center; ")
        self.auto_ar_jr.setObjectName("auto_ar_jr")

        #nome_empresa
        self.ar_condicionado_automotivo = QtWidgets.QFrame(self.blue)
        self.ar_condicionado_automotivo.setGeometry(QtCore.QRect(100, 90, 281, 41))
        self.ar_condicionado_automotivo.setStyleSheet(
        "background-image: url(:/newPrefix/imagens/ar condicionado automotivo.png);\n"
        "border: None;\n"
        "background-repeat: norepeat;\n"
        "background-position: center; \n"
        "")
        self.ar_condicionado_automotivo.setObjectName("ar_condicionado_automotivo")
 
        #img storage
        self.storage = QtWidgets.QWidget(self.blue)
        self.storage.setGeometry(QtCore.QRect(0, 180, 411, 281))
        self.storage.setStyleSheet("background: url(:/newPrefix/Icones-Controle-de-Estoque-05.png);\n"
        "background-image: url(:/newPrefix/imagens/Icones-Controle-de-Estoque-05.png);\n"
        "background-repeat: norepeat;\n"
        "background-position: center;")
        self.storage.setObjectName("storage")

        self.text_register = QtWidgets.QTextBrowser(self.blue)
        self.text_register.setGeometry(25, 460, 331, 51)
        self.text_register.setStyleSheet("border: none;\n" \
        "font-size: 15px;\n" "color: white;"
        )
        self.text_register.setText("Para registrar preencha os campos e pressione o botão register")
        self.text_register.setObjectName("text_of_register")


        #configuração lado direita
        self.white = QtWidgets.QFrame(self.centralwidget)
        self.white.setGeometry(QtCore.QRect(438, 69, 331, 491))
        self.white.setStyleSheet("QFrame{\n"
        "    background: white;\n"
        "    border: 3px solid rgb(13, 53, 74);\n"
        "    border-top-right-radius: 17px;\n"
        "    border-bottom-right-radius: 17px;\n"
        "\n"
        "}")
        self.white.setObjectName("white")

        #close button
        self.close_button = QtWidgets.QPushButton(self.white)
        self.close_button.setGeometry(QtCore.QRect(275, 6, 44, 23))
        self.close_button.clicked.connect(MainWindow.close)
        self.close_button.setText("X")
        self.close_button.setObjectName('close_buttom')
        self.close_button.setStyleSheet("QPushButton{\n" 
        # "   background-color: white;\n"
        "   border: None;\n"
        "   background: white;\n"
        "   border-radius: 5px;\n"
        "   color: white;\n"
        "   font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        # "   color: black;\n"
        "   background: red;"
        "   Border:2px solid black;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "   paddin: 6px;\n"
        "   font-size: 12px;\n"
        "   Border: 2px solid black;\n"
        "}")
        self.close_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        
        #campo usuario
        self.insert_user = QtWidgets.QLineEdit(self.white)
        self.insert_user.setGeometry(QtCore.QRect(40, 170, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        self.insert_user.setFont(font)
        self.insert_user.setStyleSheet("QLineEdit {\n"
        "\n"
        "    border-radius: 10px;\n"
        "    background: rgba(70, 72, 73, 0.1);\n"
        "    border-radius: 16px;\n"
        "    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
        "    text-size:40px;\n"
        "    border: 2px solid black;\n"
        "    padding-left:13px;\n"
        "\n"
        "\n"
        "    \n"
        "}\n"
        "\n"
        "QLineEdit:hover {\n"
        "    background: rgba(70, 72, 73, 0.19);\n"
        "    border: 1px solid black;\n"
        "}")
        self.insert_user.setText("")
        self.insert_user.setObjectName("insert_user")


        ##campo senha
        self.insert_password = QtWidgets.QLineEdit(self.white)
        self.insert_password.setGeometry(QtCore.QRect(40, 240, 241, 51))
        self.insert_password.setFont(font)
        self.insert_password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.insert_password.setMouseTracking(True)
        self.insert_password.setStyleSheet("QLineEdit {\n"
        "\n"
        "    border-radius: 10px;\n"
        "    background: rgba(70, 72, 73, 0.1);\n"
        "    border-radius: 16px;\n"
        "    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
        "    text-size: 40px;\n"
        "    padding-left: 13px;\n"
        "    border: 2px solid black;\n"
        "}\n"
        "\n"
        "QLineEdit:hover {\n"
        "    background: rgba(70, 72, 73, 0.19);\n"
        "    border: 1px solid black;\n"
        "}")
        self.insert_password.setText("")
        self.insert_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.insert_password.setObjectName("insert_password")

        #opçao de mostrar senha
        self.show_password = QtWidgets.QPushButton(self.white)
        self.show_password.setGeometry(240, 250, 31, 31)
        self.show_password.setStyleSheet("QPushButton {\n"
        "\n"
        "    border: none;\n"
        "    background: url(icons/ver_senha.png);\n"
        "    background-position: center;"
        "    background-repeat: norepeat;"
        "}\n")
       
        #atualiazndo
        self.error_login_messeger = QtWidgets.QTextBrowser(self.white)
        self.error_login_messeger.setGeometry(40, 300, 211, 41)
        self.error_login_messeger.setStyleSheet("border: none;\n" 
        "text-size:13px;\n"
        "font-weight: bold;"
        "color: red;")
        self.error_login_messeger.setObjectName("message_error")
        self.error_login_messeger.setText("")

        
        #title ( acesso ao sistema )
        self.title = QtWidgets.QLabel(self.white)
        
        self.title.setGeometry(QtCore.QRect(10, 30, 301, 111))
        self.title.setFont(font)
        self.title.setStyleSheet("QLabel {\n"
        "    border:None;\n"
        "    font-size: 30px;\n"
        "}")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        
        #botão login
        self.login_button = QtWidgets.QPushButton(self.white)
        self.login_button.setGeometry(QtCore.QRect(70, 360, 181, 41))
        self.login_button.setStyleSheet("    QPushButton{\n"
        "    background-color: rgb(99 , 139 , 224);\n"
        "    border: 1.3px solid black;\n"
        "    border-radius:10px;\n"
        "    color: white;\n"
        "    font-size: 17px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "\n"
        "    background-color: rgb(50, 88, 171);\n"
        "    font-size: 18px;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:pressed{\n"
        "    border: 2px solid black;\n"
        "    background-color: rgb(50, 88, 171);\n"
        "    font-size: 14px;\n"
        "}")
        self.login_button.setObjectName("login_button")
   
        #botão registrar
        self.register = QtWidgets.QPushButton(self.white)
        self.register.setGeometry(QtCore.QRect(100, 410, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.register.setFont(font)
        self.register.setStyleSheet("    QPushButton{\n"
        "    background-color: rgb(99 , 139 , 224);\n"
        "    border-radius:10px;\n"
        "    background: rgba(0, 0, 0, 0.2);\n"
        "    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
        "    backdrop-filter: blur(5px);\n"
        "    -webkit-backdrop-filter: blur(5px);\n"
        "    border: 1px solid rgba(0, 0, 0, 0.3);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "\n"
        "    background-color: white;\n"
        "    border: 2px solid black;\n"
        "    font-size: 11px ;\n"
        "    \n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:pressed{\n"
        "    margin: 2px;\n"
        "    border-radius:10px;\n"
        "    font-size: 10px ;\n"
        "}")
        self.register.setObjectName("register")


        #esqueceu senha 
        self.forgout = QtWidgets.QPushButton(self.white)
        self.forgout.setGeometry(QtCore.QRect(70, 450, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.forgout.setFont(font)
        self.forgout.setStyleSheet("QPushButton{\n"
        "    background-color: white;\n"
        "    Border:None;\n"
        "    border-radius: 5px;\n"
        "    \n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    background-color: rgba(213, 213, 213, 100);\n"
        "    border-radius: 5px\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgba(191, 191, 191, 100);\n"
        "    border:1px solid black ;\n"
        "    border-radius: 5px;\n"
        "    font-size: 9px;\n"
        "}")
        self.forgout.setObjectName("forgout")

      

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.insert_password.setPlaceholderText(_translate("MainWindow", " Password"))
        self.insert_user.setPlaceholderText(_translate("MainWindow", " Username"))
        self.title.setText(_translate("MainWindow", "Acesso ao Sistema"))


        self.forgout.setText(_translate("MainWindow", "Forgout your User or Password?"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.register.setText(_translate("MainWindow", "Register"))


import files_rc.nova_pasta_rc as nova_pasta_rc


# if __name__ == "__main__":

#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Login()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
