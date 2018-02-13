############################################################
#      DECLARATION DES CONSTANTES ET DES FONCTIONS         #
############################################################


# Déclaration d'une constante contenant le code utilisé pour le "namespace"
CODE_NAMESPACE = "FrCart"

# Déclaration des fonctions :  

def create(route):
    """
    Crée un fichier à partir d'un chemin donné en option.
    :param route : chemin entier depuis  tool/
    :type route : string
    returns: rien
    """
    with open(route, "w") as fichier:
        fichier.write(information[1]) # à améliorer avec lxml, envisager de créer une autre fonction
    return

def formulaire_textgrp():
    """
    Génère une série de questions pour un textgroup qui permet de récupérer des informations dans une liste que l'on retourne
    returns: une liste des réponses données
    rtype: list
    """
    code_textgrp = input("Quel est le code de textgroup ? : ")
    nom_textgrp = input("Quel est le nom du textgroup ? : ")
    lang_nom_textgrp = input("Quelle est la langue utilisée pour ce nom de textgroup ? : ")
    while len(lang_nom_textgrp) != 3 :
        print("Erreur sur le format de la langue : veuillez entrer un code à 3 lettres")
        lang_nom_textgrp = input("Quelle est la langue utilisée pour ce nom de textgroup ? : ")

    chemin = "../data/" + code_textgrp + "/__cts__.xml"

    resultat = [chemin, code_textgrp, lang_nom_textgrp, nom_textgrp]
    return resultat

def formulaire_work(): 
    """
    Génère une série de questions pour un work qui permet de récupérer des informations dans une liste que l'on retourne
    returns: une liste des réponses données
    rtype: list
    """
    code_textgrp = input("Quel est le code de textgroup ? : ")
    code_work = input("Quel est le code de l'oeuvre ? : ")
    lang_work = input("Quelle est la langue de l'oeuvre ? : ")
    while len(lang_work) != 3 :
        print("Erreur sur le format de la langue de l'oeuvre : veuillez entrer un code à 3 lettres")
        lang_work = input("Quelle est la langue de l'oeuvre ? : ")

    titre_work = input("Quel est le nom de l'oeuvre ? : ")
    lang_titre_work = input("Quelle est la langue utilisée pour le nom de l'oeuvre ? : ")
    while len(lang_titre_work) != 3 :
        print("Erreur sur le format de la langue du nom de l'oeuvre : veuillez entrer un code à 3 lettres")
        lang_titre_work = input("Quelle est la langue utilisée pour ce nom de l'oeuvre ? : ")

    label_edition = input("Quelle est le nom de la présente edition de l'oeuvre ? : ")
    lang_label_ed = input("Quelle est la langue utilisée pour nommer cette edition ? : ")
    while len(lang_label_ed) != 3 :
        print("Erreur sur le format de la langue du nom d'edition : veuillez entrer un code à 3 lettres")
        lang_label_ed = input("Quelle est la langue utilisée pour nommer cette edition ? : ")

    code_edition = input("Quel est le code de l'edition ? : ")
    desc_ed = input("Comment souhaitez-vous decrire cette edition ? : ")
    lang_desc_ed = input("Quelle est la langue de votre description ? : ")
    while len(lang_desc_ed) != 3 :
        print("Erreur sur le format de la langue de la description de l'edition : veuillez entrer un code à 3 lettres")
        lang_desc_ed = input("Quelle est la langue utilisée pour decrire cette edition ? : ")

    chemin = "../data/" + code_textgrp + "/" + code_work + "/__cts__.xml"

    resultat = [chemin, code_textgrp, code_work, lang_titre_work, titre_work, label_edition, lang_label_ed, code_edition, desc_ed, lang_desc_ed, lang_work]
    return resultat

