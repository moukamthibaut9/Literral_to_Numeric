dico1={"un":1,"deux":2,"trois":3,"quatre":4,"cinq":5,"six":6,"sept":7,"huit":8,"neuf":9,"onze":11,"douze":12,
    "treize":13,"quatorze":14,"quinze":15,"seize":16}
dico2={"mille":1000,"million":1000000,"millions":1000000,"milliard":1000000000,"milliards":1000000000}
dico={"un":1,"deux":2,"trois":3,"quatre":4,"cinq":5,"six":6,"sept":7,"huit":8,"neuf":9,"onze":11,"douze":12,"treize":13,
      "quatorze":14,"quinze":15,"seize":16,"dix":10,"vingt":20,"trente":30,"quarante":40,"cinquante":50,"soixante":60,
      "cent":100,"mille":1000,"million":1000000,"millions":1000000,"milliard":1000000000,"milliards":1000000000}

def appel_fonction(liste,start,stop):
    inter=0
    while start!=stop:
        start-=1
        if start==stop and stop!=0: continue
        if start>stop and liste[start]=="cent" and liste[start-1] in dico1.keys():
            inter+=100*dico[liste[start-1]]
            start-=1
        elif start>stop and liste[start]=="vingt" and liste[start-1]=="quatre":
            inter+=80
            start-=1
        else: inter+=dico[liste[start]]    
    return inter

def pow(nbr,p):
    if p==0: return 1
    elif p==1: return nbr
    elif p<0:
        print("Non pris en charge\n")
        return -1
    else:
        while p>1:
            nbr*=nbr
            p-=1
        return nbr

def strlen(chaine):
    len=0
    for letter in chaine:
        len+=1
    return len

def split(chaine):
    valeur=""
    liste=[]
    for i in range(strlen(chaine)):
        if chaine[i]!="\t" and chaine[i]!=" " and chaine[i]!="-":
            valeur+=chaine[i]
        elif valeur!="":
            liste.append(valeur)
            valeur=""
        if i==strlen(chaine)-1 and valeur!="":
            liste.append(valeur)
    return liste
        

def conversion_chaine_num(chaine):
    resultat=0
    len_liste_chaine=0
    liste_chaine=split(chaine)
    for elt in liste_chaine:
        if elt in dico.keys():
            len_liste_chaine+=1
        else:
            print("Impossible d'effectuer la conversion. Un probleme dans votre chaine.\n")
            return -1
    stop_indexe=0
    if "milliard" in liste_chaine or "milliards" in liste_chaine:
        if "milliard" in liste_chaine: start_indexe=liste_chaine.index("milliard")
        elif "milliards" in liste_chaine: start_indexe=liste_chaine.index("milliards")
        resultat+=appel_fonction(liste_chaine,start_indexe,stop_indexe)*dico["milliard"]
    if "million" in liste_chaine or "millions" in liste_chaine:
        if "milliard" in liste_chaine: stop_indexe=liste_chaine.index("milliard")
        elif "milliards" in liste_chaine: stop_indexe=liste_chaine.index("milliards")
        else: stop_indexe=0
        if "million" in liste_chaine: start_indexe=liste_chaine.index("million")
        elif "millions" in liste_chaine: start_indexe=liste_chaine.index("millions")
        resultat+=appel_fonction(liste_chaine,start_indexe,stop_indexe)*dico["millions"]
    if "mille" in liste_chaine and len_liste_chaine==1:resultat=1000
    elif "mille" in liste_chaine and len_liste_chaine!=1:
        if "million" in liste_chaine: stop_indexe=liste_chaine.index("million")
        elif "millions" in liste_chaine: stop_indexe=liste_chaine.index("millions")
        elif "milliard" in liste_chaine: stop_indexe=liste_chaine.index("milliard")
        elif "milliards" in liste_chaine: stop_indexe=liste_chaine.index("milliards")
        else: stop_indexe=0
        start_indexe=liste_chaine.index("mille")
        resultat+=appel_fonction(liste_chaine,start_indexe,stop_indexe)*dico["mille"]
    if liste_chaine[len_liste_chaine-1] not in dico2.keys():
        if "mille" in liste_chaine: stop_indexe=liste_chaine.index("mille")
        elif "million" in liste_chaine: stop_indexe=liste_chaine.index("million")
        elif "millions" in liste_chaine: stop_indexe=liste_chaine.index("millions")
        elif "milliard" in liste_chaine: stop_indexe=liste_chaine.index("milliard")
        elif "milliards" in liste_chaine: stop_indexe=liste_chaine.index("milliards")
        else: stop_indexe=0
        start_indexe=len_liste_chaine
        inter=0
        while start_indexe!=stop_indexe:
            start_indexe-=1
            if start_indexe==stop_indexe and (liste_chaine[stop_indexe]=="mille" or \
            liste_chaine[stop_indexe]=="million" or liste_chaine[stop_indexe]=="millions" or \
            liste_chaine[stop_indexe]=="milliard" or liste_chaine[stop_indexe]=="milliards"):
                continue
            if start_indexe>stop_indexe and liste_chaine[start_indexe]=="cent" and liste_chaine[start_indexe-1] in dico1.keys():
                inter+=100*dico[liste_chaine[start_indexe-1]]
                start_indexe-=1
            elif start_indexe>stop_indexe and liste_chaine[start_indexe]=="vingt" and liste_chaine[start_indexe-1]=="quatre":
                inter+=80
                start_indexe-=1
            else: inter+=dico[liste_chaine[start_indexe]]
        if liste_chaine[0]=="mille": resultat+=inter+1000
        else: resultat+=inter
    return resultat
    

print(conversion_chaine_num("neuf cent quatre vingt dix neuf milliards neuf cent quatre vingt dix neuf millions\
                            neuf cent quatre vingt dix neuf mille neuf cent quatre vingt dix neuf"),"\n")
print(conversion_chaine_num("neuf cent quatre vingt seize milliards cent cinquante mille huit"),"\n")
print(conversion_chaine_num("soixante dix sept  millions neuf cent quatre vingt dix neuf mille neuf cent quatre"),"\n")
print(conversion_chaine_num("mille quatre cent quarante trois"),"\n")
