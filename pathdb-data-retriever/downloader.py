import sys
from PyQt5.QtWidgets import QApplication
from pathdb_data_retriever.gui import PathologyDownloadManager  # Import from your new package

def main():
    app = QApplication(sys.argv)
    ex = PathologyDownloadManager()
    ex.show()
    sys.exit(app.exec_())
