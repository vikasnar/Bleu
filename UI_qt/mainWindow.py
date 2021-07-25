from PyQt5.QtWidgets import QMainWindow

from UI_qt.mainWindowUI import Ui_MainWindow
from utils.calculatebleu import BLEU


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        # super(MainWindow, self).__init__(*args, **kwargs)
        super().__init__()
        self.setupUi(self)
        self._init_slot_connect()

    def _init_slot_connect(self):
        self.bleu_pushButton.clicked.connect(self.calc_bleu)

    def calc_bleu(self):
        candidate = self.candidate_textEdit.toPlainText()
        reference = self.reference_textEdit.toPlainText()
        print(candidate, reference)
        candidate = [candidate]
        reference = [[reference]]
        # candidate = ["It is a guide to action which ensures that the military always obeys the commands of the party."]
        # reference = [["It is a guide to action that ensures that the military will forever heed Party commands."]]
        bleu = BLEU(candidate, reference)
        print(bleu)
        self.output_lineEdit.setText(str(bleu))


