# -*- coding: utf-8 -*-

"""
@file chronometre.py
@brief Fichier de définition de la classe Horloge et Chronomètre
"""
import math

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QPainter, QPen
import ressources
from POPUP import BottomPopup


class Horloge(QLabel):
    """
    @class Horloge
    @brief Classe définissant un widget d'horloge.
    """

    def __init__(self):
        """
        @brief Constructeur de la classe Horloge.
        """
        super().__init__()
        self.startTime = QTime(0, 0)

    def paintEvent(self, event):
        """
        @brief Gère l'événement de peinture du widget.

        @param event: Événement de peinture.
        @type event: QtGui.QPaintEvent
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        side = min(self.width(), self.height())
        painter.setViewport((self.width() - side) // 2, (self.height() - side) // 2, side, side)
        painter.setWindow(-50, -50, 100, 100)

        # Dessiner le contour de l'horloge
        circle_pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(circle_pen)
        painter.drawEllipse(-50, -50, 100, 100)

        # Dessiner les chiffres des secondes autour de l'horloge
        font = painter.font()
        font.setPixelSize(8)
        painter.setFont(font)
        for i in range(0, 60, 5):  # Dessiner les chiffres chaque 5 secondes
            angle = i * 6.0
            x = int(40 * math.sin(math.radians(angle)))
            y = int(-40 * math.cos(math.radians(angle)))
            painter.drawText(x - 5, y - 5, 10, 10, Qt.AlignCenter, str(i))

        # Dessiner l'aiguille des minutes
        minute_pen = QPen(Qt.blue, 2, Qt.SolidLine)
        painter.setPen(minute_pen)
        minute_angle = (self.startTime.minute() + self.startTime.second() / 60.0) * 6.0
        painter.drawLine(0, 0, int(40 * math.sin(math.radians(minute_angle))), int(-40 * math.cos(math.radians(minute_angle))))

        # Dessiner l'aiguille des secondes
        second_pen = QPen(Qt.red, 1, Qt.SolidLine)
        painter.setPen(second_pen)
        second_angle = self.startTime.second() * 6.0
        painter.drawLine(0, 0, int(45 * math.sin(math.radians(second_angle))), int(-45 * math.cos(math.radians(second_angle))))


class Chronometre(QWidget):
    """
    @class Chronometre
    @brief Classe définissant un widget de chronomètre.
    """

    def __init__(self, parent, num_saison, num_niveau, photoBoss):
        """
        @brief Constructeur de la classe Chronometre.

        @param parent: Widget parent.
        @type parent: QtWidgets.QWidget
        @param num_saison: Numéro de la saison.
        @type num_saison: int
        @param num_niveau: Numéro du niveau.
        @type num_niveau: int
        """
        super().__init__(parent)
        self.photoBoss = photoBoss
        self.num_saison = num_saison
        self.num_niveau = num_niveau
        self.temps = 0
        self.setObjectName("chrono")
        self.setStyleSheet("QWidget{background-color: rgba(255, 255, 255, 0.5);}")

    def initUI(self,consigne):
        """
        @brief Initialise l'interface utilisateur du chronomètre.

        @param consigne: Texte de consigne.
        @type consigne: str
        """
        self.setWindowTitle('Chronomètre')
        self.setGeometry(100, 100, 400, 600)
        self.label_question = QLabel(consigne)
        self.label_question.setAlignment(Qt.AlignCenter)
        font_question = self.label_question.font()
        font_question.setPointSize(20)
        self.label_question.setFont(font_question)

        self.label_horloge = Horloge()
        self.label_horloge.setAlignment(Qt.AlignCenter)

        self.label_numerique = QLabel()
        self.label_numerique.setAlignment(Qt.AlignCenter)
        font_numerique = self.label_numerique.font()
        font_numerique.setPointSize(20)  # Taille de police plus grande
        self.label_numerique.setFont(font_numerique)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)

        self.startTime = QTime(0, 0, 0)
        self.endTime = QTime(0, 20, 0)

        self.timer.start(1000)  # Met à jour toutes les secondes

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label_question)
        vbox.addWidget(self.label_horloge)
        vbox.addWidget(self.label_numerique)
        vbox.setSpacing(0)
        self.setLayout(vbox)

        horizon = QHBoxLayout()

        self.helper = QtWidgets.QLabel()
        self.helper.setGeometry(QtCore.QRect(1300, 625, 250, 250))
        self.helper.setText("")
        self.helper.setPixmap(QtGui.QPixmap(":/img/perso/petit-helper.png"))
        self.helper.setObjectName("helper")
        self.helper.setToolTip("Indice")
        # Connecter le clic sur l'image à la fonction pour afficher la bulle de discussion
        self.helper.mousePressEvent = self.showHintBubble
        horizon.addWidget(self.helper)

        boss = QtWidgets.QLabel()
        boss.setGeometry(QtCore.QRect(1300, 625, 250, 250))
        boss.setText("")
        boss.setPixmap(QtGui.QPixmap(f":/img/perso/{self.photoBoss}"))
        boss.setObjectName("helper")
        horizon.addWidget(boss)

        vbox.addLayout(horizon)

    def updateTime(self):
        """
        @brief Met à jour le temps affiché à chaque seconde.
        """
        self.startTime = self.startTime.addSecs(1)  # Ajouter une seconde au temps actuel
        self.temps += 1
        self.label_horloge.startTime = self.startTime
        self.label_horloge.update()

        if self.startTime >= self.endTime:
            self.timer.stop()
            self.label_horloge.setText("Temps écoulé!")
            self.label_numerique.setText("Temps écoulé!")
        else:
            self.label_horloge.setText(self.startTime.toString("hh:mm:ss"))
            self.label_numerique.setText(self.startTime.toString("hh:mm:ss"))

    def terminerChronometre(self):
        """
        @brief Arrête le chronomètre et affiche le message de fin.

        @return Temps écoulé.
        @rtype int
        """
        self.timer.stop()
        self.label_horloge.setText("Fin du niveau!")
        self.label_numerique.setText("Fin du niveau!")
        return self.temps

    def showHintBubble(self, event):
        """
        @brief Affiche une bulle d'indice lorsque l'image est cliquée.

        @param event: Événement de clic de la souris.
        @type event: QtGui.QMouseEvent
        """
        if self.num_niveau == 5:
            couleur = "rgb(38, 68, 70)"
        else:
            couleur = "rgb(70, 7, 49)"
        self.popup = BottomPopup.BottomPopup(self.num_saison, self.num_niveau, 0, couleur, True)
        self.popup.show()
