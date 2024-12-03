import sys
from PyQt5.QtWidgets import QApplication
from main import PathologyDownloadManager

def main():
    app = QApplication(sys.argv)
    ex = PathologyDownloadManager()
    ex.show()
    sys.exit(app.exec_())
