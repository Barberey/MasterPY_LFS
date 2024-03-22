import os
import faulthandler

class SaveHandler:
    """
    @brief La classe SaveHandler gère les sauvegardes de jeu.

    @details
    La classe SaveHandler fournit des fonctionnalités pour gérer les sauvegardes de jeu.
    Elle inclut des méthodes pour récupérer les noms des jeux sauvegardés, créer de nouvelles sauvegardes et sauvegarder la progression du joueur.
    """

    def __init__(self):
        """
        @brief Initialise une nouvelle instance de la classe SaveHandler.

        @details
        Initialise la liste des jeux sauvegardés et récupère les noms de fichiers de sauvegarde existants.
        """
        self.save_file = []

        path = "../save"
        result = next(os.walk(path))
        self.nomSave = result[2]

    def get_saves(self):
        """
        @brief Récupère la liste des noms de jeux sauvegardés.

        @return Liste des noms de jeux sauvegardés.
        @rtype list
        """
        return self.nomSave

    def new_save(self, game_name, player_name):
        """
        @brief Crée une nouvelle sauvegarde de jeu.

        @param game_name: Le nom de la sauvegarde de jeu.
        @type game_name: str

        @param player_name: Le nom du joueur.
        @type player_name: str

        @throws ValueError: Si le nom de jeu existe déjà.
        """
        if game_name in self.nomSave:
            raise ValueError("Mauvais nom")
        else:
            self.save_file.append(game_name)
            fichSave = open(f"../save/{game_name}", "a+")
            fichSave.write(f"{player_name}\n")
            fichSave.write("S1##N::0::0##N::0::0##N::0::0##N::0::0##N::0::0\n")
            fichSave.write("S2##N::0::0##N::0::0##N::0::0##N::0::0##N::0::0\n")
            fichSave.write("S3##N::0::0##N::0::0##N::0::0##N::0::0##N::0::0\n")
            fichSave.write("S4##N::0::0##N::0::0##N::0::0##N::0::0##N::0::0\n")
            fichSave.write("0##False\n")
            fichSave.write("1##False\n")
            fichSave.write("2##False\n")
            fichSave.write("3##False\n")
            fichSave.close()

    def sauvegarde(self, player):
        """
        @brief Sauvegarde la progression du joueur.

        @param player: L'objet joueur contenant les données de progression.
        @type player: player.Player()
        """
        chemin = player.save
        n = "0"
        lignes = []
        for i in range(4):
            lignes.append(
                f"S{i + 1}##{player.niv_complet[i][0]}::{player.etoiles[i][0]}::{n}##{player.niv_complet[i][1]}::{player.etoiles[i][1]}::{n}##{player.niv_complet[i][2]}::{player.etoiles[i][2]}::{n}##{player.niv_complet[i][3]}::{player.etoiles[i][3]}::{n}##{player.niv_complet[i][4]}::{player.etoiles[i][4]}::{n}\n")

        for i in range(len(player.cine)):
            lignes.append(f"{i}##{player.cine[i]}\n")

        with open(chemin, 'w') as fichier:
            fichier.write(f"{player.name}\n")
            for l in lignes:
                fichier.write(l)