class ActionMenu:

    def show(self):

        print()
        print("🔎 Concept trouvé.")
        print()
        print("Que souhaites-tu faire ?")
        print()
        print("[1] Lire la fiche")
        print("[2] Mettre à jour avec l'IA")
        print("[3] Approfondir le concept")
        print("[4] Comparer avec un autre concept")
        print("[5] Générer des cartes Anki")
        print("[6] Générer un quiz")
        print("[7] Voir les concepts liés")
        print("[8] Ouvrir le Markdown")
        print("[9] Annuler")
        print()

        return input("Choix : ").strip()
