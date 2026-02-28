#!/usr/bin/env bash
# Script de génération du paquet Debian (.deb) pour AlgoLab

set -e

# Se placer à la racine du projet
cd "$(dirname "$0")/.."
PROJECT_ROOT=$(pwd)

echo "=== Construction du binaire autonome avec PyInstaller ==="
# Vérification d'un espace virtuel et dépendances (on installe si besoin)
if [ ! -d ".venv" ]; then
    echo "Environnement vituel introuvable. Création de .venv..."
    python3 -m venv .venv
fi
source .venv/bin/activate
pip install -e .
pip install pyinstaller

# Compilation
pyinstaller --name algolab --onefile src/algolab/main.py

echo "=== Préparation de l'arborescence du paquet Debian ==="
BUILD_DIR="${PROJECT_ROOT}/build/debian"
VERSION="0.1.0"
DEB_NAME="algolab_${VERSION}_amd64"
DEB_DIR="${BUILD_DIR}/${DEB_NAME}"

# Nettoyage
rm -rf "$BUILD_DIR"
mkdir -p "${DEB_DIR}/usr/bin"
mkdir -p "${DEB_DIR}/DEBIAN"

# Copie de l'exécutable généré
cp "${PROJECT_ROOT}/dist/algolab" "${DEB_DIR}/usr/bin/"
chmod 755 "${DEB_DIR}/usr/bin/algolab"

echo "=== Génération du fichier control ==="
cat <<EOF > "${DEB_DIR}/DEBIAN/control"
Package: algolab
Version: ${VERSION}
Section: devel
Priority: optional
Architecture: amd64
Maintainer: Votre Nom <votre.email@example.com>
Description: Un interpréteur pédagogique d'un pseudo-code en français (Lark parser).
 Facilite l'apprentissage de l'algorithmique.
EOF

echo "=== Construction du paquet .deb ==="
dpkg-deb --build "${DEB_DIR}" "${PROJECT_ROOT}/dist/"

echo "Succès ! Le fichier .deb se trouve dans ${PROJECT_ROOT}/dist/${DEB_NAME}.deb"
echo "Pour l'installer localement : sudo dpkg -i dist/${DEB_NAME}.deb"
