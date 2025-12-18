import requests
from bs4 import BeautifulSoup
import random

# faire correspondre les humeurs à des genres de films
humeurs = {
    "joyeux": ["comedy", "musical", "family"],
    "triste": ["drama", "romance"],
    "excité": ["action", "adventure"],
    "curieux": ["documentary", "history"],
    "énergique": ["action", "adventure", "sci-fi"],
    "tendu": ["horror", "mystery", "thriller"] }

print("Générateur de film selon l'humeur")
print("Quelle est votre humeur actuelle ?")
print("Options: joyeux, triste, excité, curieux, énergique, tendu")

# variable d'humeur de l'utilisateur
choix_humeur = input("Entrez votre humeur: ").lower().strip()

# Vérifier si l'humeur est valide
if choix_humeur not in humeurs:
    print("Humeur non reconnue. Veuillez choisir parmi les options fournies.")
    exit()

# logique de sélection de l'URL en fonction de l'humeur
url = ""

if choix_humeur == "joyeux":
    url = "https://www.imdb.com/search/title/?genres=comedy,musical,family&title_type=movie"

elif choix_humeur == "triste":
    url = "https://www.imdb.com/search/title/?genres=drama,romance&title_type=movie"

elif choix_humeur == "excité":
    url = "https://www.imdb.com/search/title/?genres=action,adventure&title_type=movie"

elif choix_humeur == "curieux":
    url = "https://www.imdb.com/search/title/?genres=documentary,history&title_type=movie"

elif choix_humeur == "énergique":
    url = "https://www.imdb.com/search/title/?genres=sci-fi,action,adventure&title_type=movie"

elif choix_humeur == "tendu":
    url = "https://www.imdb.com/search/title/?genres=horror,mystery,thriller&title_type=movie"

# on choisit un film au hasard dans le top 250 si l'humeur est neutre
elif choix_humeur == "neutre":
    url = "https://www.imdb.com/chart/top/"

# récupération des données
print("Recherche de film en cours pour l'humeur: {choix_humeur}...")

# masque pour éviter d'être bloqué, car IMDb bloque les requêtes sans user-agent
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}


try: 
    # envoi de la requête
    reponse = requests.get(url, headers=headers)

    # vérifier si la requête a réussi (code 200 = ok)
    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.content, "html.parser")

        # extraction des titres des films
        films_trouves = soup.find_all('h3', class_='ipc-title__text')

        # la liste "propre" (retirer les titres vides)
        liste_titres = [f.get_text() for f in films_trouves if f.get_text()]

        # le choix final
        if liste_titres:
            film_choisi = random.choice(liste_titres)
            print("\n" + "="*40)
            print(f"Le film recommandé pour vous aujourd'hui est : {film_choisi}")
            print("="*40 + "\n")
        else:
            print("Erreur : Aucun film trouvé dans la liste disponible actuellement.")
    else: 
        print("Erreur de connexion au site IMDb (Code : {reponse.status_code})")

except Exception as e:
    print("Une erreur technique est survenue : {e}")