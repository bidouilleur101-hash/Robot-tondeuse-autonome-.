"""Tests unitaires pour le robot tondeuse autonome."""

import unittest
from tondeuse.pelouse import Pelouse
from tondeuse.robot import Robot, Direction


class TestPelouse(unittest.TestCase):

    def setUp(self):
        self.pelouse = Pelouse(largeur=5, hauteur=5)

    def test_dimensions(self):
        self.assertEqual(self.pelouse.largeur, 5)
        self.assertEqual(self.pelouse.hauteur, 5)

    def test_tondre(self):
        self.pelouse.tondre(2, 2)
        self.assertTrue(self.pelouse.est_tonte(2, 2))

    def test_obstacle(self):
        self.pelouse.ajouter_obstacle(1, 1)
        self.assertFalse(self.pelouse.peut_avancer(1, 1))

    def test_hors_grille(self):
        self.assertFalse(self.pelouse.peut_avancer(-1, 0))
        self.assertFalse(self.pelouse.peut_avancer(0, 5))

    def test_pourcentage_tonte_initial(self):
        self.assertEqual(self.pelouse.pourcentage_tonte, 0.0)

    def test_pourcentage_tonte_apres_tonte(self):
        for y in range(5):
            for x in range(5):
                self.pelouse.tondre(x, y)
        self.assertEqual(self.pelouse.pourcentage_tonte, 100.0)


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.pelouse = Pelouse(largeur=5, hauteur=5)
        self.robot = Robot(self.pelouse, x_depart=0, y_depart=0)

    def test_position_initiale(self):
        self.assertEqual(self.robot.position, (0, 0))

    def test_direction_initiale(self):
        self.assertEqual(self.robot.direction, Direction.EST)

    def test_tourner_droite(self):
        self.robot.direction = Direction.NORD
        self.robot.tourner_droite()
        self.assertEqual(self.robot.direction, Direction.EST)

    def test_tourner_gauche(self):
        self.robot.direction = Direction.NORD
        self.robot.tourner_gauche()
        self.assertEqual(self.robot.direction, Direction.OUEST)

    def test_avancer(self):
        self.robot.direction = Direction.EST
        resultat = self.robot.avancer()
        self.assertTrue(resultat)
        self.assertEqual(self.robot.position, (1, 0))

    def test_avancer_hors_limites(self):
        self.robot.direction = Direction.OUEST
        resultat = self.robot.avancer()
        self.assertFalse(resultat)
        self.assertEqual(self.robot.position, (0, 0))

    def test_avancer_sur_obstacle(self):
        self.pelouse.ajouter_obstacle(1, 0)
        self.robot.direction = Direction.EST
        resultat = self.robot.avancer()
        self.assertFalse(resultat)
        self.assertEqual(self.robot.position, (0, 0))

    def test_batterie_diminue(self):
        batterie_initiale = self.robot.batterie
        self.robot.avancer()
        self.assertEqual(self.robot.batterie, batterie_initiale - 1)

    def test_tonte_pelouse(self):
        robot = Robot(self.pelouse, x_depart=0, y_depart=0)
        robot.tondre_pelouse()
        self.assertTrue(self.pelouse.est_tonte(0, 0))
        self.assertGreater(self.pelouse.pourcentage_tonte, 0.0)


if __name__ == "__main__":
    unittest.main()
