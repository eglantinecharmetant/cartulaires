# Installation sur Linux (Ubuntu/Debian)

## Première utilisation  
Vous aurez sûrement besoin d'installer `python3`, `virtualenv` et `pip`, pour cela, ouvrez un terminal et tapez :  
`sudo apt-get install python3 libfreetype6-dev python3-pip python3-virtualenv`

Une fois cela instalé, téléchargez le repository `Chartes-TNAH/cartulaires.git`, lancez le dossier `cartulaires/` dans un terminal et tapez :  
`virtualenv ~/.env-cartulaires -p python3`  
Cela crée un environnement virtuel dans lequel pourront être installés les packages utilisés. Pour activer cet environnement virtuel, tapez :  
`source ~/.env-cartulaires/bin/activate`  
*Cette commande sera nécessaire à chaque fois que vous voudrez activer l'environnement virtuel pour travailler avec cts_creator.py.*  
  
Dans le même terminal, tapez :  
`pip install lxml`  
> il faut installer lxml-4.1.1

Cela installe le package `lxml` nécessaire pour la création des fichiers xml.  

Pour lancer `cts_creator.py`, tapez :  
`cd tools/`  
`python3 cts_creator.py`  


## Utilisation(s) ultérieure(s) :
Lancez le terminal depuis le dossier `cartulaires/` et entrez :  
`source ~/.env-cartulaires/bin/activate`  
puis lancez `cts_creator.py` depuis le dossier `tools/`.
