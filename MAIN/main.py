# -*- coding: utf-8 -*-

"""
@file main.py
@brief Fichier du main
"""
from PyQt5 import QtCore

from IHM import main_window
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import sys
import faulthandler


def ratio_size(tailleStd, type):
    """
    Calcule le ratio en fonction de la taille de l'écran.

    @param tailleStd Taille standard pour la comparaison.
    @type tailleStd int

    @param type 0 pour la largeur, 1 pour la hauteur.
    @type type int

    @return Le ratio calculé.
    @return float
    """
    desktop = QDesktopWidget()
    screenRect = desktop.screenGeometry()
    if(type == 0):
        return screenRect.width()/tailleStd
    else:
        return screenRect.height()/tailleStd


def creatRect(posX,posY,width,height, ratioWidth, ratioHeight):
    """
    @brief Créer et retourner un objet QRect en fonction des ratios fournis.

    @param posX Position X
    @type posX int

    @param posY Position Y
    @type posY int

    @param width Largeur
    @type width int

    @param height Hauteur
    @type height int

    @param ratioWidth Ratio de modification de la largeur
    @type ratioWidth float

    @param ratioHeight Ratio de modification de la hauteur
    @type ratioHeight float

    @return Objet QRect
    @rtype QtCore.QRec()
    """
    return QtCore.QRect(int(posX * ratioWidth), int(posY * ratioHeight), int(width * ratioWidth), int(height * ratioHeight))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.showFullScreen()
    faulthandler.enable()
    sys.exit(app.exec_())