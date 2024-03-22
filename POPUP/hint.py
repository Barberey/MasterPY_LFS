class Hint:
    """
    @brief La classe Hint représente un indice pour un niveau spécifique.

    @details
    L'indice est obtenu en fonction de la saison et du niveau fournis lors de l'initialisation de l'objet.
    """

    def __init__(self, saison, niveau):
        """
        @brief Initialise une nouvelle instance de la classe Hint.

        @param saison: Le numéro de la saison.
        @type saison: int
        @param niveau: Le numéro du niveau.
        @type niveau: int
        """
        self.saison = saison
        self.niveau = niveau

    def getHint(self):
        """
        @brief Obtient l'indice pour la saison et le niveau spécifiés.

        @return Une chaîne de caractères représentant l'indice.
        @rtype str
        """
        liste_ind = []

        # Lit le fichier contenant les indices en fonction de la saison
        with open(f"../texte/indice/{self.saison}/indice", encoding="utf-8") as hint:
            for lines in hint.readlines():
                tab = lines.split("##")
                chaine = ""
                if len(tab) != 1:
                    chaine += tab[0] + "\n" + tab[1]
                else:
                    chaine = tab[0]
                liste_ind.append(chaine)

        # Retourne l'indice correspondant au niveau spécifié
        return liste_ind[self.niveau - 1]
