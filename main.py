import sys

from PyQt5.QtWidgets import QApplication

from UI_qt.mainWindow import MainWindow


def main():
    # 界面
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()