# AlgoLab

Interpréteur pédagogique d'un pseudo-code, basé sur Lark. Le projet couvre la grammaire, l'AST, l'exécution et un système d'erreurs pédagogiques.

## 🚀 Installation & Démarrage rapide

### Option 1 : Installation avec Python (Recommandé)

Si vous avez Python (>= 3.9) installé, vous pouvez installer AlgoLab globalement :

```bash
pip install .
```

Vous pouvez ensuite utiliser la commande `algolab` de n'importe où :

- Lancer un fichier : `algolab examples/hello_world.algo`
- Lancer du code inline : `algolab -c 'Variable x : Entier Debut x <- 3 Ecrire x Fin'`

### Option 2 : Binaire Autonome (Sans Python)

Pour ceux qui n'ont pas Python, un exécutable autonome peut être généré :

```bash
pip install pyinstaller
pyinstaller algolab.spec
```

Le fichier exécutable compilé sera disponible dans le dossier `dist/`. Vous n'aurez qu'à le distribuer aux étudiants, ils pourront l'exécuter directement sans aucune dépendance !

### Option 3 : Artefacts de release (Windows/macOS/Linux)

Depuis les releases GitHub :

- Linux : paquet `.deb`
- Windows : exécutable `algolab.exe`
- macOS : binaire `algolab`
- VS Code : extension `algolab-vscode.vsix` (installation manuelle)

## ✅ Qualité et tests

Installer les outils de développement :

```bash
pip install -e ".[dev]"
```

Vérifications recommandées :

```bash
ruff check .
pytest --cov=src/algolab --cov-report=term-missing
```

## 📚 Documentation & Exemples

- Documentation de conception : voir `docs/`
- Guide d'utilisation après installation (Linux/macOS/Windows) : `GUIDE_UTILISATION.md`
- Guide d'installation de l'extension VS Code : `vscode-extension/README.md`
- Code source : `src/algolab/`
- Exemples de code : `examples/`
- Tests : `tests/`
