# Bitcoin_Wallet
TD2 - Blockchain Programming 2022/2023
RODRIGUES Thomas & SIROT Antoine

## Infos Utilisation
Afin d'utiliser le code Python il suffit d'écrire la commande : "python td2_bitcoin.py"

## BIP 39 
Dans cette partie nous allons suivre les étapes ci-dessous afin de créer et afficher une seed en mnémonique voire d'en importer une.

<img width="1440" alt="Capture d’écran 2022-09-30 à 14 08 32" src="https://user-images.githubusercontent.com/101109062/193266470-65203baa-340e-4e59-8b75-7742e44075cc.png">

* Création de la seed:

Pour créer notre seed, nous avons utilisé la bibliothèque Secrets de python, qui est plus sécurisé que Random pour la cryptographie.
Avec secrets.token_bytes(), nous avons obtenu cette seed en hexadecimal ce qui a rendu la conversion en binaire puis en décimal plus facile.

<img alt="cap code1" src="https://user-images.githubusercontent.com/113580716/193595397-871a1b87-62d2-46c8-a598-765ec1e8dbca.PNG" width="1300" title="hover text">

* Hachage de la seed:

Ensuite nous avons utilisé la bibliothèque Hashlib afin d'employer la fonction Sha256 pour hacher la seed que nous avons par la suite convertie en binaire pour ajouter ses 4 premiers bits (le checksum) à l'entropie. 
<img alt="cap code1" src="https://user-images.githubusercontent.com/113580716/193595720-5d6b3ffa-8dd0-4a78-8c3f-b20e790a5486.PNG" width="1300" title="hover text">

* Affichage de la seed en mnémonique:

Puis nous avons découpé la seed en lot de 11 bits pour pouvoir attribuer à chaque lot un mot selon la liste BIP 39 et afficher la seed en mnémonique.
<img alt="cap code1" src="https://user-images.githubusercontent.com/113580716/193596076-92ccc63c-96eb-4c47-8df6-9159933f3d14.PNG" width="1300" title="hover text">

* Vérification:

Puis avec l'entropie et le site https://iancoleman.io/bip39/, nous avons vérifié le checksum ainsi que le BIP39 mnemonic et avons vu qu'ils étaient en concordance.

<img  src="https://user-images.githubusercontent.com/113580716/193586263-7a14d98e-cd5f-4cfc-ab64-06565c12880b.PNG" width="900" title="hover text">




## BIP 32 
Dans cette partie nous allons générer des clés enfants à différents index et dérivations après avoir extrait la master private key, le chain code et la master public key.

<img width="1440" alt="cap code2" src="https://user-images.githubusercontent.com/113580716/193590517-dba43ab6-f1d2-4ef8-97a7-85cdec422fe1.PNG" width="600" title="hover text">

<img width="1440" alt="Capture d’écran 2022-09-30 à 14 08 57" src="https://user-images.githubusercontent.com/101109062/193266497-057a8852-1800-4224-a83b-50d15df8ca7c.png">

https://sha512.online
<img  src="https://user-images.githubusercontent.com/113580716/193586311-16a284b2-4f4e-40a5-bb8c-7e6f1288b82b.PNG" width="400" title="hover text">
