# AlgoLab

Interpréteur pédagogique d'un pseudo-code, basé sur Lark. Le projet couvre la grammaire, l'AST, l'exécution et un système d'erreurs pédagogiques.

## 🚀 Installation & Démarrage rapide

### Option 1 : Installation avec Python (Recommandé)

Si vous avez Python (>= 3.9) installé, vous pouvez installer AlgoLab globalement :

```bash
pip install -e .
```

Vous pouvez ensuite utiliser la commande `algolab` de n'importe où :

- Lancer un fichier : `algolab examples/hello_world.algo`
- Lancer du code inline : `algolab -c 'Variable x : Entier Debut x <- 3 Ecrire x Fin'`

### Option 2 : Binaire Autonome (Sans Python)

Pour ceux qui n'ont pas Python, un exécutable autonome peut être généré :

```bash
pip install pyinstaller
pyinstaller --name algolab --onefile src/algolab/main.py
```

Le fichier exécutable compilé sera disponible dans le dossier `dist/`. Vous n'aurez qu'à le distribuer aux étudiants, ils pourront l'exécuter directement sans aucune dépendance !

## 📚 Documentation & Exemples

- Documentation de conception : voir `docs/`
- Code source : `src/algolab/`
- Exemples de code : `examples/`
- Tests : `tests/`
