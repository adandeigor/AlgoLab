<p align="center">
  <h1 align="center">🧪 AlgoLab</h1>
  <p align="center">
    <strong>Interpréteur pédagogique de pseudo-code en français</strong><br>
    Apprenez l'algorithmique avec une syntaxe naturelle, des erreurs claires et zéro configuration.
  </p>
  <p align="center">
    <a href="https://github.com/adandeigor/AlgoLab/actions"><img src="https://github.com/adandeigor/AlgoLab/actions/workflows/build-release.yml/badge.svg" alt="CI"></a>
    <a href="https://github.com/adandeigor/AlgoLab/blob/main/LICENSE"><img src="https://img.shields.io/github/license/adandeigor/AlgoLab" alt="License: MIT"></a>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-≥3.9-blue" alt="Python 3.9+"></a>
    <a href="https://github.com/adandeigor/AlgoLab/releases"><img src="https://img.shields.io/github/v/release/adandeigor/AlgoLab?include_prereleases" alt="Release"></a>
  </p>
</p>

---

## 🎯 C'est quoi AlgoLab ?

AlgoLab est un **interpréteur de pseudo-code en français**, conçu pour les étudiants et enseignants en algorithmique. Il permet d'écrire et exécuter du pseudo-code tel qu'il est enseigné en cours — sans avoir besoin d'apprendre Python, C ou Java d'abord.

```
Variable nom : Caractere
Variable age : Entier

Debut
  Ecrire "Comment tu t'appelles ?"
  Lire(nom)
  Ecrire "Quel âge as-tu ?"
  Lire(age)

  Si age >= 18 Alors
    Ecrire "Bienvenue ", nom, " ! Tu es majeur."
  Sinon
    Ecrire "Salut ", nom, " ! Tu as encore ", 18 - age, " ans à attendre."
  FinSi
Fin
```

### Pourquoi AlgoLab ?

- 🇫🇷 **Syntaxe 100% française** — `Variable`, `Si...Alors...Sinon`, `Pour...De...A`, `TantQue`, `Ecrire`, `Lire`
- 📚 **Messages d'erreurs pédagogiques** — pas de stack traces cryptiques, des explications claires
- ⚡ **Zéro config** — un binaire, ça marche. Pas besoin d'installer Python
- 🧩 **Extension VS Code** — coloration syntaxique, snippets, exécution intégrée
- 🖥️ **Multi-plateforme** — Linux (.deb), Windows (.exe), macOS

---

## 🚀 Installation

### Option 1 : Binaires pré-compilés (recommandé pour les étudiants)

Téléchargez le binaire pour votre OS depuis les [Releases GitHub](https://github.com/adandeigor/AlgoLab/releases) :

| OS | Fichier |
|---|---|
| Linux | `algolab-linux.deb` |
| Windows | `algolab-windows.exe` |
| macOS | `algolab-macos` |

### Option 2 : Avec pip (pour les développeurs)

```bash
pip install git+https://github.com/adandeigor/AlgoLab.git
```

Ou en clonant le repo :

```bash
git clone https://github.com/adandeigor/AlgoLab.git
cd AlgoLab
pip install .
```

### Option 3 : Extension VS Code

Téléchargez `algolab-vscode.vsix` depuis les [Releases](https://github.com/adandeigor/AlgoLab/releases), puis dans VS Code :

```
Ctrl+Shift+P → "Extensions: Install from VSIX..."
```

---

## 📖 Syntaxe rapide

### Variables et types

```
Variable x : Entier
Variable nom : Caractere
Variable pi : Reel
Variable ok : Booleen
Variable notes : Entier[10]
```

Types supportés : `Entier`, `Reel`, `Caractere`, `Chaine`, `Booleen`, tableaux avec `[taille]`.

### Structures de contrôle

```
Si condition Alors
  ...
SinonSi autre_condition Alors
  ...
Sinon
  ...
FinSi

Pour i De 1 A 10 Pas 2 Faire
  ...
FinPour

TantQue condition Faire
  ...
FinTantQue
```

### Fonctions

```
Fonction Carre(n : Entier) : Entier
  Retourner n * n
FinFonction
```

### Entrées / Sorties

```
Lire(variable)
Ecrire "Résultat = ", variable
```

> 📁 Plus d'exemples dans le dossier [`examples/`](./examples/)

---

## 🛠️ Développement

### Pré-requis

- Python ≥ 3.9
- pip

### Setup

```bash
git clone https://github.com/adandeigor/AlgoLab.git
cd AlgoLab
pip install -e ".[dev]"
```

### Lancer les tests

```bash
pytest --cov=src/algolab --cov-report=term-missing
```

### Linter

```bash
ruff check src/algolab
```

### Exécuter un fichier .algo

```bash
algolab examples/hello_world.algo
algolab -c 'Variable x : Entier Debut x <- 42 Ecrire x Fin'
```

---

## 🏗️ Architecture

```
src/algolab/
├── grammar.lark      # Grammaire Lark (source de vérité syntaxique)
├── parser.py         # Parsing → arbre Lark
├── interpreter.py    # Exécution de l'arbre
├── environment.py    # Gestion mémoire et variables
├── errors.py         # Erreurs pédagogiques
└── main.py           # Point d'entrée CLI
```

Documentation technique complète dans [`docs/`](./docs/).

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Que vous soyez débutant ou expérimenté, il y a plein de façons d'aider :

- 🐛 Signaler un bug
- 💡 Proposer une fonctionnalité
- 📝 Améliorer la documentation
- 🧪 Ajouter des tests
- 🌍 Traduire (README en anglais, etc.)

👉 Lisez le [Guide de contribution](./CONTRIBUTING.md) pour démarrer.

Cherchez les issues avec le label [`good first issue`](https://github.com/adandeigor/AlgoLab/labels/good%20first%20issue) pour un premier pas facile !

---

## 📜 Licence

AlgoLab est distribué sous licence [MIT](./LICENSE). Libre d'utilisation, modification et redistribution.

---

## 🙏 Remerciements

AlgoLab est né d'un constat : les étudiants en algorithmique écrivent du pseudo-code en cours mais ne peuvent pas l'exécuter. Ce projet vise à combler ce fossé.

Construit avec ❤️ depuis Cotonou, Bénin 🇧🇯

---

<p align="center">
  <strong>⭐ Si AlgoLab vous aide, laissez une étoile sur GitHub !</strong><br><br>
  <em>— The Pirate Dev 🏴‍☠️</em>
</p>
