

# import sys, os
# from pathlib import Path
# import pandas as pd # import Pandas
# from tqdm import tqdm


# from widgets_alignment import set_alignment

# from PyQt6.QtWidgets import (
#     QApplication, QStyleFactory,
#     QMainWindow,
#     QWidget,
#     QFileDialog
# )
# from PyQt6.QtGui import QColor
# from PyQt6.QtCore import Qt, QThread, pyqtSignal
# from PyQt6 import uic

# import random

# import string




# class CICML(QMainWindow):

#     progress = pyqtSignal(int)
#     status = pyqtSignal(str)
#     finished = pyqtSignal(pd.DataFrame)


#     def __init__(self, parent = None, flags = Qt.WindowType(0)):
#         super().__init__(parent, flags)

#         uic.loadUi(r'designs\self_things.ui', self)

#         self.setWindowTitle('Test')
#         self.resize(300, 200)

#         self.submit_btn.setText('Submit') #= QPushButton('Submit')
#         self.submit_btn.setFixedSize(70, 28)
#         self.submit_btn.clicked.connect(self.update_status)

#         self.upload_btn.clicked.connect(self.upload_file)

#         self.status_lbl.setText('Listening 👂')
#         # self.status_lbl.adjustSize()

#         self.layout.setAlignment(set_alignment('center'))
#         self.layout.setSpacing(20)

#         container = QWidget()
#         container.setLayout(self.layout)
#         self.setCentralWidget(container)


#     def update_status(self):
#         chars = list('0123456789') + list(string.ascii_letters)
#         random.shuffle(chars)
#         self.status_lbl.setText(''.join(chars)[:14])


#     def upload_file(self):
#         file_path, _ =  QFileDialog.getOpenFileName(self,
#                                                  caption='Upload file',
#                                                  directory="",
#                                                  filter="Excel Files (*.xlsx *.xls *.xlsm *.csv)")
#         if file_path == '':
#             return

#         cols = self.__handle_file(file_path)
#         cols = ', '.join(cols)

#         # self.update_status()


#     def __handle_file(self, filepath: str):        
#         file_ext = Path(filepath).suffix

#         match file_ext:
#             case '.xlsx' | '.xls' | '.xlsm':
#                 return
#             case '.csv':
#                 df = self.__load_csv(filepath)
#                 return list(df.columns)
#             case _: return pd.DataFrame()


#     def __load_csv(self, file_path):
#         self.thread = CsvLoaderThread(file_path)
#         self.thread.progress.connect(self.update_progress)
#         self.thread.status.connect(self.status_lbl.setText)
#         self.thread.finished.connect(self.handle_csv_loaded)
#         self.thread.start()
    
    
    
# class CsvLoaderThread(QThread):

#     progress = pyqtSignal(int)
#     status = pyqtSignal(str)
#     finished = pyqtSignal(pd.DataFrame)


#     def __init__(self, file_path, chunksize=10000):
#         super().__init__()
#         self.file_path = file_path
#         self.chunksize = chunksize


#     def run(self):
#         chunks = []
#         total_rows = sum(1 for _ in open(self.file_path)) - 1
#         loaded_rows = 0

#         for chunk in pd.read_csv(self.file_path, chunksize=self.chunksize):
#             chunks.append(chunk)
#             loaded_rows += len(chunk)
#             percent = int((loaded_rows / total_rows) * 100)
#             self.progress.emit(percent)
#             self.status.emit(f"Loading: {percent}%")

#         df = pd.concat(chunks)
#         self.status.emit("✅ Done")
#         self.finished.emit(df)

        

        

# app = QApplication(sys.argv)
# app.setStyle('windows11')
# cicml = CICML()
# cicml.show()
# sys.exit(app.exec())


import sys
from pathlib import Path
import pandas as pd
import random
import string

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QDialog
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6 import uic


class CsvLoaderThread(QThread):
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    finished = pyqtSignal(pd.DataFrame)

    def __init__(self, file_path, chunksize=10000):
        super().__init__()
        self.file_path = file_path
        self.chunksize = chunksize

    def run(self):
        chunks = []
        try:
            total_rows = sum(1 for _ in open(self.file_path, encoding='utf-8')) - 1
            if total_rows <= 0:
                self.status.emit("❌ CSV is empty.")
                self.finished.emit(pd.DataFrame())
                return

            loaded_rows = 0
            for chunk in pd.read_csv(self.file_path, chunksize=self.chunksize):
                chunks.append(chunk)
                loaded_rows += len(chunk)
                percent = int((loaded_rows / total_rows) * 100)
                self.progress.emit(percent)
                self.status.emit(f"Loading: {percent}%")

            df = pd.concat(chunks)
            self.status.emit("✅ Done")
            self.finished.emit(df)

        except Exception as e:
            self.status.emit(f"❌ Error: {str(e)}")
            self.finished.emit(pd.DataFrame())


class CICML(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowType(0)):
        super().__init__(parent, flags)

        # Load UI from .ui file
        uic.loadUi('designs/self_things.ui', self)

        self.setWindowTitle('Test')
        self.resize(500, 250)
        # self.adjustSize()

        # Connect buttons
        self.submit_btn.setText('Submit')
        self.submit_btn.setFixedSize(70, 28)
        # self.submit_btn.clicked.connect(self.random_status)

        self.upload_btn.clicked.connect(self.upload_file)

        self.status_lbl.setText('Listening 👂')
        self.status_lbl.adjustSize()


    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            caption='Upload file',
            directory="",
            filter="CSV Files (*.csv);;Excel Files (*.xlsx *.xls *.xlsm)"
        )
        if file_path:
            self.__handle_file(file_path)

    def __handle_file(self, filepath: str):
        ext = Path(filepath).suffix
        if ext == '.csv':
            self.__load_csv(filepath)
        elif ext in {'.xls', '.xlsx', '.xlsm'}:
            self.status_lbl.setText("Excel support not implemented yet.")
        else:
            self.status_lbl.setText("Unsupported file type.")

    def __load_csv(self, file_path):
        self.filename = Path(file_path).name
        self.thread = CsvLoaderThread(file_path)
        self.thread.progress.connect(self.update_progress)
        self.thread.status.connect(self.update_progress)
        self.thread.finished.connect(self.handle_csv_loaded)
        self.thread.start()


    def update_progress(self, percent):
        self.main_status_lbl.setText(f'Uploading {self.filename}')
        self.status_lbl.setText(f"{percent}%")

    def handle_csv_loaded(self, df):
        if df.empty:
            self.status_lbl.setText("No data loaded.")
        else:
            self.status_lbl.setText(f"Loaded {len(df)} rows.")
        self.setWindowTitle("Done")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion') 
    window = CICML()
    window.show()
    sys.exit(app.exec())
