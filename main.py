"""code pour retourner une liste de tuple comprenant 
les caracteres d une liste et leurs occurences"""
#### Imports et définition des variables globales
import sys
#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
     passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    car = [s[0]]
    occ = [1]
    n = len(s)
    for i in range(1,n):
        if s[i] == s[i-1]:
            occ[-1] += 1
        else :
            car.append(s[i])
            occ.append(1)
    l = list(zip(car,occ,strict = True))
    return l


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    sys.setrecursionlimit(4000)
    n = len(s)
    # cas en fin de liste, donc liste vide
    if not s :
        return []
    # cas de base, premier caractere
    base = s[0]
    c = 1
    # recherche nombre de caractères identiques au premier
    for i in range(1,n) :
        if s[i] == base :
            c += 1
        else :
            break
    # on enleve la base de la liste avec replace par "" et puis appel récursif
    return [(base, c)] + artcode_r(s[c:])


#### Fonction principale
def main():
    """main function pour appel des secondaires"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()