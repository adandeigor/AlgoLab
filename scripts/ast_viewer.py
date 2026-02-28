#!/usr/bin/env python3
"""
Script pour générer l'AST d'un fichier AlgoLab.

Ce script affiche l'arbre syntaxique abstrait (AST) généré par Lark
dans la console avec un affichage textuel arborescent (en utilisant `.pretty()`),
ce qui est idéal pour comprendre la structure du code.

Usage:
  python ast_viewer.py <fichier.algo>
"""

import sys
import os

# Ajouter le dossier src au path pour pouvoir importer algolab
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algolab.parser import parse_source

def main():
    if len(sys.argv) < 2:
        print("Usage: python ast_viewer.py <fichier.algo>")
        print("Ou lancez sans argument pour un exemple intégré.")
        
        # Code d'exemple si aucun fichier n'est fourni
        source_code = """
        VARIABLE x : ENTIER
        VARIABLE y : REEL
        
        DEBUT
            x <- 10
            y <- 3.14
            SI x > 5 ALORS
                ECRIRE "x est grand"
            FIN_SI
        FIN
        """
        print("\n--- Exemple de génération AST sur le code suivant ---")
        print(source_code)
    else:
        filepath = sys.argv[1]
        if not os.path.isfile(filepath):
            print(f"Erreur: Le fichier {filepath} n'existe pas.")
            sys.exit(1)
            
        with open(filepath, 'r', encoding='utf-8') as f:
            source_code = f.read()
            print(f"--- Fichier: {filepath} ---")

    try:
        # Analyse du code et génération de l'AST
        ast = parse_source(source_code)
        
        # Lark offre la méthode .pretty() qui dessine l'arbre
        print("\n--- Arbre Syntaxique Abstrait ---")
        print(ast.pretty())
        
    except Exception as e:
        print(f"Erreur d'analyse: {e}")

if __name__ == "__main__":
    main()
