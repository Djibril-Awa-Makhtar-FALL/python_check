# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:05:18 2024

@author: Djibril Awa Makhtar FALL
"""

## 1) Créez une liste nommée « shopping_list » pour stocker les articles.

shopping_list = [ ]

""" 2) Utilisez une boucle while pour créer un menu d’options 
permettant à l’utilisateur d’ajouter, de supprimer ou d’afficher
 des éléments de la liste."""
 
while True :
    print("\n options:")
    print("1. ajouter un article de la liste")
    print("2. supprimer un article de la liste")
    print("3. afficher les éléments de la liste")

""" 3) Utilisez la fonction input() pour inviter l'utilisateur à faire 
une sélection dans le menu."""

input('faire une sélection dans le menu.')

"""4) Utilisez un bloc if-elif-else pour déterminer la sélection de
 l'utilisateur et effectuer l'action correspondante."""

choice = input("Sélection de l'utilisateur")

if choice == "1" :

    item = input("Entrée le nom de l'article à ajouter")
    
    shopping_list.append(item)

    print(f"'{item}' a été ajouté à la liste")

elif choice == "2" :
    
    item = input("Entrée le nom de l'article à supprimer")
    
if item in shopping_list :
    
    shopping_list.remove(item)
    
    print(f"'{item}' a été supprimer de la liste")
    
else : print(f"'{item}' n'est pas dans la liste.")

elif choice == "3" : 
    
if shopping_list:
    
    item = input("Afficher les éléments de la liste")

#### je ne comprends pas le reste du code Coach


""" 5) Si l'utilisateur sélectionne « ajouter », utilisez la fonction input()
 pour l'inviter à saisir un élément à ajouter à la liste. 
 Utilisez la fonction range() pour limiter le nombre d'éléments 
 pouvant être ajoutés à la liste."""
 
## Définissons le nombre d'éléments par exemple à 8

 nombre_d\'éléments = 8
 
action = input("Saisir un élément à ajouter à la liste.")

for i in range(nombre_d\'éléments):
               élément = input(f"saisissez l'élémnt {i+1}" :)
               shopping_list.append(élément)

                break

""" 6) Si l'utilisateur sélectionne « supprimer », utilisez la fonction input()
 pour l'inviter à saisir un élément à supprimer de la liste."""
 
élément_à_supprimer = input("Saisiser l'élément à supprimer :")

## Vérifions d'abord si l'élément est dans la liste:

if élément_à_supprimer in shopping_list :

    shopping_list.remove(élément_à_supprimer)
print(f"l'élément '{élément_à_supprimer}' a été supprimé.")

else : 
    
    print(f"L'élément '{élément_à_supprimer}' n'est pas dans la liste.")

""" 7) Si l'utilisateur sélectionne « Afficher », utilisez une boucle for pour parcourir
 la liste des éléments et les afficher à l'utilisateur."""
 
 if action == "afficher" :
     
     print("Voici les éléments dans la liste.")
 
for élément in shopping_list :
    
    print(f"'{élément}'")
    
""" 8) Utilisez les structures de données de liste, de tuple, 
d'ensemble et de dictionnaire pour stocker et manipuler les articles d'achat."""

## Je pense que c'est déjà fait ultérieurement si j'ai bien compris!



    
    
 



