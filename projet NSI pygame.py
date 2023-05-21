import pygame
import random
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie = 20
        self.vitesse = 30
        self.img = pygame.image.load("img/kazuha_pix.png")
        self.img = pygame.transform.scale(self.img, (50,80))
        self.rect = self.img.get_rect()
        self.rect.x = 100  # joueur placé aux coordonnées x = 100 dans la fenetre
        self.rect.y =  370 # joueur placé aux coordonnées y = 370 dans la fenetre

    def move_droite(self):
        self.rect.x += self.vitesse # mouvement à droite initialisé
    def move_gauche(self):
        self.rect.x -= self.vitesse # mouvement à gauche initialisé

    def barre_vie(self, dessine):
        barre_color = (111, 210, 46) # couleur initiale de la barre de vie
        barre_position = [self.rect.x, self.rect.y, self.vie, 10] # sa position et sa taille
        pygame.draw.rect(dessine, barre_color, barre_position)


class Projectile(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.img1 = pygame.image.load("img/meteorite.jpg")
        self.img1 = pygame.transform.scale(self.img1, (40,40))
        self.rect = self.img1.get_rect()
        self.gravite = (0, 0.6)
        self.resistance = (0, 0)
        self.rect.x = random.randint(10, 690)
        self.rect.y = -20

    def gravite_jeu(self):
        self.rect.y += self.gravite[1] + self.resistance[1]


largeur = 740
longueur = 494
fenetre = pygame.display.set_mode((largeur, longueur))
# définition des mesures de la fenetre

pygame.display.set_caption("Projet Jeu NSI") # titre
img = pygame.image.load("img/paysage_enneigé_jeu.jpg")

joueur = Player()
continuer = True
# initialisation des météorites
meteore = Projectile()
gamma = Projectile()
sigma = Projectile()
omega = Projectile()
beta = Projectile()
zeta = Projectile()
liste_objet = []
liste_objet.append(meteore)
liste_objet.append(gamma)
liste_objet.append(sigma)
liste_objet.append(omega)
liste_objet.append(beta)
liste_objet.append(zeta)



def Game_over():
    continuer == False
    img2 = pygame.image.load("img/game_over.jpg")
    img2 = pygame.transform.scale(img2, (30,30))
    fenetre.blit(img2, (0,0))

def tomber(objet):
    fenetre.blit(objet.img1, objet.rect)
    objet.gravite_jeu()
    #pygame.display.flip()



while continuer:
    fenetre.blit(img, (0, 0)) # image placée
    joueur.barre_vie(fenetre) # barre de vie initialisée sur le joueur
    fenetre.blit(joueur.img, joueur.rect) # joueur placée
    n = 0
    for m in range(len(liste_objet) - 1):
        if n < 10:
            n = (n + 1) % 10
            tomber(liste_objet[n])
        pygame.display.flip()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.display.flip()
# parametre de la fenetre ouverte

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and joueur.rect.x < 700:
                joueur.move_droite()
                # deplacement droite

            elif event.key == pygame.K_LEFT and joueur.rect.x > 10:

                joueur.move_gauche()
                # deplacement gauche

        if joueur.rect.colliderect(meteore): # collision du meteore avec le personnage
            joueur.vie -= 5
            if joueur.vie < 0:
                Game_over()    # Game over

pygame.quit()


