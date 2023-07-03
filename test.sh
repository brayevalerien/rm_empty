#!/bin/bash

# Créer une structure de répertoires pour le test
mkdir -p test_dir/sub_dir1/sub_sub_dir1
mkdir -p test_dir/sub_dir1/sub_sub_dir2
mkdir -p test_dir/sub_dir2

# Créer des fichiers vides et non vides pour le test
echo "Contenu du fichier 1" > test_dir/file1.txt
echo "Contenu du fichier 2" > test_dir/file2.txt
echo "Contenu du fichier 3" > test_dir/sub_dir1/file3.txt
echo "Contenu du fichier 4" > test_dir/sub_dir1/sub_sub_dir1/file4.txt

# Créer des fichiers vides pour le test
touch test_dir/empty_file1.txt
touch test_dir/empty_file2.txt
touch test_dir/sub_dir1/empty_file3.txt
touch test_dir/sub_dir1/sub_sub_dir1/empty_file4.txt

# Afficher la structure du répertoire avant l'exécution du script
echo "=== Structure du répertoire avant l'exécution ==="
find test_dir

# Exécuter le script Python pour supprimer les répertoires vides
echo 
echo "Executing rm_empty.py..."
python3 rm_empty.py --rm-files test_dir
echo "Done."
echo 

# Afficher la structure du répertoire après l'exécution du script
echo "=== Structure du répertoire après l'exécution ==="
find test_dir

# Supprimer le répertoire de test
rm -rf test_dir