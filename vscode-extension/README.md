# Extension VS Code : AlgoLab

Cette extension apporte le support du langage pédagogique **AlgoLab** à l'éditeur Visual Studio Code.

## Fonctionnalités 🚀

- **Coloration Syntaxique** : Mise en surbrillance automatique des mots-clés (`SI`, `ALORS`, `TANT_QUE`, `VARIABLE`), des types (`ENTIER`, `BOOLEEN`) et des chaînes de caractères.
- **Auto-complétion (Snippets)** :
  - Tapez `algo` ou `programme` puis appuyez sur **Tabulation** pour générer instantanément l'architecture d'un programme (`VARIABLE ... DEBUT ... FIN`).
  - Tapez `si`, `sinon`, `pour`, `tant_que`, ou `fonction` pour insérer les blocs complets sans effort.
- **Exécution rapide** : bouton **Exécuter AlgoLab** dans la barre de l'éditeur.
- **Diagnostics VS Code** :
  - Bouton **Vérifier AlgoLab** pour lancer une validation et alimenter l'onglet *Problems*.
  - Validation automatique à la sauvegarde (configurable).

## Installation 📦

_Si le fichier `.vsix` a été généré :_

1. Ouvrez VS Code.
2. Allez dans l'onglet des extensions.
3. Cliquez sur les `...` en haut à droite > **Install from VSIX...**
4. Sélectionnez le fichier `.vsix` de l'extension (ex: `algolab-vscode-0.1.1.vsix`).
5. C'est prêt ! Ouvrez ou créez un fichier `.algo` pour en profiter.

## Configuration ⚙️

Paramètres disponibles dans VS Code :

- `algolab.executablePath` : chemin de la commande AlgoLab (par défaut `algolab`).
- `algolab.diagnosticsOnSave` : active/désactive les diagnostics à la sauvegarde.
- `algolab.diagnosticsTimeoutMs` : délai max (ms) pour la validation.
