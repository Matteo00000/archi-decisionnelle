# Entrepôt de Données Coder/coder

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

Ce projet collecte et analyse les données du projet Coder/coder depuis GitHub.

## Table des Matières
1. [Structure du Projet](#structure-du-projet)
2. [Fonctionnalités](#fonctionnalités)
3. [Sources de Données](#sources-de-données)
4. [Schéma de la Base de Données](#schéma-de-la-base-de-données)
5. [Dépendances](#dépendances)
6. [Licence](#licence)
7. [Dépannage](#dépannage)

## Structure du Projet

```
archi/
├── data/                   # Contient les données collectées au format parquet
├── scripts/                # Scripts de collecte et traitement des données
│   ├── fetch_branches.py
│   ├── fetch_contributors.py
│   ├── fetch_forks.py
│   ├── fetch_issues.py
│   ├── fetch_labels.py
│   ├── fetch_tags.py
│   ├── load_to_duckdb.py   # Script Python pour charger les données dans DuckDB

└── README.md
```

## Fonctionnalités

Le projet permet de :
- Collecter les données GitHub du projet Coder/coder
- Stocker les données dans des fichiers Parquet
- Charger les données dans une base DuckDB
- Analyser les données via SQL
- Gérer les limites de taux d'API GitHub
- Mettre en cache les résultats pour éviter les collectes répétées


### Pré-requis
- Python 3.8 ou supérieur
- Compte GitHub avec token d'accès

## Sources de Données

Les données suivantes sont collectées :
- Issues (tickets)
- Tags (tags)
- Contributeurs
- Labels (étiquettes)
- Forks (copie indépendante)
- Branches (branches Git)

## Schéma de la Base de Données

La base contient les tables suivantes :
- raw_issues : Données brutes des issues
- raw_tags : Données brutes des tags
- raw_contributors : Données brutes des contributeurs
- raw_labels : Données brutes des labels
- raw_forks : Données brutes des forks
- raw_branches : Données brutes des branches

Chaque table contient les données brutes du fichier parquet correspondant.


## Dépendances

- Python 3.8+
- Bibliothèques Python :
  - requests
  - pandas
  - duckdb
  - python-dotenv
  - tqdm

## Licence

Distribué sous licence MIT. Voir `LICENSE` pour plus d'informations.

## Dépannage

### Problèmes courants

1. **Erreur 401 - Non autorisé**
   - Vérifiez que votre token GitHub est valide
   - Assurez-vous que le fichier `.env` est correctement configuré

2. **Limite de taux API atteinte**
   - Le système gère automatiquement les limites
   - Vous pouvez augmenter le délai entre les requêtes dans `scripts/run_all.py`

3. **Erreurs de dépendances**
   - Vérifiez que vous utilisez Python 3.8+
   - Réinstallez les dépendances : `pip install -r requirements.txt`
