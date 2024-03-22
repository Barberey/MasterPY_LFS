from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer

from POPUP import hint

class BottomPopup(QWidget):
    """
    @brief La classe BottomPopup gère l'affichage de pop-ups inférieurs dans l'interface graphique.

    @details
    La classe BottomPopup crée des fenêtres pop-up inférieures avec des composants tels que des images, des étiquettes
    de texte et des boutons. Elle est utilisée pour afficher des dialogues dans le jeu.
    """

    def __init__(self, saison, niveau, max, couleur, ind=False, parent=None, parent_obj=None, bis=False):
        """
        @brief Initialise une nouvelle instance de la classe BottomPopup.

        @param saison: Numéro de la saison.
        @type saison: int
        @param niveau: Niveau du jeu.
        @type niveau: int
        @param max: Nombre maximum d'apparitions du pop-up.
        @type max: int
        @param couleur: Couleur de fond du pop-up.
        @type couleur: str
        @param ind: Indique si le pop-up est lié à un indice.
        @type bool
        @param parent: Parent de la fenêtre.

        @param parent_obj: Objet parent.

        @param bis: Indique si c'est une version bis du niveau.
        @type bis: bool
        """
        super(BottomPopup, self).__init__(parent)
        self.apparition = max
        self.setObjectName("fond")
        self.parent_obj = parent_obj

        self.setGeometry(250, 1080-200, 1500, 200)
        self.vide = False

        if not ind:
            bisTxt = ""
            if bis:
                bisTxt = "bis"
            file_path = f"../texte/dialogue/saison{saison}/{niveau}{bisTxt}"
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                if len(file_content.split("@@")) > 1:
                    self.vide = True
                else:
                    self.sections = [section.strip() for section in file_content.split('#')]
        else:
            indice = hint.Hint(saison, niveau)
            self.sections = [indice.getHint()]

        if not self.vide:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

            dial = self.sections[self.apparition].split("!!")

            self.photo = QLabel(self)
            self.photo.setPixmap(QPixmap(dial[0]))

            self.label = QLabel(dial[1], self)

            horizon = QtWidgets.QHBoxLayout()
            horizon.addWidget(self.photo)
            spacerItemH1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            horizon.addItem(spacerItemH1)
            horizon.addWidget(self.label)
            spacerItemH2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            horizon.addItem(spacerItemH2)

            font = self.label.font()
            font.setPointSize(16)
            self.label.setFont(font)

            self.close_button = QPushButton("Continuer", self)
            self.close_button.setFont(font)
            self.close_button.clicked.connect(self.close_popup)

            layout = QtWidgets.QGridLayout(self)
            layout.addLayout(horizon, 1, 0, 1, 1)
            layout.addWidget(self.close_button, 2, 0, 1, 1)
            layout.setVerticalSpacing(20)

            if parent is None:
                self.setStyleSheet(
                    "QWidget#fond { background-color: " + couleur + " ;} "
                    "QLabel { color: white; } "
                    "QPushButton { color: white; background-color: black; }")

            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            layout.addItem(spacerItem, 0, 0, 1, 1)
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            layout.addItem(spacerItem1, 3, 0, 1, 1)

            self.close_button.setEnabled(False)

            self.enable_close_button_timer = QTimer(self)
            self.enable_close_button_timer.timeout.connect(self.enable_close_button)
            self.enable_close_button_timer.start(1500)

    def enable_close_button(self):
        """
        @brief Active le bouton de fermeture après un délai.
        """
        self.close_button.setEnabled(True)

    def close_popup(self):
        """
        @brief Gère la fermeture du pop-up.
        """
        self.apparition += 1
        if self.apparition < len(self.sections):
            self.updateTxt()
            self.update()
        else:
            if self.parent_obj is None:
                self.close()
            else:
                self.parent_obj.fin()

    def updateTxt(self):
        """
        @brief Met à jour le texte et l'image du pop-up en fonction de l'apparition actuelle.
        """
        dial = self.sections[self.apparition].split("!!")
        self.photo.setPixmap(QPixmap(dial[0]))
        self.label.setText(dial[1])
