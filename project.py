import random

def main():
    while True:
        print("""
                1. Je veux apprendre une table de multiplication
                2. Je veux m'entrainer sur une table de multiplication
                3. Je veux tester mes connaissances
                4. Quitter""")
        choix = input("votre choix : ")
    # Gestion des choix de l'utilisateur

        # si l'utilisateur veut apprendre une table
        if choix == "1":
                    table = choisir_table()
                    apprendre_table(table)
                
        # si l'utilisateur veut s'entrainer sur une table avec un nombre aléatoire
        elif choix == "2":
            table = choisir_table()
            entrainer_table(table)

        # si l'utilisateur veut tester ses connaissances sur toutes les tables
        elif choix == "3":
            tester_connaissances()

        # si l'utilisateur veut quitter le programme
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


# Fonction pour obtenir un nombre valide de l'utilisateur
def obtenir_nombre_valide(message):
        # Boucle jusqu'à ce que l'utilisateur entre un nombre valide
    while True:
            # Essayer de convertir l'entrée en entier
        try:
            nombre = int(input(message))
            return nombre
            # Gérer l'exception si l'entrée n'est pas un entier
        except ValueError:
            print("Entrée invalide, veuillez entrer un nombre valide.")


# Fonction pour vérifier la réponse de l'utilisateur
def verifier_reponse(table, i, reponse):
    return reponse == table * i

# Fonction pour vérifier si la table choisie est valide
def table_valide(table):
    return 1 <= table <= 10

# fontion pour obliger l'utilisateur à choisir une table entre 1 et 10
def choisir_table():
    while True:
        table = obtenir_nombre_valide("Quelle table voulez-vous (entre 1 et 10) ? ")
        if table_valide(table):
            return table
        else:
            print("Veuillez choisir une table entre 1 et 10.")

# Fonction pour afficher le score final            
def score_final(score, table):
        # Si le score est parfait
    if score == 10:
        return f"Félicitations ! Vous avez parfaitement appris la table de {table} !"  
    # Si le score est entre 8 et 9 
    elif score >= 8:
        return f"Avec un score de {score}/10, vous n'êtes pas loin de bien connaitre la table de {table} ! Continuez comme ça !"
    # Si le score est inférieur à 8
    else:
        return f"Avec un score de {score}/10, il faut encore travailler la table de {table}. Ne vous découragez pas !"
        

# Fonction pour apprendre une table de multiplication
def apprendre_table(table):
    # Affichage de la table de multiplication
    print(f"Apprentissage de la table de multiplication de {table}:")
    # Initialisation du score
    score = 0
    # Boucle pour chaque multiplication de 1 à 10
    for i in range(1, 11):
        # Demande de la réponse à l'utilisateur
        reponse = obtenir_nombre_valide((f"{table} x {i} = "))
        # Vérification de la réponse 
        # Si la réponse est correcte
        if verifier_reponse(table, i, reponse):
            print("Super!")
            # on augmente le score
            score += 1
        # Si la réponse est incorrecte
        else:
            print(f"Mince. La bonne réponse est {table * i}.")
    # Affichage du score final        
    print(score_final(score, table))    


# Fonction pour s'entrainer sur une table de multiplication    
def entrainer_table(table): 
    # Affichage de la table de multiplication
    print(f"Entraînement sur la table de multiplication de {table}:")
    # Initialisation du score
    score = 0
    # Boucle pour 10 questions aléatoires
    for _ in range(10):
        # Génération d'un nombre aléatoire entre 1 et 10
        i = random.randint(1, 10)
        # Demande de la réponse à l'utilisateur
        reponse = obtenir_nombre_valide((f"{table} x {i} = "))
        # Vérification de la réponse 
        # Si la réponse est correcte
        if verifier_reponse(table, i, reponse):
            print("Super!")
            # on augmente le score
            score += 1
        # Si la réponse est incorrecte
        else:
            print(f"Mince. La bonne réponse est {table * i}.")
            
    print(score_final(score, table)) 


# Fonction pour tester les connaissances sur toutes les tables de multiplication
def tester_connaissances():
        # Affichage du message de test
    print("Test de connaissances sur toutes les tables de multiplication:")
        # Initialisation du score
    score = 0
        # Boucle pour 10 questions aléatoires
    for _ in range(10):
         # Génération de deux nombres aléatoires entre 1 et 10
        table = random.randint(1, 10)
            # Génération d'un autre nombre aléatoire entre 1 et 10
        i = random.randint(1, 10)
            # Demande de la réponse à l'utilisateur
        reponse = obtenir_nombre_valide((f"{table} x {i} = "))
            # Vérification de la réponse
        # Si la réponse est correcte
        if verifier_reponse(table, i, reponse):
            print("Super!")
            # on augmente le score
            score += 1
        # Si la réponse est incorrecte
        else:
            print(f"Mince. La bonne réponse est {table * i}.")
        # Affichage du score final        
    print(f"Votre score final est {score}/10.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()