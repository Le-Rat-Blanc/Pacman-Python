# Importe les fonctions spécifiques du jeu.
import jeu 

def main():
    rejouer=True
    while rejouer:
        rejouer=False
        ''' Fonction principale. '''
        # Initialise le jeu en stockant les parametres dans un dictionnaire
        jeu_att = jeu.init()

        # Exécute la boucle principale du jeu.
        jeu.boucle(jeu_att)
        
        if jeu_att["rejouer"]:
            rejouer=True

 
     
     # Termine le jeu.
    jeu.quitte()

# Appelle la fonction principale.
if __name__ == '__main__':
    main()

