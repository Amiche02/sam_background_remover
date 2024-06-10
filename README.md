Pour exécuter le script, suivez les étapes suivantes:

### Étape 1: Pré-requis
Assurez-vous d'avoir installé les bibliothèques Python nécessaires. Vous pouvez installer les bibliothèques requises avec pip :

```sh
pip -r requirements.txt
```

### Étape 2: Préparer vos images et le modèle SAM
1. **Images** : Placez les images dans un dossier ou spécifiez le chemin d'une seule image.
2. **Modèle SAM** : Téléchargez le fichier du modèle SAM (`sam_vit_h_4b8939.pth`) et placez-le dans un dossier `sam_pt` à côté de votre script.

### Étape 3: Enregistrer le script dans un fichier
Enregistrez le script fourni dans un fichier nommé par exemple `remove_background.py`.

### Étape 4: Exécuter le script
Ouvrez un terminal et exécutez le script en spécifiant les arguments nécessaires. Voici quelques exemples de commandes pour exécuter le script :

#### Exemple 1: Traiter un dossier d'images
```sh
python remove_background.py --input_dir path/to/input_directory --output_dir path/to/output_directory
```

#### Exemple 2: Traiter une seule image
```sh
python remove_background.py --input_dir test_inputs\DSC00754.JPG --output_dir test_outputs
```

### Explication des arguments
- `--input_dir` : Le chemin du dossier contenant les images à traiter.
- `--input_image` : Le chemin d'une seule image à traiter.
- `--output_dir` : Le chemin du dossier où les images traitées seront enregistrées.

### Exemple Complet
Si vous avez un dossier `images` contenant des images et vous voulez enregistrer les résultats dans un dossier `output`, utilisez la commande suivante :

```sh
python remove_background.py --input_dir images --output_dir output
```

Assurez-vous de remplacer `path/to/input_directory` et `path/to/output_directory` par les chemins réels sur votre système.

### Note
- Si vous utilisez un environnement virtuel, assurez-vous qu'il est activé avant d'installer les bibliothèques et d'exécuter le script.
- Assurez-vous que le fichier `sam_vit_h_4b8939.pth` est téléchargé et placé correctement dans le dossier `sam_pt` situé dans le même répertoire que le script.

En suivant ces étapes, vous pourrez exécuter le script et tester la suppression de fond des images en utilisant le modèle SAM.