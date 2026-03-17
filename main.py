"""Point d'entrée : simulation du robot tondeuse autonome."""

from tondeuse.pelouse import Pelouse
from tondeuse.robot import Robot


def main():
    # Création de la pelouse 10×10
    pelouse = Pelouse(largeur=10, hauteur=10)

    # Quelques obstacles
    for obs in [(3, 3), (3, 4), (4, 3), (7, 7), (7, 8)]:
        pelouse.ajouter_obstacle(*obs)

    # Position de la base (coin supérieur gauche)
    pelouse.definir_base(0, 0)

    # Création du robot à la base
    robot = Robot(pelouse, x_depart=0, y_depart=0)

    print("=== Robot Tondeuse Autonome ===\n")
    print("Pelouse initiale :")
    pelouse.afficher(robot)

    # Lancement de la tonte
    robot.tondre_pelouse()

    print("Pelouse après tonte :")
    pelouse.afficher(robot)
    print(robot)


if __name__ == "__main__":
    main()
