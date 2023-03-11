from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QLineEdit
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
import sys
from database import Database
from login import Login
from estoque import Estoque
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QPixmap, QIcon


buttonn_show_password = 0


class login(QWidget):

    def __init__(self, *args, **argv):
        super(login, self).__init__(*args, **argv)
        self.login = Login()
        self.login.setupUi(self)
        self.login.login_button.clicked.connect(self.logar)
        self.login.register.clicked.connect(self.register_user)   
        self.login.show_password.clicked.connect(self.show_password)
        self.db = Database()
        # self.db.manipulation("CREATE DATABASE IF NOT EXISTS auto_ar")
        self.db.manipulation('CREATE TABLE IF NOT EXISTS credentials'
                             '(usuario text NOT NULL, senha text'
                             'NOT NULL);')

    def show_messege_register(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("registered")
        self.msg.setText("usuario registrado")
        self.msg.setIcon(QMessageBox.Information)
        self.msg.exec_()

    # habilita opção de mover a janela
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def enter_storage(self):
        self.storage = storage()
        self.storage.show()

    def get_credentials(self):
        global name_user
        self.user_input = self.login.insert_user.text()
        self.password_input = self.login.insert_password.text()
        name_user = self.user_input

    # verifica se existe o usuário e senha no bd
    def cheking_if_the_credentials_exist(self):
        self.get_credentials()
        if self.user_input and self.password_input != "":
            try:
                self.all_user_and_password = self.db.Query(
                    'SELECT usuario, senha FROM credentials'
                )

            except IndexError:
                pass
            finally:
                self.login.insert_password.setText('')

    # verifica se as credenciais bate com os dados do bd
    def logar(self):
        self.cheking_if_the_credentials_exist()
        name_passwod = (self.user_input, self.password_input)
        if len(self.user_input) and len(self.password_input) > 0:
            if name_passwod in self.all_user_and_password:
                self.enter_storage()
                self.hide()
            else:
                self.login.error_login_messeger.setText(
                    "Usuário ou senha invalido"
                    )

    # ver e esconder senha
    def show_password(self):
        global buttonn_show_password
        buttonn_show_password += 1

        if buttonn_show_password % 2 == 0:
            self.login.show_password.setStyleSheet(
                "QPushButton {\n"
                "\n"
                "    border: none;\n"
                "    background: url(icons/ver_senha.png);\n"
                "    background-position: center;"
                "    background-repeat: norepeat;"
                "}\n"
                )
            self.login.insert_password.setEchoMode(QLineEdit.EchoMode.Password)

        elif buttonn_show_password % 2 == 1:
            self.login.show_password.setStyleSheet(
                "QPushButton {\n"
                "\n"
                "    border: none;\n"
                "    background: url(icons/bloquear_senha.png);\n"
                "    background-position: center;"
                "    background-repeat: norepeat;"
                "}\n"
                )
            self.login.insert_password.setEchoMode(QLineEdit.EchoMode.Normal)

    def register_user(self):
        self.get_credentials()
        if len(self.user_input) and len(self.password_input) > 0:

            users = self.db.Query('SELECT usuario, senha FROM credentials')

            if (self.user_input, self.password_input) not in users:
                self.db.manipulation(
                    f'INSERT INTO credentials VALUES '
                    f' ("{self.user_input}", "{self.password_input}" )')
                self.show_messege_register()


class storage(QMainWindow):
    def __init__(self, *args, **argv):
        super(storage, self).__init__(*args, **argv)
        self.storage = Estoque()
        self.storage.setupUi(self)
        self.storage.bnt_add_cliente.clicked.connect(
            lambda: self.storage.stackedWidget.setCurrentWidget(
                self.storage.page_clientes))

        self.storage.btn_estoque.clicked.connect(
            lambda: self.storage.stackedWidget.setCurrentWidget(
                self.storage.page_estoque))

        self.storage.btn_pix.clicked.connect(self.show_pix)
        self.storage.txt_bem_vindo.setText(
            f'Bem Vindo(a) - {name_user.capitalize()}'
            )
        self.db = Database()
        self.db.manipulation(
            'CREATE TABLE IF NOT EXISTS clientes \
            (cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, \
             carro TEXT, placa TEXT, numero TEXT ); '
            )

        self.db.manipulation(
            'CREATE TABLE IF NOT EXISTS produtos \
            (cod INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            produto TEXT, quantidade TEXT); ')

        self.storage.btn_cadastrar_cliente.clicked.connect(
            self.insert_bd_cliente
            )
        self.storage.btn_cadastrar_estoque.clicked.connect(
            self.insert_bd_storage
            )
        self.storage.btn_sair.clicked.connect(self.exit)
        self.table_storage()
        self.storage.table_estoque.clicked.connect(self.set_text_storage)
        self.storage.btn_alterar_estoque.clicked.connect(self.change_storage)
        self.storage.btn_excluir_estoque.clicked.connect(self.delete)

        self.table_client()
        self.storage.table_cliente.clicked.connect(self.set_text_client)
        self.storage.btn_alterar_cliente.clicked.connect(self.change_client)
        self.storage.btn_registration_4.clicked.connect(self.delete_client)

        self.storage.btn_menu.clicked.connect(self.menu)
        self.storage.pesquisar.textChanged.connect(self.search_bar_storage)
        self.storage.pesquisar_2.textChanged.connect(self.search_bar_cliente)
        
        # Iniciando relógio
        tempo = QTimer(self)
        tempo.timeout.connect(self.displaytime)
        tempo.start(1000)

    def default_fields(self):
        self.storage.insert_nome.setText('')
        self.storage.insert_carro.setText('')
        self.storage.insert_placa.setText('')
        self.storage.insert_numero.setText('')
        self.storage.insert_product.setText('')
        self.storage.insert_quantidade.setText('')

    def show_pix(self):
        self.pix = QMessageBox()
        self.pix.setWindowTitle('PIX')
        self.pix.setWindowIcon(QIcon("icons/logo_pix.png"))
        self.pix.setIconPixmap(QPixmap("icons/qrcode.png"))
        self.pix.exec_()

    def displaytime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.storage.date_estoque.setText(displayText)
        self.storage.date_cliente.setText(displayText)

    def table_storage(self):

        self.db.manipulation(
            'CREATE TABLE IF NOT EXISTS produtos '
            '(cod INTEGER PRIMARY KEY AUTOINCREMENT, produto'
            ' TEXT, quantidade TEXT); '
            )
        all = self.db.Query('SELECT * FROM produtos;')
        self.storage.table_estoque.clearContents()
        self.storage.table_estoque.setRowCount(len(all))

        for row, text in enumerate(all):
            for column, data in enumerate(text):
                self.storage.table_estoque.setItem(
                    row, column, QTableWidgetItem(str(data))
                    )

    def insert_bd_storage(self):
        product = self.storage.insert_product.text()
        amount = self.storage.insert_quantidade.text()
        if len(product) and len(amount) != 0:
            all_products = self.db.Query('SELECT produto FROM produtos;')
            all_product = list()
            for item in all_products:
                all_product.append(item[0])
            if not product in all_product:
                self.db.manipulation(
                    f'INSERT INTO produtos (produto, quantidade) VALUES ("{product}", "{amount}")'
                    )
            self.table_storage()
        self.storage.insert_product.setPlaceholderText('Produto')
        self.storage.insert_quantidade.setPlaceholderText('Quantidade')
        self.default_fields()

    def set_text_storage(self):
        row_table = self.storage.table_estoque.currentRow()
        all_product = self.db.Query(
            'SELECT produto, quantidade FROM produtos;'
            )
        product, amount = all_product[row_table]
        self.storage.insert_product.setText(product)
        self.storage.insert_quantidade.setText(amount)
        return row_table

    def change_storage(self):
        row_table = self.storage.table_estoque.currentRow() + 1
        item = self.storage.insert_product.text()
        amount = self.storage.insert_quantidade.text()

        if len(item) or len(amount) > 0:
            self.db.manipulation(
                f" UPDATE produtos SET produto = '{item}', "
                f"quantidade = '{amount}' WHERE cod = '{str(row_table)}' "
                )
            self.table_storage()

        self.storage.insert_product.clear()
        self.storage.insert_quantidade.clear()
        self.storage.insert_product.setPlaceholderText('Produto')
        self.storage.insert_quantidade.setPlaceholderText('Quantidade')

    def delete(self):
        # num = self.storage.table_estoque.currentRow() + 1S
        product = self.storage.insert_product.text()
        amount = self.storage.insert_quantidade.text()
        self.db.manipulation(f"DELETE FROM produtos WHERE produto = '{product}' AND quantidade = '{amount}'  ")

        all_items = self.db.Query("SELECT produto, quantidade FROM produtos;")
        self.db.manipulation('DROP TABLE produtos;')
        for cod, item in enumerate(all_items):
            self.db.manipulation(
                'CREATE TABLE IF NOT EXISTS produtos '
                '(cod INTEGER PRIMARY KEY AUTOINCREMENT, '
                'produto TEXT, quantidade TEXT ); '
                )
            self.db.manipulation(f'INSERT INTO produtos (produto, quantidade) \
                                  VALUES ("{item[0]}", "{item[1]}" ); ')

        self.storage.insert_product.clear()
        self.storage.insert_quantidade.clear()
        self.storage.insert_product.setPlaceholderText('Produto')
        self.storage.insert_quantidade.setPlaceholderText('Quantidade')
        self.table_storage()

    def search_bar_storage(self):
        var = self.storage.pesquisar.text()
        self.storage.table_estoque.clearContents()
        all = self.db.Query(
            f"SELECT * FROM produtos Where produto Like '{var}%' ;"
            )
        self.storage.table_estoque.setRowCount(len(all))

        for row, text in enumerate(all):
            for column, data in enumerate(text):
                self.storage.table_estoque.setItem(
                    row, column, QTableWidgetItem(str(data))
                    )

    def default_placeholder_cliente(
            self, nome='Nome', carro='Carro',
            placa='Placa', numero='Numero'):
        self.storage.insert_nome.setPlaceholderText(nome)
        self.storage.insert_carro.setPlaceholderText(carro)
        self.storage.insert_placa.setPlaceholderText(placa)
        self.storage.insert_numero.setPlaceholderText(numero)

    def insert_bd_cliente(self):
        name = self.storage.insert_nome.text()
        car = self.storage.insert_carro.text()
        plate = self.storage.insert_placa.text().upper()
        number = self.storage.insert_numero.text()
        if len(name) and len(number) != 0:
            self.db.manipulation(
                f'INSERT INTO clientes (nome, carro, placa, numero) VALUES \
                    ("{name}", "{car}", "{plate}", "{number}") ')
            self.table_client()
        self.default_placeholder_cliente()
        self.default_fields()
     
    def table_client(self):
        self.db.manipulation(
            'CREATE TABLE IF NOT EXISTS clientes'
            '(cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, \
                carro TEXT, placa TEXT, numero TEXT); '
            )
        all = self.db.Query('SELECT * FROM clientes;')
        self.storage.table_cliente.clearContents()
        self.storage.table_cliente.setRowCount(len(all))

        for row, text in enumerate(all):
            for column, data in enumerate(text):
                self.storage.table_cliente.setItem(
                    row, column, QTableWidgetItem(str(data))
                    )

    def table_cell_cliente(self):
        row_table = self.storage.table_cliente.currentRow() 
        all_product = self.db.Query(
            'SELECT nome, carro, placa, numero FROM clientes;'
            )
        nome, carro, placa, numero = all_product[row_table]
        self.default_placeholder_cliente(nome, carro, placa, numero)
        return row_table

    def set_text_client(self):
        row_table = self.storage.table_cliente.currentRow()
        all_names = self.db.Query(
            'SELECT nome, carro, placa, numero FROM clientes;'
            )
        name, car, plate, number = all_names[row_table]

        name = self.storage.insert_nome.setText(name)
        number = self.storage.insert_numero.setText(number)
        plate = self.storage.insert_placa.setText(plate)
        car = self.storage.insert_carro.setText(car)

    def change_client(self):
        row_table = self.storage.table_cliente.currentRow() + 1

        name = self.storage.insert_nome.text()
        number = self.storage.insert_numero.text()
        plate = self.storage.insert_placa.text()
        car = self.storage.insert_carro.text()
        if len(name) and len(number):
            self.db.manipulation(
                f" UPDATE clientes SET nome = '{name}', carro = '{car}',"
                f"placa = '{plate}', numero = '{number}'\
                WHERE cod = '{row_table}'")
        self.table_client()
        self.default_placeholder_cliente()
        self.default_fields()

    def delete_client(self):
        row_table = self.table_cell_cliente() + 1
        self.db.manipulation(f"DELETE FROM clientes WHERE cod = '{row_table}'")
        all_items = self.db.Query(
            "SELECT nome, carro, placa, numero  FROM clientes;"
            )
        self.db.manipulation('DROP TABLE clientes')
        for item in all_items:
            self.db.manipulation(
                'CREATE TABLE IF NOT EXISTS clientes '
                '(cod INTEGER PRIMARY KEY AUTOINCREMENT, '
                'nome TEXT, carro TEXT, placa TEXT, '
                'numero TEXT); '
                )
            self.db.manipulation(
                f'INSERT INTO clientes (nome, carro, placa, numero) '
                f'VALUES ("{item[0]}", "{item[1]}", "{item[2]}", "{item[3]}");'
                )
        self.storage.insert_nome.clear()
        self.storage.insert_carro.clear()
        self.storage.insert_placa.clear()
        self.storage.insert_numero.clear()
        self.default_placeholder_cliente()
        self.table_client()

    def menu(self):
        menu = self.storage.menu_animado.width()
        if menu == 0:
            new_menu = 149
        else:
            new_menu = 0

        self.animation = QtCore.QPropertyAnimation(
            self.storage.menu_animado, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(menu)
        self.animation.setEndValue(new_menu)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutSine)
        self.animation.start()

    def search_bar_cliente(self):
        var = self.storage.pesquisar_2.text()
        self.storage.table_cliente.clearContents()
        self.storage.table_cliente.setRowCount(0)
        all = self.db.Query(
            f"SELECT * FROM clientes Where nome Like '{var}%';"
            )
        self.storage.table_cliente.setRowCount(len(all))

        for row, text in enumerate(all):
            for column, data in enumerate(text):
                self.storage.table_cliente.setItem(
                    row, column, QTableWidgetItem(str(data))
                    )

    def exit(self):
        self.close()


app = QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window = login()
window.show()
sys.exit(app.exec_())
