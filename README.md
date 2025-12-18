Générateur de films via IMDb selon l'humeur de l'utilisateur

Ce projet est un outil de recommandation de films développé en Python.
Il utilise le Web Scraping pour interagir avec le site IMDb en temps réel et proposer un film en fonction à l'humeur de l'utilisateur.

Contrairement aux bases de données statiques, ce script interroge les classements actuels d'IMDb, garantissant des recommandations basées sur les tendances récentes.

## Fonctionnalités

* **Sélection par humeur :** L'utilisateur entre son état d'esprit parmi les options  offertes (joyeux, triste, tendu, curieux, énergique).
* **Lien humeur-film :** Chaque humeur est associée à une combinaison intelligente de genres de film.
* **Mode Aléatoire (Neutre) :** Pioche directement dans le "Top 250" mondial d'IMDb.
* **Web Scraping dynamique :** Utilisation de `BeautifulSoup` pour extraire les données HTML en direct.
* **Filtrage intelligent :** Élimination des séries  et des courts-métrages pour se concentrer sur que des films.

## Technologies utilisées

* **Python 3**
* **Requests :** Pour la gestion des requêtes HTTP vers les serveurs d'IMDb.
* **BeautifulSoup4 (bs4) :** Pour la transformation du code HTML et l'extraction des titres.
* **Random :** Pour la sélection aléatoire du film choisi.