def valider_textgrp(liste_resultat):
    """
    Enregistre et retourne une validation par l'utilisateur d'un ensemble de valeurs recueillies et affichées de manière lisible.
    :param liste_resultat : une liste qui contient les réponses d'un formulaire_textgrp
    :type liste_resultat : list
    returns: une variable qui contient "o" (oui) ou "n" (non)
    rtype: string
    """
    print("\nUn fichier __cts__.xml sera créé à l'emplacement suivant : " + liste_resultat[0])
    print("L'élément <textgroup> aura comme attribut : @urn=\"urn:cts:" + CODE_NAMESPACE + ":" + liste_resultat[1])
    print("L'élément <groupname> aura comme attribut : @xml:lang=\"" + liste_resultat[2] + "\"")
    print("L'élément <groupname> contiendra le texte suivant : " + liste_resultat[3])
    valide = input("Valider ? [o/n]")
    while not((valide == "o") or (valide == "n")):
    	valide = input("Valider ? [o/n]")
    return valide

def valider_work(liste_resultat):
    """
    Enregistre et retourne une validation par l'utilisateur d'un ensemble de valeurs recueillies et affichées de manière lisible.
    :param liste_resultat : une liste qui contient les réponses d'un formulaire_textgrp
    :type liste_resultat : list
    returns: une variable qui contient "o" (oui) ou "n" (non)
    rtype: string
    """
    print("\nUn fichier __cts__.xml sera créé à l'emplacement suivant : " + liste_resultat[0] + "\"")
    print("L'élément <work> aura comme attribut : @groupUrn=\"urn:cts:" + CODE_NAMESPACE + ":" + liste_resultat[1] + "\"")
    print("L'élément <work> aura comme attribut : @urn=\"urn:cts:" + CODE_NAMESPACE + ":" + liste_resultat[1] + ":" + liste_resultat[2] + "\"")
    print("L'élément <work> aura comme attribut : @xml:lang=\"" + liste_resultat[10] + "\"") # On a vu qu'on peut mettre "mul" s'il y a plusieurs langues
    print("L'élément <title> contiendra le texte suivant : " + liste_resultat[4])
    print("L'élément <title> aura pour attribut : @xml:lang= \"" + liste_resultat[3] + "\"")
    print("L'élément <edition> contiendra le texte suivant : " + liste_resultat[5])
    print("L'élément <edition> aura pour attribut : @xml:lang= \"" + liste_resultat[6] + "\"")
    print("L'élément <edition> aura pour attribut : @urn=\"urn:cts:" + CODE_NAMESPACE + ":" + liste_resultat[1] + ":" + liste_resultat[2] + ":" + liste_resultat[7] + "\"") # correction de liste_resultat[5] en liste_resultat[7]
    print("L'élément <description> contiendra le texte suivant : " + liste_resultat[8])
    print("L'élément <description> aura pour attribut : @xml:lang= \"" + liste_resultat[9] + "\"")
    valide = input("Valider ? [o/n]")
    while not((valide == "o") or (valide == "n")):
    	valide = input("Valider ? [o/n]")
    return valide

def create_cts_textgrp(liste_information):
	'''
	Crée à partir d'une liste de résultats un fichier __cts__.xml niveau textgroup
	:type liste_information: list

	'''
	# importe le module etree de la library lxml désigné par ET pour simplifier (utilisation courante)
	import lxml.etree as ET
	urn_calcul = 'urn:cts:' + ':' + liste_information[4] + ':' + liste_information[1]

	#définit l'élément racine du fichier
	root = ET.Element("textgroup")
	#ajoute des attributs à l'élément racine textgroup
	root.attrib['xmlns'] = 'http://chs.harvard.edu/xmlns/cts'
	root.attrib['urn'] = urn_calcul

	groupname = ET.SubElement(root,"groupname")
	# groupname.set("xml:lang","mul") et groupname.attrib['xml:lang'] = 'langue' ne fonctionnait pas 
	#la solution a été trouvée sur http://bendustries.org/wp/?p=21
	attr = groupname.attrib
	attr['{http://www.w3.org/XML/1998/namespace}lang'] = liste_information[2]
	groupname.text = liste_information[3]
	tree = ET.ElementTree(root)
	# pretty_print permet l'indentation correcte des fichiers xml
	tree.write(liste_information[0], pretty_print = True)

	return 

