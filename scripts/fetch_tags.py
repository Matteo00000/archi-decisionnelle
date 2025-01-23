import requests
import pandas as pd
from pathlib import Path
import os

# Variables globales
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = 'coder'  # Remplace par le propriétaire du dépôt
REPO_NAME = 'coder'   # Remplace par le nom du dépôt
DATA_DIR = Path('data')

def fetch_tags():
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/tags'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lève une exception si le statut HTTP n'est pas 200
        
        tags = response.json()  # Parse la réponse JSON
        df = pd.DataFrame(tags)  # Convertit en DataFrame
        
        # Crée le répertoire "data" s'il n'existe pas
        DATA_DIR.mkdir(exist_ok=True)
        
        # Sauvegarde les données dans un fichier Parquet
        df.to_parquet(DATA_DIR / 'tags.parquet')
        print(f"Saved {len(df)} tags to {DATA_DIR / 'tags.parquet'}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tags: {e}")

if __name__ == "__main__":
    fetch_tags()
