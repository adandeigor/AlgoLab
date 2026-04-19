# 🤝 Guide de contribution — AlgoLab

Merci de vouloir contribuer à AlgoLab ! Ce guide vous explique comment participer au projet, que vous soyez débutant ou développeur expérimenté.

## 📋 Table des matières

- [Code de conduite](#-code-de-conduite)
- [Comment contribuer](#-comment-contribuer)
- [Premiers pas](#-premiers-pas)
- [Workflow Git](#-workflow-git)
- [Standards de code](#-standards-de-code)
- [Soumettre une Pull Request](#-soumettre-une-pull-request)
- [Signaler un bug](#-signaler-un-bug)
- [Proposer une fonctionnalité](#-proposer-une-fonctionnalité)

---

## 📜 Code de conduite

En participant à ce projet, vous acceptez de respecter notre [Code de conduite](./CODE_OF_CONDUCT.md). Soyez bienveillant, respectueux et constructif.

---

## 🎯 Comment contribuer

Il y a de nombreuses façons de contribuer, même sans écrire de code :

| Type | Exemples |
|---|---|
| 🐛 **Bugs** | Signaler un problème, reproduire un bug existant |
| 📝 **Documentation** | Corriger une typo, améliorer un guide, ajouter des exemples `.algo` |
| 🧪 **Tests** | Ajouter des tests unitaires, des cas limites |
| 💡 **Fonctionnalités** | Proposer et implémenter de nouvelles features |
| 🌍 **Traduction** | Traduire le README ou la doc en anglais |
| 🎨 **Extension VS Code** | Améliorer les snippets, la coloration syntaxique |

> 💡 **Nouveau sur l'open source ?** Cherchez les issues avec le label [`good first issue`](https://github.com/adandeigor/AlgoLab/labels/good%20first%20issue) — elles sont conçues pour être abordables.

---

## 🤖 Contributions générées par des agents IA

Les contributions produites avec l'aide d'agents IA (GitHub Copilot, 
Claude Code, rawcell, ou tout autre outil autonome) sont les bienvenues 
dans AlgoLab, sous une condition non négociable :

**Un humain doit avoir relu, compris et testé le code avant de soumettre 
la PR.**

Concrètement :
- La description de la PR doit mentionner explicitement l'outil utilisé.
- Le contributeur humain est responsable du code soumis, qu'il l'ait 
  écrit lui-même ou qu'un agent l'ait généré.
- Toute PR soumise directement par un agent sans validation humaine 
  explicite sera fermée sans review. Le contributeur humain pourra la 
  réouvrir après relecture.

Ce n'est pas un rejet des outils IA — c'est une exigence de 
responsabilité. Le code qui entre dans `main` doit être compris et 
assumé par quelqu'un.

---

## 🏁 Premiers pas

### 1. Fork et clone

```bash
# Fork le repo sur GitHub, puis :
git clone https://github.com/<votre-username>/AlgoLab.git
cd AlgoLab
```

### 2. Installer l'environnement de développement

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install -e ".[dev]"
```

### 3. Vérifier que tout fonctionne

```bash
# Lancer les tests
pytest --cov=src/algolab --cov-report=term-missing

# Vérifier le linting
ruff check src/algolab

# Tester manuellement
algolab examples/hello_world.algo
```

---

## 🔀 Workflow Git

### Convention de branches

```
main                  # Branche stable
├── feature/xxx       # Nouvelle fonctionnalité
├── fix/xxx           # Correction de bug
├── docs/xxx          # Documentation
└── test/xxx          # Ajout de tests
```

### Workflow

```bash
# 1. Créer une branche depuis main
git checkout main
git pull origin main
git checkout -b feature/ma-fonctionnalite

# 2. Travailler, commiter
git add .
git commit -m "feat: ajouter le support des procédures"

# 3. Pousser et créer une PR
git push origin feature/ma-fonctionnalite
```

### Convention de commits

Utilisez des messages clairs en français ou en anglais :

```
feat: ajouter le support des procédures sans retour
fix: corriger l'évaluation des expressions booléennes imbriquées
docs: ajouter un exemple de tri à bulles
test: couvrir les cas limites des tableaux
refactor: simplifier le visiteur d'expressions
```

---

## 📏 Standards de code

### Python

- **Linter** : Ruff (configuré dans `pyproject.toml`)
- **Ligne max** : 100 caractères
- **Python minimum** : 3.9
- **Style** : suivre le code existant, garder la simplicité

Avant chaque commit :

```bash
ruff check src/algolab
pytest
```

### Fichiers `.algo`

- Indentation : 2 espaces
- Mots-clés en PascalCase : `Variable`, `Debut`, `Fin`, `Si`, `Alors`, etc.
- Commentaires dans le code en français

### Tests

- Fichiers dans `tests/`
- Nommage : `test_<module>.py`
- Couvrir les cas nominaux ET les cas d'erreur
- Chaque nouvelle fonctionnalité doit venir avec des tests

---

## 🚀 Soumettre une Pull Request

1. Assurez-vous que `ruff check` et `pytest` passent
2. Décrivez clairement ce que fait votre PR
3. Référencez l'issue liée (ex: `Closes #12`)
4. Une PR = un sujet. Gardez les changements focalisés
5. Soyez patient — la review peut prendre quelques jours

### Template de PR

Votre PR sera automatiquement guidée par le template dans `.github/pull_request_template.md`.

---

## 🐛 Signaler un bug

Utilisez le [template de bug report](https://github.com/adandeigor/AlgoLab/issues/new?template=bug_report.md) et incluez :

- Le code `.algo` qui pose problème
- Le message d'erreur obtenu
- Le comportement attendu
- Votre OS et version de Python (ou binaire utilisé)

---

## 💡 Proposer une fonctionnalité

Utilisez le [template de feature request](https://github.com/adandeigor/AlgoLab/issues/new?template=feature_request.md). Gardez en tête la philosophie du projet :

- **Pédagogie avant complexité** — AlgoLab doit rester simple et accessible
- **Syntaxe française** — proche de ce qui est enseigné en cours
- **Messages d'erreur clairs** — chaque erreur doit aider l'apprenant

---

## ❓ Questions ?

- Ouvrez une [Discussion GitHub](https://github.com/adandeigor/AlgoLab/discussions) pour les questions générales
- Créez une issue pour les bugs ou propositions concrètes

Merci de contribuer à AlgoLab ! 🧪🇧🇯
