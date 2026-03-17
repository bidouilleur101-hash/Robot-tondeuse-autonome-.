# Robot Tondeuse Autonome

Simulation en Python d'un robot tondeuse autonome se déplaçant sur une pelouse en grille, évitant les obstacles et maximisant la surface tondue.

## Structure du projet

```
.
├── main.py                  # Point d'entrée de la simulation
├── tondeuse/
│   ├── __init__.py
│   ├── config.py            # Paramètres de configuration
│   ├── pelouse.py           # Grille représentant la pelouse
│   └── robot.py             # Logique du robot (mouvement, navigation)
└── tests/
    └── test_tondeuse.py     # Tests unitaires
```

## Fonctionnalités

- Pelouse de taille configurable (par défaut 10 × 10)
- Placement d'obstacles sur la grille
- Robot autonome avec stratégie de balayage en zigzag
- Gestion de la batterie (nombre de mouvements limité)
- Affichage de la pelouse dans le terminal après chaque simulation
- Calcul du pourcentage de surface tondue

## Lancer la simulation

```bash
python main.py
```

## Lancer les tests

```bash
python -m unittest discover -s tests -v
```

## Symboles d'affichage

| Symbole | Signification        |
|---------|----------------------|
| `T`     | Robot tondeuse       |
| `.`     | Zone tondue          |
| `#`     | Zone non tondue      |
| `X`     | Obstacle             |
| `B`     | Base de rechargement |

## Configuration

Les paramètres par défaut se trouvent dans `tondeuse/config.py` :

| Paramètre          | Valeur par défaut | Description                        |
|--------------------|-------------------|------------------------------------|
| `LARGEUR_PELOUSE`  | 10                | Largeur de la grille               |
| `HAUTEUR_PELOUSE`  | 10                | Hauteur de la grille               |
| `AUTONOMIE_BATTERIE` | 100             | Nombre maximum de mouvements       |

