# Projet Python
=================
## Lancement du projet 
Placer vous dans un venv actif :
 * pip install -r requirements.txt
 * export FLASK_ENV=development
 * lancement partie 1 : python3 sharecode.py
 * lancement partie 2 : python3 sharecodedb.py

## Partie 1 : Possibilité de choisir le langage de programmation

**Ajout de 2 fonctions permettant de lire et créer un nouveau type de fichier dédié uniquement au langage :**

* save_language_as_file qui retourne l'uid
* read_language_as_file qui retourne le language associé à l'uid

**Coté utilisateur :**

* Ajout d'un menu déroulant qui affiche plusieurs langage de programmation selon le code que l'on vas écrire
* Affichage du code et du langage dans l'index ainsi que dans la view

## Partie 2 : Gestion des données dans un SGBDR

**Ajout de 3 nouveaux fichiers :**

 1. model_sqlite.py = création nouveau model et réecriture de toutes les fonctions nécessaire pour le fonctionnement avec sqlite
 2. shareCodedb.py = gestion des routes et utilisation des fonctions du model_sqlite.py
 3. shareCodeBdd.db = base de données Sqlite

## Partie 3 : Enegistrement des informations utilisateur qui publient le code

 * Ajout de fonctions pour la connexion à la table user
 * Ajout du template admin.html
 (Je n'ai pas eu le temps de terminer la partie 3, donc je n'ai pas merge ma branche avec le reste de mon code, la partie 3 se trouve sur la branch develop3 qui pars de la master)
