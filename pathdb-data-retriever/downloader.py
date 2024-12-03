import sys
from PyQt5.QtWidgets import QApplication
from pathdb_data_retriever.main import PathologyDownloadManager

def main():
    app = QApplication(sys.argv)
    ex = PathologyDownloadManager()
    ex.show()
    sys.exit(app.exec_())
