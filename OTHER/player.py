# -*- coding: utf-8 -*-

"""
@file player.py
@brief Fichier decrivant la classe Player qui permet de stocker les informations du joueur
"""

class Player:
    """
    @brief Classe qui gère les informations d'un joueur.
    """

    def __init__(self, saveFile):
        """
        @brief Constructeur de la classe Player.

        @param saveFile: Le chemin du fichier de sauvegarde.
        @type saveFile: str
        """
        self.save = saveFile
        self.name = self.recupNom()
        self.nb_etoile = self.recupStars()
        self.etoiles = self.generInfo(1)
        self.niv_complet = self.generInfo(0)
        self.cine = self.recupInfoCine()

    def generInfo(self, posInf):
        """
        @brief Génère les informations sur les étoiles ou les niveaux complétés.

        @param posInf: Position de l'information à générer (0 pour niveaux complétés, 1 pour étoiles).
        @type posInf: int

        @return: Liste d'informations générées pour chaque saison.
        @rtype: list
        """
        etoiles = []
        for i in range(4):
            match i:
                case 0:
                    etoiles.append(self.info_nivs("S1", posInf))
                case 1:
                    etoiles.append(self.info_nivs("S2", posInf))
                case 2:
                    etoiles.append(self.info_nivs("S3", posInf))
                case 3:
                    etoiles.append(self.info_nivs("S4", posInf))

        return etoiles

    def info_nivs(self, code, pos):
        """
        @brief Récupère les informations d'un niveau spécifique.

        @param code: Le code de la saison.
        @type code: str
        @param pos: Position de l'information à récupérer (0 pour niveaux complétés, 1 pour étoiles).
        @type pos: int

        @return: Liste d'informations récupérées pour chaque niveau de la saison.
        @rtype: list
        """
        etoiles = []
        with open(self.save, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                if (ligne[0] + ligne[1] == code):
                    nivs = ligne.split("##")
                    for i in range(1, 6):
                        lvl = nivs[i].split("::")
                        etoiles.append(lvl[pos][0])
        return etoiles

    def recupStars(self):
        """
        @brief Récupère le nombre total d'étoiles du joueur.

        @return: Le nombre total d'étoiles.
        @rtype: int
        """
        with open(self.save, 'r') as fichier:
            lignes = fichier.readlines()
            nbEtoile = 0
            for ligne in lignes:
                if (ligne[0] == "S"):
                    nivs = ligne.split("##")
                    for i in range(1, 6):
                        lvl = nivs[i].split("::")
                        nbEtoile += int(lvl[1])

        return nbEtoile

    def recupNom(self):
        """
        @brief Récupère le nom du joueur à partir du fichier de sauvegarde.

        @return: Le nom du joueur.
        @rtype: str
        """
        with open(self.save, 'r') as fichier:
            nom = fichier.readline().strip()

        return nom

    def updateStars(self, saison, niveau, etoile):
        """
        @brief Met à jour les informations sur les étoiles obtenues dans un niveau spécifique.

        @param saison: Le numéro de la saison.
        @type saison: int
        @param niveau: Le numéro du niveau.
        @type niveau: int
        @param etoile: Le nombre d'étoiles obtenu dans le niveau.
        @type etoile: int
        """
        etoile_niv = self.etoiles[saison - 1][niveau - 1]
        if (etoile > int(etoile_niv)):
            self.etoiles[saison - 1][niveau - 1] = str(etoile)
            self.nb_etoile += etoile - int(etoile_niv)

    def valide(self, saison, niveau):
        """
        @brief Marque un niveau comme validé.

        @param saison: Le numéro de la saison.
        @type saison: int
        @param niveau: Le numéro du niveau.
        @type niveau: int
        """
        self.niv_complet[saison - 1][niveau - 1] = "Y"

    def is_valide(self, saison):
        """
        @brief Vérifie si tous les niveaux d'une saison sont validés.

        @param saison: Le numéro de la saison.
        @type saison: int

        @return: True si tous les niveaux sont validés, False sinon.
        @rtype: bool
        """
        for i in self.niv_complet[saison - 1]:
            if (i != "Y"):
                return False

        return True

    def recupInfoCine(self):
        """
        @brief Recuperation des informations permettant de savoir si le joueur a deja vu les differents dialogues de l'histoire

        @return: Liste des informations concernant les dialogues de l'histoire
        @rtype: list
        """
        infoCine = []
        with open(self.save, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                tab = ligne.strip().split("##")
                if(len(tab) == 2):
                    if(tab[1] == "False"):
                        infoCine.append(False)
                    if(tab[1] == "True"):
                        infoCine.append(True)

        return infoCine

    def modifCine(self, num):
        """
        @brief Modification lors de la realisation des dialogues de l'histoire

        @param num: Numéro du dialogue de l'histoire
        @type num: int
        """
        if(not self.cine[num]):
            self.cine[num] = True