def create_cts_work (liste_information):
	'''
	Crée à partir d'une liste de résultats un fichier __cts__.xml niveau work
	:type liste_information: list

	'''

	import lxml.etree as ET
	urn_group = 'urn:cts:'+ liste_information[11] + liste_information[1]
	urn_work = urn_group + '.' + liste_information[3]
	urn_edition = liste_information[11] + ":" + liste_information[1] + ":" + liste_information[2] + ":" + liste_information[7]

	root = ET.Element("work")
	root.attrib['xmlns'] = 'http://chs.harvard.edu/xmlns/cts'
	root.attrib['groupUrn'] = urn_group
	root.attrib['urn'] = urn_work
	attr_lang_work = root.attrib
	attr_lang_work['{http://www.w3.org/XML/1998/namespace}lang'] = liste_information[10]
#	root.attrib['xmlns:cpt'] = 'http://purl.org/capitains/ns/1.0#' cette ligne pose le même problème que xml:lang
#	root.attribt['xmlns:dc'] = 'http://purl.org/dc/elements/1.1/'

	title = ET.SubElement(root, "title")
	attr_lang_title = title.attrib
	attr_lang_title['{http://www.w3.org/XML/1998/namespace}lang'] = liste_information[3]
	title.text = liste_information[4]

	edition = ET.SubElement(root, "edition")
	edition.attrib['workUrn'] = urn_edition
	edition.attrib['urn'] = ""
	attr_lang_edition = edition.attrib
	attr_lang_edition['{http://www.w3.org/XML/1998/namespace}lang'] = liste_information[6]
	edition.text = liste_information[5]

	label = ET.SubElement(edition, "label")
	attr = label.attrib
	attr['{http://www.w3.org/XML/1998/namespace}lang'] = 'langue_label'

	description = ET.SubElement(edition, "description")
	attr = description.attrib
	attr['{http://www.w3.org/XML/1998/namespace}lang'] = liste_information[9]

	tree = ET.ElementTree(root)

	tree.write(liste_information[0], pretty_print = True)

	return

# Fin Déclaration des fonctions

############################################################
#                     DEBUT DE L'EXECUTION                 #
############################################################

valide = "n"

# sélection du type de fichier à créer, deux options possibles : "textgroup" ou "work"
choix_branche = input("Souhaitez-vous créer un fichier __cts__.xml pour un niveau textgroup ou un niveau work ? [textgroup/work] : ")
while not((choix_branche == "textgroup") or (choix_branche == "work")):
    choix_branche = input("Réponse impossible à traiter. \nSouhaitez-vous créer un fichier __cts__.xml pour un niveau textgroup ou un niveau work ? [textgroup/work] : ")

# branche "textgroup"
if choix_branche == "textgroup" : 
    while valide != "o":
        information = formulaire_textgrp()
        valide = valider_textgrp(information)
    try:
        information.append(CODE_NAMESPACE)
        create_cts_textgrp(information)
        print("Félicitation, vous avez créé un fichier __cts__.xml, avec plein de trucs dedans !")
    except FileNotFoundError:
        print("Création du fichier interrompue : erreur dans le calcul du chemin. \nVeuillez relancer le programme sans faire d'erreur")

# branch "work"
elif choix_branche == "work" :
    while valide != "o":
        information = formulaire_work()
        valide = valider_work(information)
    try:
    	information.append(CODE_NAMESPACE)
    	create_cts_work(information)
    	print("Félicitation, vous avez créé un fichier __cts__.xml, avec plein de trucs dedans !")
    except FileNotFoundError:
    	print("Création du fichier interrompue : erreur dans le calcul du chemin. \nVeuillez relancer le programme sans faire d'erreur")