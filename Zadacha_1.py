from PyQt5 import QtCore, QtGui, QtWidgets
import pygame, requests, sys, os


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("№1")
        Form.resize(218, 139)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_login = QtWidgets.QLineEdit(Form)
        self.le_login.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.le_login.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.le_login)
        self.le_password = QtWidgets.QLineEdit(Form)
        self.le_password.setObjectName("lineEdit_2")
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.le_password)
        self.pb_login = QtWidgets.QPushButton(Form)
        self.pb_login.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pb_login)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "№1"))
        self.le_login.setPlaceholderText(_translate("Form", "Широта и долгота"))
        self.le_password.setPlaceholderText(_translate("Form", "Масштаб"))
        self.pb_login.setText(_translate("Form", "Готово"))


class Authorization(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pb_login.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.le_login, self.ui.le_password]

    def auth(self):
        name = self.ui.le_login.text()
        zoom = self.ui.le_password.text()
        map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=name, z=zoom,
                                                                                        type="map")
        response = requests.get(map_request)
        map = "map.png"
        with open(map, "wb") as file:
            file.write(response.content)
        ex_auth.hide()
        main(map)



def main(map):
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:  # Выход из программы
            os.remove(map_file)
            sys.exit(app.exec_())
            break
        # Создаем файл
        map_file = map
        # Рисуем картинку, загружаемую из только что созданного файла.
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    # Удаляем файл с изображением.
    os.remove(map_file)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex_auth = Authorization()
    ex_auth.show()

    sys.exit(app.exec_())

