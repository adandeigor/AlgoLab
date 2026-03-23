# Guide d'utilisation après installation

Ce document explique comment utiliser AlgoLab une fois installé sur Linux, macOS ou Windows.

## 1) Vérifier l'installation

Ouvre un terminal et exécute :

```bash
algolab --help
```

Si la commande répond, l'installation est correcte.

## 2) Exécuter un fichier `.algo`

Commande générale (tous systèmes) :

```bash
algolab chemin/vers/mon_programme.algo
```

Exemple :

```bash
algolab examples/hello_world.algo
```

## 3) Exécuter du code directement en ligne de commande

Commande générale :

```bash
algolab -c "Variable x : Entier Debut x <- 3 Ecrire x Fin"
```

## 4) Utilisation selon le système

### Linux

- Si installé via paquet `.deb`, la commande `algolab` est normalement disponible directement.
- Vérification :

```bash
which algolab
algolab --help
```

### macOS

- Si installé via binaire release, rends-le exécutable puis lance-le :

```bash
chmod +x ./algolab
./algolab --help
./algolab examples/hello_world.algo
```

- Pour l'utiliser globalement :

```bash
sudo mv ./algolab /usr/local/bin/algolab
algolab --help
```

### Windows

- Si tu utilises `algolab.exe`, ouvre PowerShell dans le dossier du binaire :

```powershell
.\algolab.exe --help
.\algolab.exe examples\hello_world.algo
```

- Pour l'usage global, ajoute le dossier contenant `algolab.exe` au `PATH` Windows.

## 5) Vérification rapide de bon fonctionnement

Crée un fichier `test.algo` avec :

```text
Variable x : Entier
Debut
  x <- 5
  Ecrire x
Fin
```

Puis exécute :

```bash
algolab test.algo
```

Sortie attendue : `5`

## 6) Dépannage rapide

- **`command not found: algolab` / `algolab n'est pas reconnu`**  
  Le binaire n'est pas dans le `PATH`. Lance avec chemin complet ou ajoute le dossier au `PATH`.

- **Erreur de permission (Linux/macOS)**  
  Rendre exécutable : `chmod +x algolab`.

- **Fichier introuvable**  
  Vérifie le chemin du fichier `.algo` et relance la commande depuis le bon dossier.
