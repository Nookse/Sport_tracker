# 🏃 Suivi Sportif – Application Python (Tkinter + JSON)

Cette application permet de suivre ses performances sportives sur 5 disciplines (course, muscu, vélo, natation, rando), fixer des objectifs, et visualiser ses progrès via une interface Tkinter. Les données sont stockées localement en JSON.

---

## 📁 Structure du projet

mon_suivi_sport/  
├── main.py # Point d’entrée de l’application  
├── ui/ # Interface utilisateur Tkinter  
│ ├── accueil.py # Page d’accueil (login / sélection de profil)  
│ ├── session.py # Page d’ajout de séances sportives  
│ ├── objectifs.py # Page de définition/suivi des objectifs  
│ └── statistiques.py # Page de visualisation (graphes)  
├── core/ # Logique métier (traitement des données)  
│ ├── gestion_utilisateurs.py # Gestion des profils utilisateurs  
│ ├── gestion_sessions.py # Gestion des séances sportives  
│ ├── gestion_objectifs.py # Suivi des objectifs  
├── data/ # Stockage des données utilisateurs  
│ ├── utilisateurs.json # Profils enregistrés  
│ ├── sessions.json # Historique des séances par utilisateur  
│ └── objectifs.json # Objectifs par utilisateur et par sport  
├── utils.py # Fonctions utilitaires partagées  
└── README.md # Ce fichier  



---

## 🧠 Séparation des responsabilités

### `main.py`
- Initialise l’application Tkinter.
- Gère la navigation entre les différentes pages.
- Appelle les modules de logique et d’interface.

---

### `core/` – Logique métier

Ce dossier ne fait **aucune interface**. Il lit, écrit, modifie les données JSON.

- `gestion_utilisateurs.py` : crée, sélectionne ou supprime des utilisateurs.
- `gestion_sessions.py` : ajoute, lit ou filtre des séances selon le sport et la période.
- `gestion_objectifs.py` : ajoute, modifie et vérifie les objectifs fixés.

---

### `ui/` – Interface utilisateur Tkinter

Chaque fichier correspond à une **page** ou **composant graphique** de l'application.

- `accueil.py` : sélection d’un utilisateur ou création de profil.
- `session.py` : formulaire pour ajouter une séance (sport, durée, distance, notes).
- `objectifs.py` : interface pour fixer et suivre ses objectifs.
- `statistiques.py` : affichage de données avec des graphes (ex : matplotlib).

---

### `data/` – Fichiers de données

Toutes les données sont stockées localement, en JSON.

- `utilisateurs.json` : liste des profils créés.
- `sessions.json` : historique des séances, organisées par utilisateur et sport.
- `objectifs.json` : objectifs définis par sport pour chaque utilisateur.

---

### `utils.py` – Fonctions communes

Contient des fonctions utiles à plusieurs modules :
- Lecture/écriture JSON
- Calculs de date (semaine en cours, mois…)
- Conversions (minutes → heures, etc.)

---

## 📦 Technologies utilisées

- **Python 3**
- **Tkinter** : interface graphique
- **JSON** : stockage simple des données
- **matplotlib** *(optionnel)* : génération de graphes

---

## 🚀 À faire dans l'ordre

1. Créer la structure des dossiers et fichiers.
2. Implémenter `gestion_utilisateurs.py` pour gérer les profils.
3. Ajouter la page `accueil.py` pour choisir ou créer un utilisateur.
4. Implémenter `session.py` et `gestion_sessions.py` pour enregistrer une séance.
5. Ajouter les objectifs (`objectifs.py`) et suivi (`statistiques.py`).

---

## ✍️ Auteur

Projet personnel de suivi sportif avec Python, organisé pour être simple, clair, évolutif, et motivant 💪
