#sandra nitchi
#TP1

def count_word():
    chaine = input("entrez une chaine de mots (ne mettez pas d'espace au debut)")
    wordsNumber = chaine.count(" ") + 1
    print("le nombre de mots dans cette chaine est:", wordsNumber)

count_word()
