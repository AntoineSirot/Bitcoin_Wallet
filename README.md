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
<img alt="cap code2" src="https://user-images.githubusercontent.com/113580716/193595720-5d6b3ffa-8dd0-4a78-8c3f-b20e790a5486.PNG" width="1300" title="hover text">

* Affichage de la seed en mnémonique:

Puis nous avons découpé la seed en lot de 11 bits pour pouvoir attribuer à chaque lot un mot selon la liste BIP 39 et afficher la seed en mnémonique.
<img alt="cap code3" src="https://user-images.githubusercontent.com/113580716/193596076-92ccc63c-96eb-4c47-8df6-9159933f3d14.PNG" width="1300" title="hover text">

* Vérification:

Puis avec l'entropie et le site https://iancoleman.io/bip39/, nous avons vérifié le checksum ainsi que le BIP39 mnemonic et avons vu qu'ils étaient en concordances.

<img  src="https://user-images.githubusercontent.com/113580716/193586263-7a14d98e-cd5f-4cfc-ab64-06565c12880b.PNG" width="900" title="hover text">




## BIP 32 
Dans cette partie nous allons générer des clés enfants à différents index et dérivations après avoir extrait la master private key, le chain code et la master public key.

<img width="1440" alt="Capture d’écran 2022-09-30 à 14 08 57" src="https://user-images.githubusercontent.com/101109062/193266497-057a8852-1800-4224-a83b-50d15df8ca7c.png">

* Extraction de la master private key et du chain code:

Nous avons tout d'abord encoder le mnémonique avec Sha512 pour récupérer le hash total, puis nous l'avons séparé en deux pour obtenir la master private key (la partie gauche du hash) ainsi que le chain code (la partie droite du hash).

Nous avons vérifié si notre valeur du hachage de la phrase mnemonique, obtenue par Sha512 était la bonne grâce au site https://sha512.online:

<img  src="https://user-images.githubusercontent.com/113580716/193586311-16a284b2-4f4e-40a5-bb8c-7e6f1288b82b.PNG" width="400" title="hover text">

<img alt="cap code4" src="https://user-images.githubusercontent.com/113580716/193599884-80266288-f14b-48b7-afba-aaa80aefb93a.PNG" width="1300" title="hover text">

* Extraction de la master public key:

Pour extraire la master public key, on commence par décoder la clé privée en bits puis on génère la public key avec SECP256k1 (la courbe eliptique utilisée par Bitcoin) grâce à la bibliothèque de l'algorithme ecdsa. Puis nous les réencodons en bits en ajoutant au début de la public key, 02 ou 03 en fonction de son dernier bit non compréssé.

<img width="1000" alt="cap code5" src="https://user-images.githubusercontent.com/113580716/193613648-f468e61f-1240-4a79-9d32-65e5b215599d.PNG" title="hover text">

* Génération d'une clé enfant:

Nous encodons la public key parent, le chaincode avec Sha512

<img width="1300" alt="cap code6" src="https://user-images.githubusercontent.com/113580716/193613760-cff697e7-08a3-4650-9877-41e80afc7e50.PNG" title="hover text">

* Génération d'une clé enfant à l'index N:

Afin d'encoder une clé enfant à un index précis nous ajoutons l'index voulu codé sur 32 bits en binaire dans le hash du Sha512 

<img width="1300" alt="cap code7" src="https://user-images.githubusercontent.com/113580716/193613801-4461b05d-30f7-49f4-8552-499f59f0586f.PNG" title="hover text">





