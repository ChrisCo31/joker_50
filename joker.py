import random

#créer variable liste current_question 
#créer variable liste jokers_available 
#print réponses 
#exe : recup liste des 4 / isole bonne réponse 
#print 2 réponse sur les 4 dont la BR 

current_question = ["Quelle est la couleur du cheval blanc d'Henri IV ?", "rouge", "vert", "blanc", "rose", "blanc"]
jokers_available = ["50/50", "public", "ami"]

def joker_50(current_question):

    #print(*current_question[0:5])

    # from general index, we isolated all the answers
    liste_reponses= current_question[1:5]
    # from general index, we isolated the good answer. 
    bonne_reponse = current_question[5]
    # we create an empty table which will collect all the bad answers
    liste_mauvaises_reponses = []


    #retrieve bad answers by comparing all the answers by good answer
    for i,val in enumerate(current_question[1:5]):
        if (val == bonne_reponse):
            i= i+1
        else:
            liste_mauvaises_reponses.append(val)
            
    #Select randomly one bad answer among all bad answers
    rm=random.choice(liste_mauvaises_reponses)

    #Print 50/50 answers with 1 random choice bad answer and the good answer
    liste_50=[rm, bonne_reponse]
    random.shuffle(liste_50)
    print(liste_50)


