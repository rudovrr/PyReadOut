import http.client
import json
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label1 = QLabel("Введите сообщение:")
        self.input = QLineEdit()
        self.button = QPushButton("Отправить!")
        self.label2 = QLabel()
        self.button.clicked.connect(self.the_button_was_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.label2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        headers = {'Content-type': 'application/json'}
        foo = {'message': self.input.text()}
        json_foo = json.dumps(foo)
        conn = http.client.HTTPConnection("127.0.0.1:8027")
        conn.request("POST", "", json_foo, headers)
        response = conn.getresponse()
        if response.getcode() == 200:
            self.label2.setText("Отправлено!")
        else:
            self.label2.setText("Ошибка!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
