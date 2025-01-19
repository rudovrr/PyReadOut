import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from flask import Flask, request

HOST = "127.0.0.1"
PORT = 8027


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Output message")

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


application = QApplication(sys.argv)
window = MainWindow()
window.show()


class ApplicationThread(QtCore.QThread):
    def __init__(self, application1, host, port=5000):
        super(ApplicationThread, self).__init__()
        self.application = application1
        self.host = host
        self.port = port

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=self.port, threaded=True)


app = Flask(__name__)


@app.route('/', methods=['POST'])
def add():
    f = request.get_json()
    window.label.setText(f['message'])
    return "Add the json request."


webapp = ApplicationThread(app, HOST, PORT)
webapp.start()
application.exec()
